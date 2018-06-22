import io
import math
import re

import discord
from discord.ext import commands
from discord.ext.commands import BucketType

from objects.glimcontext import GlimContext
from utils import colors, http, render, sqlite as sql, utils
from objects.logger import Log
from objects import errors

log = Log(__name__)


class Canvas:
    def __init__(self, bot):
        self.bot = bot

    # =======================
    #          DIFF
    # =======================

    @commands.cooldown(1, 5, BucketType.guild)
    @commands.group(name="diff", invoke_without_command=True, aliases=["d"])
    async def diff(self, ctx, *args):
        if len(args) < 1:
            return
        if args[0] == "-f":
            if len(args) < 3:
                return
            f = sql.guild_get_by_faction_name_or_alias(args[1])
            if not f:
                await ctx.send("That faction could not be found.")  # TODO: Translate
                return
            name = args[2]
            zoom = args[3] if len(args) >= 4 else "#1"
            t = sql.template_get_by_name(f['id'], name)
        else:
            name = args[0]
            zoom = args[1] if len(args) >= 2 else "#1"
            t = sql.template_get_by_name(ctx.guild.id, name)
        if t:
            data = await http.get_template(t.url)
            try:
                max_zoom = int(math.sqrt(4000000 // (t.width * t.height)))
                zoom = int(zoom[1:]) if zoom and zoom.startswith("#") else 1
                zoom = max(1, min(zoom, max_zoom))
            except ValueError:
                zoom = 1

            fetchers = {
                'pixelcanvas': render.fetch_pixelcanvas,
                'pixelzio': render.fetch_pixelzio,
                'pixelzone': render.fetch_pixelzone,
                'pxlsspace': render.fetch_pxlsspace
            }

            await render.diff(ctx, t.x, t.y, data, zoom, fetchers[t.canvas], colors.by_name[t.canvas])
            return
        await ctx.invoke_default("diff")

    @commands.cooldown(1, 5, BucketType.guild)
    @diff.command(name="pixelcanvas", aliases=["pc"])
    async def diff_pixelcanvas(self, ctx, *, raw_arg: str):
        args = await Canvas.parse_diff(ctx, raw_arg)
        if args:
            await render.diff(*args, render.fetch_pixelcanvas, colors.pixelcanvas)

    @commands.cooldown(1, 5, BucketType.guild)
    @diff.command(name="pixelzio", aliases=["pzi"])
    async def diff_pixelzio(self, ctx, *, raw_arg: str):
        args = await Canvas.parse_diff(ctx, raw_arg)
        if args:
            await render.diff(*args, render.fetch_pixelzio, colors.pixelzio)

    @commands.cooldown(1, 5, BucketType.guild)
    @diff.command(name="pixelzone", aliases=["pz"])
    async def diff_pixelzone(self, ctx, *, raw_arg: str):
        args = await Canvas.parse_diff(ctx, raw_arg)
        if args:
            await render.diff(*args, render.fetch_pixelzone, colors.pixelzone)

    @commands.cooldown(1, 5, BucketType.guild)
    @diff.command(name="pxlsspace", aliases=["ps"])
    async def diff_pxlsspace(self, ctx, *, raw_arg: str):
        args = await Canvas.parse_diff(ctx, raw_arg)
        if args:
            await render.diff(*args, render.fetch_pxlsspace, colors.pxlsspace)

    # =======================
    #        PREVIEW
    # =======================

    @commands.cooldown(1, 5, BucketType.guild)
    @commands.group(name="preview", invoke_without_command=True, aliases=["p"])
    async def preview(self, ctx):
        await ctx.invoke_default("preview")

    @commands.cooldown(1, 5, BucketType.guild)
    @preview.command(name="pixelcanvas", aliases=["pc"])
    async def preview_pixelcanvas(self, ctx, *, coordinates: str):
        args = await Canvas.parse_preview(ctx, coordinates)
        if args:
            await render.preview(*args, render.fetch_pixelcanvas)

    @commands.cooldown(1, 5, BucketType.guild)
    @preview.command(name="pixelzio", aliases=["pzi"])
    async def preview_pixelzio(self, ctx, *, coordinates: str):
        args = await Canvas.parse_preview(ctx, coordinates)
        if args:
            await render.preview(*args, render.fetch_pixelzio)

    @commands.cooldown(1, 5, BucketType.guild)
    @preview.command(name="pixelzone", aliases=["pz"])
    async def preview_pixelzone(self, ctx, *, coordinates: str):
        args = await Canvas.parse_preview(ctx, coordinates)
        if args:
            await render.preview(*args, render.fetch_pixelzone)

    @commands.cooldown(1, 5, BucketType.guild)
    @preview.command(name="pxlsspace", aliases=["ps"])
    async def preview_pxlsspace(self, ctx, *, coordinates: str):
        args = await Canvas.parse_preview(ctx, coordinates)
        if args:
            x = max(0, min(1279, args[1]))
            y = max(0, min(719, args[2]))
            await render.preview(ctx, x, y, args[3], render.fetch_pxlsspace)

    # =======================
    #        QUANTIZE
    # =======================

    @commands.cooldown(1, 5, BucketType.guild)
    @commands.group(name="quantize", invoke_without_command=True, aliases=["q"])
    async def quantize(self, ctx):
        await ctx.invoke_default("quantize")

    @commands.cooldown(1, 5, BucketType.guild)
    @quantize.command(name="pixelcanvas", aliases=["pc"])
    async def quantize_pixelcanvas(self, ctx, *args):
        data = await self.parse_quantize(ctx, "pixelcanvas", args)
        if data:
            await render.quantize(ctx, data, colors.pixelcanvas)

    @commands.cooldown(1, 5, BucketType.guild)
    @quantize.command(name="pixelzio", aliases=["pzi"])
    async def quantize_pixelzio(self, ctx, *args):
        data = await self.parse_quantize(ctx, "pixelzio", args)
        if data:
            await render.quantize(ctx, data, colors.pixelzio)

    @commands.cooldown(1, 5, BucketType.guild)
    @quantize.command(name="pixelzone", aliases=["pz"])
    async def quantize_pixelzone(self, ctx, *args):
        data = await self.parse_quantize(ctx, "pixelzone", args)
        if data:
            await render.quantize(ctx, data, colors.pixelzone)

    @commands.cooldown(1, 5, BucketType.guild)
    @quantize.command(name="pxlsspace", aliases=["ps"])
    async def quantize_pxlsspace(self, ctx, *args):
        data = await self.parse_quantize(ctx, "pxlsspace", args)
        if data:
            await render.quantize(ctx, data, colors.pxlsspace)

    # =======================
    #         GRIDIFY
    # =======================

    @commands.cooldown(1, 5, BucketType.guild)
    @commands.command(name="gridify", aliases=["g"])
    async def gridify(self, ctx, *args):
        faction = None
        color = 8421504
        iter_args = iter(args)
        a = next(iter_args, None)
        while a in ["-f", "-c"]:
            if a == "-f":
                faction = sql.guild_get_by_faction_name_or_alias(next(iter_args, None))
                if not faction:
                    await ctx.send("That faction could not be found.")  # TODO: Translate
                    return
            if a == "-c":
                try:
                    color = abs(int(next(iter_args, None), 16) % 16777215)
                except ValueError:
                    await ctx.send("That is not a valid color.")  # TODO: Translate
                    return
            a = next(iter_args, None)
        name = a
        zoom = next(iter_args, None)

        if faction:
            t = sql.template_get_by_name(faction['id'], name)
        else:
            t = sql.template_get_by_name(ctx.guild.id, name)

        if t:
            data = await http.get_template(t.url)
            max_zoom = int(math.sqrt(4000000 // (t.width * t.height)))
            try:
                zoom = max(1, min(int(zoom[1:]) if zoom and zoom.startswith("#") else 1, max_zoom))
            except ValueError:
                zoom = 1
            await render.gridify(ctx, data, color, zoom)
            return
        att = await utils.verify_attachment(ctx)
        if att:
            data = io.BytesIO()
            await att.save(data)
            zoom = args[0] if len(args) >= 1 else "#1"
            max_zoom = int(math.sqrt(4000000 // (att.width * att.height)))
            try:
                zoom = max(1, min(int(zoom[1:]) if zoom and zoom.startswith("#") else 1, max_zoom))
            except ValueError:
                zoom = 1
            await render.gridify(ctx, data, color, zoom)

    # ======================
    #       DITHERCHART
    # ======================

    @commands.group(name="ditherchart", invoke_without_command=True)
    async def ditherchart(self, ctx):
        await ctx.invoke_default("ditherchart")

    @ditherchart.command(name="pixelcanvas", aliases=["pc"])
    async def ditherchart_pixelcanvas(self, ctx):
        await ctx.send(file=discord.File("assets/dither_chart_pixelcanvas.png", "dither_chart_pixelcanvas.png"))

    @ditherchart.command(name="pixelzio", aliases=["pzi"])
    async def ditherchart_pixelzio(self, ctx):
        await ctx.send(file=discord.File("assets/dither_chart_pixelzio.png", "dither_chart_pixelzio.png"))

    @ditherchart.command(name="pixelzone", aliases=["pz"])
    async def ditherchart_pixelzone(self, ctx):
        await ctx.send(file=discord.File("assets/dither_chart_pixelzone.png", "dither_chart_pixelzone.png"))

    @ditherchart.command(name="pxlsspace", aliases=["ps"])
    async def ditherchart_pxlsspace(self, ctx):
        await ctx.send(file=discord.File("assets/dither_chart_pxlsspace.png", "dither_chart_pxlsspace.png"))

    # ======================
    #         REPEAT
    # ======================

    @commands.cooldown(1, 5, BucketType.guild)
    @commands.command(name="repeat", aliases=["r"])
    async def repeat(self, ctx):
        async for msg in ctx.history(limit=50, before=ctx.message):
            new_ctx = await self.bot.get_context(msg, cls=GlimContext)
            new_ctx.is_repeat = True

            match = re.match('^{}(diff|d|preview|p)'.format(sql.guild_get_prefix_by_id(ctx.guild.id)), msg.content)
            if match:
                await self.bot.invoke(new_ctx)
                return

            if await utils.autoscan(new_ctx):
                return
        await ctx.send(ctx.get("canvas.repeat_not_found"))

    # ======================

    @staticmethod
    async def parse_diff(ctx, raw_arg):
        m = re.search('(-?\d+)(?:,| |, )(-?\d+)(?: #?(\d+))?', raw_arg)
        if not m:
            await ctx.send(ctx.get("canvas.invalid_input"))
            return
        att = await utils.verify_attachment(ctx)
        if att:
            x = int(m.group(1))
            y = int(m.group(2))
            data = io.BytesIO()
            await att.save(data)
            max_zoom = int(math.sqrt(4000000 // (att.width * att.height)))
            zoom = max(1, min(int(m.group(3)) if m.group(3) else 1, max_zoom))
            return ctx, x, y, data, zoom

    @staticmethod
    async def parse_preview(ctx, coords):
        m = re.search('(-?\d+)(?:,|&y=) ?(-?\d+)(?:(?:,|&scale=)(\d+))?/?\s?#?(-?\d+)?', coords)
        if m is not None:
            x = int(m.group(1))
            y = int(m.group(2))
            if m.group(4):
                zoom = int(m.group(4))
            elif m.group(3):
                zoom = int(m.group(3))
            else:
                zoom = 1
            zoom = max(min(zoom, 16), -8)
            return ctx, x, y, zoom

    @staticmethod
    async def parse_quantize(ctx, canvas, args):
        if len(args) < 1:
            return
        if args[0] == "-f":
            if len(args) < 3:
                return
            f = sql.guild_get_by_faction_name_or_alias(args[1])
            if not f:
                await ctx.send("That faction could not be found.")  # TODO: Translate
                return
            name = args[2]
            t = sql.template_get_by_name(f['id'], name)
        else:
            name = args[0]
            t = sql.template_get_by_name(ctx.guild.id, name)
        if t:
            if t.canvas == canvas:
                raise errors.IdempotentActionError
            return await http.get_template(t.url)
        att = await utils.verify_attachment(ctx)
        if att:
            data = io.BytesIO()
            await att.save(data)
            return data


def setup(bot):
    bot.add_cog(Canvas(bot))
