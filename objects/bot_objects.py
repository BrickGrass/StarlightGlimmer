import uuid

import discord
from discord.ext import commands
from discord.utils import get as dget

from lang import en_US, pt_BR, tr_TR
from utils import canvases
from objects.database_models import session_scope, Guild


class GlimContext(commands.Context):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.is_repeat = False
        self.is_autoscan = False
        self.is_default = False
        self.is_template = False

        self.uuid = uuid.uuid4()

    langs = {
        'en-us': "English (US)",
        'pt-br': "Português (BR)",
        'tr-tr': "Türkçe (TR)",
    }

    @property
    def canvas(self):
        guild = self.session.query(Guild).get(self.guild.id)
        return guild.canvas

    @property
    def canvas_pretty(self):
        return canvases.pretty_print[self.canvas]

    @property
    def lang(self):
        return self.bot.get_guild_language(self.guild.id)

    @staticmethod
    def get_from_guild(bot, guild, str_id):
        string = None
        language = bot.get_guild_language(guild)

        if language == "pt-br":
            string = pt_BR.STRINGS.get(str_id, None)
        if language == "tr-tr":
            string = tr_TR.STRINGS.get(str_id, None)
        if language == "en-us":
            string = en_US.STRINGS.get(str_id, None)

        if string is None:
            return en_US.STRINGS.get(str_id, None)
        else:
            return string

    def s(self, str_id):
        language = self.lang
        string = None

        if language == "pt-br":
            string = pt_BR.STRINGS.get(str_id, None)
        if language == "tr-tr":
            string = tr_TR.STRINGS.get(str_id, None)
        if language == "en-us":
            string = en_US.STRINGS.get(str_id, None)

        if string is None:
            return en_US.STRINGS.get(str_id, None)
        else:
            return string

    async def invoke_default(self, cmd: str):
        default_canvas = self.canvas
        cmds = cmd.split('.')
        self.command = dget(self.bot.commands, name=cmds[0])
        self.view.index = 0
        self.view.preview = 0
        self.view.get_word()
        if len(cmds) > 1:
            for c in cmds[1:]:
                self.command = dget(self.command.commands, name=c)
                self.view.skip_ws()
                self.view.get_word()
        self.command = dget(self.command.commands, name=default_canvas)
        self.is_default = True
        if self.command is not None:
            await self.bot.invoke(self)
