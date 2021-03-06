STRINGS = {
    # Global messages
    "bot.added_by": "Added By",
    "bot.alert_channel": "Alert Channel",
    "bot.alias": "Alias",
    "bot.aliases": "Aliases",
    "bot.cancel": "Cancel",
    "bot.canvas": "Canvas",
    "bot.canvases": "Canvases",
    "bot.coordinates": "Coordinates",
    "bot.date_added": "Date Added",
    "bot.date_modified": "Date Modified",
    "bot.dimensions": "Dimensions",
    "bot.errors": "Errors",
    "bot.examples": "Examples",
    "bot.faction": "Faction",
    "bot.name": "Name",
    "bot.no": "No",
    "bot.or": "{0} or {1}",
    "bot.or_all_caps": "OR",
    "bot.page": "Page",
    "bot.percent": "Percent",
    "bot.public": "Public",
    "bot.size": "Size",
    "bot.subcommands": "Subcommands",
    "bot.timeout": "Menu timed out.",
    "bot.total": "Total",
    "bot.update": "I have updated to version **{0}**! Here's the changelog:",
    "bot.update_no_changelog": "I have updated to version **{0}**! Visit https://github.com/DiamondIceNS/StarlightGlimmer/releases for the full changelog.",
    "bot.usage": "Usage",
    "bot.visibility": "Visibility",
    "bot.yes": "Yes",
    "bot.menu_deleted": "Menu not found, was the message deleted?",
    "bot.reaction_scroll": "Scroll using the reactions below to see other pages.",
    "bot.menu_page": "Page {0} of {1}",
    "bot.pixel": "[{x},{y}]({url}) is {current} should be {target}.",
    "bot.time_label": "Time in UTC",
    "bot.not_enough_data": "Not enough data found.",

    # Error messages
    "error.account_deleted": "[[Account deleted]]",
    "error.bad_image": "An error occurred while attempting to open an image. Ensure that the supplied image is not corrupted.",
    "error.bad_png": "This image seems to be corrupted. Try re-saving it with an image editor or using `{0}quantize`.",
    "error.cannot_fetch_template": "Could not access URL for template '{0}'. (Was the original attachment deleted?)",
    "error.command_not_found": "The command {0} could not be found.",
    "error.cooldown": "That command is on cooldown. Try again in {0:.01f}s.",
    "error.did_you_mean": "Did you mean: {0}?",
    "error.faction_not_found": "That faction could not be found.",
    "error.http": "There was an error retrieving data from a remote location. Try again later.",
    "error.http_canvas": "{0} seems to be having connection issues. Try again later.",
    "error.invalid_color": "That is not a valid color.",
    "error.invalid_option": "That is not a valid option. Please try again.",
    "error.jpeg": "Seriously? A JPEG? Gross! Please create a PNG template instead.",
    "error.max_concurrency": "That command has reached maximum concurrency. Try again later.",
    "error.missing_arg_faction": "Missing argument: The `-f` flag must be followed by a faction name or alias.",
    "error.missing_argument": "You are missing a required argument. Please try again.",
    "error.no_attachment": "That command requires an attachment.",
    "error.no_dm": "That command only works in guilds.",
    "error.no_self_permission": "I do not have the permission to do that in this channel.",
    "error.no_templates": "This guild currently has no templates.",
    "error.no_templates_for_canvas": "This guild currently has no templates for that canvas.",
    "error.no_user_permission": "You do not have permission to use that command.",
    "error.non_discord_url": "I can only accept Discord attachment URLs.",
    "error.not_png": "That command requires a PNG image.",
    "error.template_not_found": "The template {0} could not be found.",
    "error.timed_out": "Command timed out.",
    "error.unknown": "An unknown error occurred. The dev has been notified. The unique code for this command was: `{0}`",
    "error.why": "But... why?",
    "error.canvas_not_supported": "Templates of that canvas are not supported for this command.",
    "error.invalid_duration_1": "Invalid duration, format like `1h8m`",
    "error.invalid_duration_2": "Invalid duration, duplicate time suffix (eg: 1**h**8m3**h**)",
    "error.connection": "Error with discord connection. Please try again.",

    # Alerts command messages
    "alerts.alert_description": "Messages that are crossed out have been fixed.",
    "alerts.alert_title": "{0} took damage!",
    "alerts.allies": "Allies",
    "alerts.already_muted": "`{0}` has no alert channel/is already muted",
    "alerts.comparision_title": "Comparision of allied vs enemy pixels placed per hour on {0} in the past {1} day(s).",
    "alerts.comparision_y_label": "Pixels placed",
    "alerts.enemies": "Enemies",
    "alerts.gain_title": "Pixels gained or lost per hour on {0} in the past {1} day(s).",
    "alerts.gain_y_label": "Pixels gained or lost",
    "alerts.muted": "`{0}` muted for {1:.2f} hours.",
    "alerts.no_recent_errors": "No recent errors found.",
    "alerts.no_stats": "No alert statistics found for that template",
    "alerts.not_muted": "`{0}` is not currently muted.",
    "alerts.received": "Received:",
    "alerts.unmuted": "Unmuted `{0}`.",
    "alerts.will_alert": "`{0}` will now alert in the channel {1} when damaged.",
    "alerts.will_not_alert": "`{0}` will no longer alert for damage.",

    # Animotes command messages
    "animotes.opt_in": "You have successfully **opted-in** to emoji conversion.",
    "animotes.opt_out": "You have successfully **opted-out** of emoji conversion.",

    # Canvas command messages
    "canvas.calculating": "Calculating...",
    "canvas.diff": "{0}/{1} | {2} errors | {3} complete",
    "canvas.diff_bad_color": "{0}/{1} | {2} errors | {bad} bad color | {3} complete",
    "canvas.diff_bad_color_list": "{0} pixels of bad color #{1:02x}{2:02x}{3:02x}",
    "canvas.diff_bad_color_title": "Bad Colors:",
    "canvas.diff_error_title": "Errors",
    "canvas.diff_fixed": "All fixed!",
    "canvas.diff_timeout": "Message timed out.",
    "canvas.dither": "`Image dithered in {0:.2f} seconds with {1} dithering. {2}`",
    "canvas.dither_invalid": "Invalid input: Please specify what kind of dither to use.",
    "canvas.dither_invalid_to": "Invalid threshold or order value.",
    "canvas.dither_notpngorjpg": "Only pngs or jpgs can be dithered.",
    "canvas.dither_order_and_threshold_option": "Threshold: {0}/4 Order: {1}",
    "canvas.dither_order_option": "Order: {0}",
    "canvas.dither_toolarge": "Image is too big, under {0},{0} only please.",
    "canvas.err.preview_no_args": "Invalid input: No template or coordinates provided to preview.",
    "canvas.fetching_data": "Fetching data from {0}...",
    "canvas.invalid_input": "Invalid input: does not match any template name or supported coordinates format.",
    "canvas.large_template": "(Processing large template, this might take a few seconds...)",
    "canvas.online": "There are {0} players online on {1}.",
    "canvas.online_await": "Waiting for next player count update...",
    "canvas.quantize": "Fixed {0} pixels.",
    "canvas.repeat_not_found": "Could not find a valid command to repeat, do I have the **Read Message History** permission?",
    "canvas.template_report_header": "Template Report",
    "canvas.pie_color_title": "Pie chart of the most popular colors on {0} from `{1}` to `{2}`",
    "canvas.hexbin_title": "Hexbin plot of the density of pixels placed on {0} from `{1}` to `{2}`",
    "canvas.hexbin_colorbar_count": "Pixels placed",
    "canvas.hexbin_colorbar_log": "Pixels placed - log10(count)",
    "canvas.hexbin_xlabel": "X Coordinate",
    "canvas.hexbin_ylabel": "Y Coordinate",
    "canvas.csv_placement": "CSV file of placement data from `{0}` to `{1}` for canvas {2}.",
    "canvas.csv_online": "CSV file of online data from `{0}` to `{1}` for canvas {2}.",
    "canvas.online_line_title": "Users online on {0} from `{1}` to `{2}`",
    "canvas.online_line_ylabel": "Online users",
    "canvas.online_line_mean": "Mean: {:.2f}",
    "canvas.radius_toolarge": "Radius value cannot be greater than {0}.",
    "canvas.hist2d_title": "2d histogram of the density of pixels placed on {0} from `{1}` to `{1}`",

    # Configuration command messages
    "configuration.alert_channel_cleared": "Alert channel has been cleared.",
    "configuration.alert_channel_current": "Alert channel is currently set to {0}.",
    "configuration.alert_channel_none": "No alert channel has been set.",
    "configuration.alert_channel_set": "Alert channel has been set to {0}.",
    "configuration.autoscan_disabled": "Autoscan has been disabled.",
    "configuration.autoscan_enabled": "Autoscan has been enabled.",
    "configuration.canvas_check_1": "This guild's default canvas is `{0}`.",
    "configuration.canvas_check_2": "To change the default canvas, run this command again with a supported canvas. (Use `{0}help canvas` to see a list.)",
    "configuration.canvas_set": "Default canvas has been set to `{0}`.",
    "configuration.language_check_1": "This guild's current language is `{0}`.",
    "configuration.language_check_2": "To set a new language, run this command again with one of the following options:",
    "configuration.language_set": "Language has been set to `English (US)`.",
    "configuration.prefix_current": "This guild's current prefix is `{0}`.",
    "configuration.prefix_set": "Prefix for this guild has been set to `{0}`.",
    "configuration.role_bot_admin_check": "Bot admin privileges are currently assigned to `@{0}`.",
    "configuration.role_bot_admin_cleared": "Bot admin privileges successfully cleared.",
    "configuration.role_bot_admin_not_set": "Bot admin privileges have not been assigned to a role.",
    "configuration.role_bot_admin_set": "Bot admin privileges assigned to role `@{0}`.",
    "configuration.role_list_botadmin": "Can do anything an Administrator can do",
    "configuration.role_list_footer": "Use '{0}role <type>' to view the current linked role.",
    "configuration.role_list_header": "Roles List",
    "configuration.role_list_templateadder": "Can add templates, and remove templates they added themself",
    "configuration.role_list_templateadmin": "Can add and remove any template",
    "configuration.role_not_found": "That role could not be found.",
    "configuration.role_template_adder_check": "Template adder privileges are currently assigned to `@{0}`.",
    "configuration.role_template_adder_cleared": "Template adder privileges successfully cleared.",
    "configuration.role_template_adder_not_set": "Template adder privileges have not been assigned to a role.",
    "configuration.role_template_adder_set": "Template adder privileges assigned to role `@{0}`.",
    "configuration.role_template_admin_check": "Template admin privileges are currently assigned to `@{0}`.",
    "configuration.role_template_admin_cleared": "Template admin privileges successfully cleared.",
    "configuration.role_template_admin_not_set": "Template admin privileges have not been assigned to a role.",
    "configuration.role_template_admin_set": "Template admin privileges assigned to role `@{0}`.",

    # Faction command messages
    "faction.alias_already_exists": "A faction with that alias already exists.",
    "faction.already_faction": "This guild is already a faction.",
    "faction.assembled": "Faction `{}` assembled.",
    "faction.clear_alias": "Faction alias cleared.",
    "faction.clear_color": "Faction color cleared.",
    "faction.clear_description": "Faction description cleared.",
    "faction.clear_emblem": "Faction emblem cleared.",
    "faction.clear_hide": "Unhid faction `{}`.",
    "faction.clear_invite": "Faction invite cleared. NOTE: Invite link is still active and must be removed manually.",
    "faction.disbanded": "Faction successfully disbanded.",
    "faction.err.alias_length": "Faction aliases must be between 1 and 5 characters.",
    "faction.err.description_length": "Faction descriptions must be at most 240 characters.",
    "faction.err.invalid_invite": "That is not a valid invite.",
    "faction.err.invite_not_this_guild": "You must use an invite to this guild.",
    "faction.err.name_length": "Faction names must be between 6 and 32 characters.",
    "faction.faction_list_footer_1": "Use '{0}faction <page>' to see that page",
    "faction.faction_list_footer_2": "Use '{0}faction info <name>' to see more info on a faction",
    "faction.list_header": "Faction List",
    "faction.must_be_a_faction": "This guild needs to become a faction to use that command.",
    "faction.name_already_exists": "A faction with that name already exists.",
    "faction.no_alias": "This faction does not have an alias.",
    "faction.no_description": "This faction does not have a description.",
    "faction.no_emblem": "This faction does not have an emblem.",
    "faction.no_factions": "There doesn't seem to be any guilds yet...",
    "faction.no_invite": "This faction has not set a public invite.",
    "faction.not_a_faction_yet": "This guild has not created a faction yet.",
    "faction.set_alias": "Faction alias set to `{}`.",
    "faction.set_color": "Faction color set.",
    "faction.set_description": "Faction description set.",
    "faction.set_emblem": "Faction emblem set.",
    "faction.set_hide": "Hid faction `{}`.",
    "faction.set_invite": "Faction invite set.",
    "faction.set_name": "Faction renamed to `{}`.",

    # General command messages
    "general.err.cannot_get_changelog": "There was an error fetching the changelog. Visit https://github.com/BrickGrass/StarlightGlimmer/releases to see all releases.",
    "general.help_arguments": "Optional Arguments",
    "general.help_command_list_header": "Command List",
    "general.help_command_not_found": "The command `{0}` could not be found.",
    "general.help_footer": "Use {}help <command> to view more info about a specific command. For more in depth documentation, click the title's link.",
    "general.help_more_info": "More Info",
    "general.help_no_subcommand_named": "The command `{0}` has no subcommand named `{1}`. Did you mean {2}?",
    "general.help_no_subcommands": "The command `{0}` has no subcommands.",
    "general.help_subcommand": "# Use '{}help {} (subcommand)' to view more info about a subcommand",
    "general.ping": "Pinging...",
    "general.pong": "Pong! | **{0}ms**",
    "general.suggest": "Your suggestion has been sent. Thank you for your input!",
    "general.version": "My version number is **{0}**",
    "general.wiki": "https://github.com/BrickGrass/StarlightGlimmer/wiki/",

    # Template command messages
    "template.added": "Template '{0}' added!",
    "template.duplicate_list_close": "Create a new template anyway?",
    "template.duplicate_list_open": "The following templates already match this image:",
    "template.err.hyphen": "Template names cannot begin with hyphens.",
    "template.err.invalid_coords": "Coordinates must be numbers!",
    "template.err.max_templates": "This guild already has the maximum number of templates. Please remove a template before adding another.",
    "template.err.name_exists": "A template with that name already exists. Please choose a different name.",
    "template.err.name_not_found": "Could not find template with name `{0}`.",
    "template.err.name_too_long": "That name is too long. Please use a name under {0} characters.",
    "template.err.no_image": "An image is required to add a template.",
    "template.err.no_public_templates": "There are currently no public templates.",
    "template.err.not_owner": "You do not have permission to modify that template.",
    "template.err.number": "Template names cannot be numbers.",
    "template.err.template_gen_error": "There was an error building the template.",
    "template.err.update_file": "Updating file failed",
    "template.err.update_invalid_url": "Updating image failed, invalid url, it must be a discord attachment.",
    "template.err.update_no_attachment": "Updating image failed, no attachments could be detected.",
    "template.err.url_access": "{0}: Could not access URL for template.",
    "template.link_to_canvas": "Link to canvas",
    "template.list_all_footer_1": "Use '{0}template all <page>' to see that page",
    "template.list_all_footer_2": "Use '{0}template info -f <faction> <name>' to see more info on a template",
    "template.list_footer_1": "Use '{0}template <page>' to see that page or scroll using the reactions below",
    "template.list_footer_2": "Use '{0}template info <name>' to see more info on a template",
    "template.list_header": "Template List",
    "template.menu_entry": "[{0}, {1}]({2}) | [Link to file]({3})",
    "template.menuclose": "Menu exited!",
    "template.name_exists_ask_replace": "A template with the name '{0}' already exists for {1} at ({2}, {3}).",
    "template.not_quantized": "This image contains colors that are not part of this canvas's palette. Would you like to quantize it?",
    "template.remove": "Successfully removed '{0}'.",
    "template.replace": "Replace it?",
    "template.update_header_1": "Template updated!",
    "template.update_header_2": "Summary of changes",
    "template.updated": "Template '{0}' updated!",

    # Command brief help
    "brief.alert": "Set or clear a templates alert channel.",
    "brief.alertchannel": "Set or clear the channel used for receiving bot update alerts from my github page.",
    "brief.alertchannel.clear": "Clears the alert channel.",
    "brief.alertchannel.set": "Sets the alert channel.",
    "brief.alerts-stats": "Shows statistics about a template I monitor.",
    "brief.assemble": "Assemble this guild into a faction.",
    "brief.autoscan": "Toggles automatic preview and diff.",
    "brief.canvas": "Sets the default canvas website for this guild.",
    "brief.canvas.pixelcanvas": "Sets the default canvas to Pixelcanvas.io.",
    "brief.canvas.pixelzone": "Sets the default canvas to Pixelzone.io.",
    "brief.canvas.pxlsspace": "Sets the default canvas to Pxls.space.",
    "brief.changelog": "Gets a link to my releases page.",
    "brief.check": "Check the completion status of all templates.",
    "brief.diff": "Checks completion status of a template on a canvas.",
    "brief.diff.pixelcanvas": "Creates a diff using Pixelcanvas.io.",
    "brief.diff.pixelzone": "Creates a diff using Pixelzone.io.",
    "brief.diff.pxlsspace": "Creates a diff using Pxls.space.",
    "brief.disband": "Disband this guild's faction.",
    "brief.dither": "Dither a png or jpg image.",
    "brief.dither.geo32": "Dithers an image using the geo32 palette",
    "brief.dither.pixelcanvas": "Dithers an image using the pixelcanvas palette",
    "brief.ditherchart": "Gets a chart of canvas colors dithered together.",
    "brief.ditherchart.pixelcanvas": "Gets a dither chart of Pixelcanvas.io colors.",
    "brief.ditherchart.pixelzone": "Gets a dither chart of Pixelzone.io colors.",
    "brief.ditherchart.pxlsspace": "Gets a dither chart of Pxls.space colors.",
    "brief.faction": "Manages this guild's faction.",
    "brief.faction.alias": "View or modify the alias of this guild's faction.",
    "brief.faction.alias.clear": "Clear the alias of this guild's faction.",
    "brief.faction.alias.set": "Set the alias of this guild's faction.",
    "brief.faction.color": "View or modify the color.",
    "brief.faction.color.clear": "Clear the color.",
    "brief.faction.color.set": "Set the color.",
    "brief.faction.desc": "View or modify the description.",
    "brief.faction.desc.clear": "Clear the description.",
    "brief.faction.desc.set": "Set the description.",
    "brief.faction.emblem": "View or modify the emblem image.",
    "brief.faction.emblem.clear": "Clear the emblem image.",
    "brief.faction.emblem.set": "Set the emblem image.",
    "brief.faction.invite": "View or modify the invite link.",
    "brief.faction.invite.clear": "Clear the invite link.",
    "brief.faction.invite.set": "Set the invite link.",
    "brief.faction.name": "View or modify the name of this guild's faction.",
    "brief.faction.name.set": "Set the name of this guild's faction.",
    "brief.factioninfo": "Get info about a faction.",
    "brief.factionlist": "List all factions.",
    "brief.github": "Gets a link to my GitHub repository.",
    "brief.gridify": "Adds a grid to a template.",
    "brief.help": "Displays this message.",
    "brief.hide": "Toggle hiding a faction from public lists on and off.",
    "brief.info": "Get info about a faction.",
    "brief.invite": "Gets my invite link.",
    "brief.language": "Sets my language.",
    "brief.mute": "Mute or unmute a templates alerts.",
    "brief.online": "Shows how many players are currently online.",
    "brief.online.pixelcanvas": "Shows how many players are currently online on Pixelcanvas.io.",
    "brief.online.pixelzone": "Shows how many players are currently online on Pixelzone.io.",
    "brief.online.pxlsspace": "Shows how many players are currently online on Pxls.space.",
    "brief.ping": "Pong!",
    "brief.prefix": "Sets my command prefix for this guild.",
    "brief.preview": "Previews the canvas at a given coordinate or template.",
    "brief.preview.pixelcanvas": "Creates a preview using Pixelcanvas.io.",
    "brief.preview.pixelzone": "Creates a preview using Pixelzone.io.",
    "brief.preview.pxlsspace": "Creates a preview using Pxls.space.",
    "brief.quantize": "Rough converts an image to the palette of a canvas.",
    "brief.quantize.pixelcanvas": "Quantizes colors using the palette of Pixelcanvas.io.",
    "brief.quantize.pixelzone": "Quantizes colors using the palette of Pixelzone.io.",
    "brief.quantize.pxlsspace": "Quantizes colors using the palette of Pxls.space.",
    "brief.quickstart": "Gives a guided tour to the bot.",
    "brief.recent": "Lists recent error pixels from templates with alerting on.",
    "brief.register": "Opt-in to animated emoji replacement.",
    "brief.repeat": "Repeats the last used canvas command.",
    "brief.role": "Assign bot privileges to a role.",
    "brief.role.botadmin": "Configure Bot Admin privileges.",
    "brief.role.botadmin.clear": "Clear the role assigned to Bot Admin.",
    "brief.role.botadmin.set": "Set the role assigned to Bot Admin.",
    "brief.role.templateadder": "Configure Template Adder privileges.",
    "brief.role.templateadder.clear": "Clear the role assigned to Template Adder.",
    "brief.role.templateadder.set": "Set the role assigned to Template Adder.",
    "brief.role.templateadmin": "Configure Template Admin privileges.",
    "brief.role.templateadmin.clear": "Clear the role assigned to Template Admin.",
    "brief.role.templateadmin.set": "Set the role assigned to Template Admin.",
    "brief.suggest": "Sends a suggestion to the developer.",
    "brief.template": "Manages templates.",
    "brief.template.add": "Adds a template.",
    "brief.template.add.pixelcanvas": "Adds a template for Pixelcanvas.io.",
    "brief.template.add.pixelzone": "Adds a template for Pixelzone.io.",
    "brief.template.add.pxlsspace": "Adds a template for Pxls.space.",
    "brief.template.all": "List all templates for all factions.",
    "brief.template.info": "Displays info about a template.",
    "brief.template.remove": "Removes a template.",
    "brief.snapshot": "Manages snapshots.",
    "brief.snapshot.add": "Add snapshots.",
    "brief.snapshot.list": "List snapshots.",
    "brief.snapshot.remove": "Remove snapshots.",
    "brief.template.update": "Updates a template.",
    "brief.unregister": "Opt-out of animated emoji replacement.",
    "brief.version": "Gets my version number.",
    "brief.canvas-stats": "Shows statistics about a canvas I monitor",
    "brief.canvas-stats.pixelcanvas": "Shows statistics about Pixelcanvas.io",
    "brief.canvas-stats.pixelzone": "Shows statistics about Pixelzone.io",
    "brief.canvas-stats.pxlsspace": "Shows statistics about Pxls.space",

    # Command long help
    "help.alert": "With an alert channel set, I will monitor your template constantly and alert for damage in that channel.",
    "help.alertchannel.set": "Use the #channel mention syntax with this command to ensure the correct channel is set.",
    "help.alert-stats": """
        When template alerts are enabled (see `{p}alert`) I will begin to gather statistics about pixels placed on it.
        You can retrieve graphs displaying that data with this command. No data older than a week old is kept.

        Graph types:
        `comparision` - The comparision graph displays the total number of pixels placed each hour by allies or enemies. Allies being pixels that are correct to the template, enemies being pixels that are damaging to the template. Anywhere on the template that is transparent will be ignored.
        `gain` - The gain graph displays the overall gain or loss in progress on a template in each hour recorded. So if 2 pixels were placed by your allies, and 4 by your enemies, the overall gain for that hour would be -2.
    """,
    "help.assemble": "Faction names and aliases must be unique. Names must be between 6 and 32 characters, case sensitive. Aliases must be between 1 and 5 characters, case insensitive.",
    "help.autoscan": """
        If enabled, I will watch all messages for coordinates and automatically create previews and diffs according to these rules:
        - Any message with coordinates in the form "@0, 0" will trigger a preview for the default canvas (see `{p}help canvas`)
        - Any message with a link to a supported canvas will trigger a preview for that canvas.
        - Any message with coordinates in the form "0, 0" with a PNG attached will trigger a diff for the default canvas.
        - Previews take precedence over diffs
        - Messages which use spoiler tags will be entirely ignored""",
    "help.canvas": "Defaults to Pixelcanvas.io.",
    "help.diff": """
        Images must be in PNG format.
        Error pixels will be marked in red. Pixels that do not match the canvas palette ('bad color') will be marked in blue (see `{p}help quantize`).
        You cannot zoom an image to contain more than 4 million pixels.""",
    "help.dither": """
        Images must be in PNG or JPEG format.
        The image will be converted to the palette you select using the dithering algorithm specified.
        Please be aware that the algorthims other than Bayer dithering can be quite slow, you may need to wait a while.
        The dimension limits on each algorithm are as follows:
        Bayer dithering: 1500px by 1500px
        Yliluoma dithering: 100px by 100px
        Floyd Steinberg dithering: 100px by 100px

        `-d` or `--ditherType` - This argument determines the type of dithering that will happen, the default is bayer.
            options: b, bayer, y, yliluoma, fs, floyd-steinberg
        `-t` or `--threshold` - Change the threshold setting. (Note: only bayer dithering uses this option)
            options: 2, 4, 8, 16, 32, 64, 128, 256, 512
        `-o` or `--order` - Change the order setting.
            options: 2, 4, 8, 16""",
    "help.faction.alias.set": "Faction aliases must be unique. Min 1 char, max 32 chars. Case insensitive.",
    "help.faction.color.set": "Color must be a valid hexidecimal number. Default 0xCF6EE4.",
    "help.faction.create": """
        Factions must have unique names (6 to 32 chars, case sensitive) and, if at all, unique aliases (1 to 5 chars, case insensitive).
        A guild can only have one faction at any given time.""",
    "help.faction.desc.set": "Max 240 characters.",
    "help.faction.emblem.set": "URLs must be Discord URLs.",
    "help.faction.hide": "You can still view info about hidden factions if you explicitly use their name or alias in commands with the `-f` paramater.",
    "help.faction.name.set": "Faction names must be unique. Min 6 chars, max 32 chars. Case sensitive.",
    "help.mute": """
        Duration can either be given in hours.
        eg:
        `7` - 7 hours
        `5.5` - 5 hours 30 minutes

        Or you can give the duration using one of these 5 suffixes. w - Week, d - Day, h - Hour, m - Minute, s - Second.
        eg:
        `2h` - 2 hours
        `7h2M4s` - 7 hours, 2 minutes, 4 seconds
        `1s5d2M` - 5 days, 2 minutes, 1 second
    """,
    "help.prefix": "Max length is 5 characters. You really shouldn't need more than 2.",
    "help.quantize": """
        This should primarily be used if `{p}diff` is telling you your image has 'bad color' in it.
        Using this command to create templates from raw images is not suggested, use the {p}dither command instead.""",
    "help.register": """
        Opting into this feature means that whenever you type :animated_emoji_name: I will delete
        your message and replace it with the emoji specified, as long as that emoji is in a server
        that I can see.

        You only need to register once for this to apply to all guilds.
        This feature requires that I have the Manage Messages permission.""",
    "help.repeat": "This command only applies to 'preview', 'diff', and their autoscan invocations. Only the last 50 messages will be searched.",
    "help.role.botadmin": "If a user has a role with this privilege bound to it, that user can use any of my commands with no restrictions. They will have the same permissions as guild Administrators.",
    "help.role.templateadder": "If this privilege is bound to a role, all regular members will lose the ability to modify templates unless they have that role.",
    "help.role.templateadmin": "If a user has a role with this privilege bound to it, that user can add and remove any template using the 'templates' command, regardless of ownership.",
    "help.template": "You can scroll through the pages of the templates listed using the reactions underneath, this times out and stops responding after 5 minutes.",
    "help.template.add": """
        Image must be in PNG format. If the image is not quantized to the target canvas's palette, I will offer to quantize it for you.
        A guild can have up to 25 templates at any time.
        Templates must have unique names (max 32 chars, case sensitive). If you attempt to add a new template with the same name as an existing one, it will be replaced if you have permission to remove the old one (see `{p}help remove`).
        I only store URLs to templates. If the message that originally uploaded a template is deleted, its URL will break and the template will be lost. Save backups to your computer just in case.""",
    "help.template.remove": "This command can only be used if the template being removed was added by you, unless you are a Template Admin, Bot Admin, or have the Administrator permission (see 'role').",
    "help.snapshot": """
        Attempts to update all currently registered snapshot templates. If a snapshot has errors, it will not be updated.
        This command can only be used by Template Admins and those with Admin perms. If you wish to only attempt to update specific templates you can specify them by listing their base template names.""",
    "help.snapshot.add": "Base is what you want the template to look like, snapshot is what it looks like currently.",
    "help.update": "Update an existing template. The only required argument is <name> which is the name of the template you wish to update. All other arguments are optional and can be used in any order as long as <name> is before all of them.",
    "help.unregister": "You only need to unregister once for this to apply to all guilds.",
    "help.canvas-stats": """
        This command can either display various graphs using the statistics I gather, or it can output the raw data to csv.
        I keep data no longer than a week, so if you want to plot data over a greater timespan, you will have to manually request csv's periodically and piece together the data yourself.
        To see the default value for any optional argument, or the full list of choices available, use the `--help` argument.

        Also: The `--center` + `--radius` arguments only apply for the hexbin/2dhist plot types, all other plots and also the raw option use the entire area of the canvas.
    """,

    "args.canvas-stats": """
        `-t` or `--type` - Selects the kind of graph to plot. NOTE: Not compatible with the `--raw` argument.
            options: hexbin, color-pie, online-line, 2dhist
        `-r` or `--raw` - Dumps the kind of data you specify for a canvas from my database to csv. NOTE: Not compatible with the `--type` argument.
            options: placement, online
        `-d` or `--duration` - The duration of time counting backwards from the current moment to fetch or plot. Given in `1d2h` type format, where 5 suffixes are available. w - Week, d - Day, h - Hour, m - Minute, s - Second.
        `-c` or `--center` - Where to center the data (if area restriction applies).
        `-a` or `--radius` - The Radius (in pixels) of the data (if area restriction applies).
        `--nooverlay` - Disable the canvas preview overlay on plots that use it.
        `--bins` - Select the binning strategy for plots that use it. The 2dhist's binning strategy is not currently controllable.
            options: log, count
        `--mean` - Toggle on a mean line for a line plot.
    """,
    "args.canvas-stats2": """
        `--colormap` - Select the colormap for plots that use it.
            options: see `{p}canvas-stats --help`
    """,
    "args.alert-stats": """
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.
        `-d` or `--duration` - The duration of time counting backwards from the current moment to plot. Given in `1d2h` type format, where 5 suffixes are available. w - Week, d - Day, h - Hour, m - Minute, s - Second.
        `-t` or `--type` - Selects the type of graph to display. Default is comparision.
            options: comparision, gain
    """,
    "args.check": """
        `-e` or `--onlyErrors` - This argument filters the results and only shows templates with errors.
        `-f` or `--faction` - Searches for the faction name provided and tries to check it's templates.
        `-s` or `--sort` - Select how the results are sorted, default is by template name, a-z.
            options: name_az, name_za, errors_az, errors_za, percent_az, percent_za""",
    "args.diff": """
        `-e` or `--errors` - Sends the specific coordinates of 10 error pixels. I then monitor these pixels for 5 minutes and remove any from the list that are fixed.
        `-s` or `--snapshot` - Sends a snapshot of a template. All correct pixels will be the colour they are on your template and all other pixels will be transparent.
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.
        `-z` or `--zoom` - Zooms in the diff by the factor you provide.
        The following args filter `-e`. Colors are represented by a number from 0-palleteLength.
        `-t` or `--excludeTarget` - If not used, pixels are filtered based on what color they are damaged to, if used, they are filtered based on what they should be.
        `-oc` or `--onlyColors` - Only target pixels of the colors you list here will be shown.
        `-ec` or `--excludeColors` - Pixels target pixels of the colors you list here will not be shown.""",
    "args.diff2": """
        `-c` or `--highlightCorrect` - Overlay errors with red, correct (and on template) pixels with green and leaves anything off template greyscale.
        `-cb` or `--colorBlind` - Switches the colours used in `-c` to be more color blind friendly, correct in blue incorrect in red.""",
    "args.gridify": """
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.
        `-c` or `--color` - Uses the hexadecimal color value you provide for the grid lines of the final image.
        `-z` or `--zoom` - Zooms in the image by the factor you provide. You cannot zoom an image to contain more than 4 million pixels.""",
    "args.preview": """
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.
        `-z` or `--zoom` - Zooms in the image by the factor you provide.""",
    "args.recent": """
        `-f` or `--faction` - Searches for the faction name that you provide and tries to list error pixels from there.
        `-p` or `--page` - Opens on the page number you provide, if it is a valid page.""",
    "args.template": """
        `-p` or `--page` - Opens on the page number you provide, if it is a valid page.
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.""",
    "args.template.info": """
        `-r` or `--raw` - Returns just the template image without extra info.
        `-z` or `--zoom` - Zooms in the image by the factor you provide. Only works when `-r` is enabled.
        `-f` or `--faction` - Searches for the faction name that you provide and tries to find the template you specify in that faction.""",
    "args.template_update": """
        `-n` or `--name` - Any text following this argument will be used to update the name of the template.
        `-x` - A number after this argument will be used to update the x coordinate.
        `-y` - A number after this argument will be used to update the y coordinate.
        `-i` or `--image` - This argument can be used without any input after it to tell the bot to check for image attachments or with a discord image url to use that to update the image.""",

    # Command signatures
    "signature.canvas-stats": "(subcommand) (-t) (-r) (-d) (-c) (-a) (--nooverlay) (--bins) (--mean) (--colormap)",
    "signature.alert": "<template_name> (alert_channel)",
    "signature.alertchannel": "(subcommand)",
    "signature.alertchannel.set": "<channel>",
    "signature.alert-stats": "<template_name> (-f|--faction) (-d|--days) (-t|--type)",
    "signature.assemble": "<name> (alias)",
    "signature.canvas": "(subcommand)",
    "signature.check": "(-e|--onlyErrors) (-f|--faction) (-s|--sort)",
    "signature.diff": "<template_name> (-e) (-s) (-f) (-z) (-c) (-cb) (-t) (-oc) (-ec)",
    "signature.diff.pixelcanvas": "<coordinates> (-e) (-s) (-z) (-c) (-cb)",
    "signature.diff.pixelzone": "<coordinates> (-e) (-s) (-z) (-c) (-cb)",
    "signature.diff.pxlsspace": "<coordinates> (-e) (-s) (-z) (-c) (-cb)",
    "signature.dither": "(subcommand) (-d|--ditherType) (-t|--threshold) (-o|--order)",
    "signature.ditherchart": "(subcommand)",
    "signature.faction": "(subcommand)",
    "signature.faction.alias": "(subcommand)",
    "signature.faction.alias.set": "<alias>",
    "signature.faction.color": "(subcommand)",
    "signature.faction.color.set": "<color>",
    "signature.faction.desc": "(subcommand)",
    "signature.faction.desc.set": "<description>",
    "signature.faction.emblem": "(subcommand)",
    "signature.faction.emblem.set": "['', '<url>']",
    "signature.faction.name": "(subcommand)",
    "signature.faction.name.set": "<name>",
    "signature.factioninfo": "(faction)",
    "signature.gridify": ['(-f|--faction) (-c|--color) (-z|--zoom)', '<template> (-f|--faction) (-c|--color) (-z|--zoom)'],
    "signature.info": "<faction>",
    "signature.language": "(code)",
    "signature.mute": "<template_name> (duration)",
    "signature.online": "(subcommand)",
    "signature.prefix": "<prefix>",
    "signature.preview": ['(subcommand) <coordinates> (-t|--templateRegion) (-f|--faction) (-z|--zoom)', '<template_name> (-t|--templateRegion) (-f|--faction) (-z|--zoom)'],
    "signature.preview.pixelcanvas": "<coordinates> (-t|--templateRegion) (-f|--faction) (-z|--zoom)",
    "signature.preview.pixelzone": "<coordinates> (-t|--templateRegion) (-f|--faction) (-z|--zoom)",
    "signature.preview.pxlsspace": "<coordinates> (-t|--templateRegion) (-f|--faction) (-z|--zoom)",
    "signature.quantize": "(subcommand) (-f|--faction) (-z|--zoom)",
    "signature.quantize.pixelcanvas": ['(-f|--faction) (-z|--zoom)', '<template> (-f|--faction) (-z|--zoom)'],
    "signature.quantize.pixelzone": ['(-f|--faction) (-z|--zoom)', '<template> (-f|--faction) (-z|--zoom)'],
    "signature.quantize.pxlsspace": ['(-f|--faction) (-z|--zoom)', '<template> (-f|--faction) (-z|--zoom)'],
    "signature.recent": "(-f|--faction) (-p|--page)",
    "signature.role": "(role)",
    "signature.role.botadmin": "(subcommand)",
    "signature.role.botadmin.set": "<role>",
    "signature.role.templateadder": "(subcommand)",
    "signature.role.templateadder.set": "<role>",
    "signature.role.templateadmin": "(subcommand)",
    "signature.role.templateadmin.set": "<role>",
    "signature.suggest": "<suggestion>",
    "signature.template": "(subcommand) (-p|--page) (-f|--faction)",
    "signature.template.add": "(subcommand) <name> <x> <y> (url)",
    "signature.template.add.pixelcanvas": "<name> <x> <y> (url)",
    "signature.template.add.pixelzone": "<name> <x> <y> (url)",
    "signature.template.add.pxlsspace": "<name> <x> <y> (url)",
    "signature.template.info": "<template> (-r|--raw) (-f|--faction) (-z|--zoom)",
    "signature.template.remove": "<template>",
    "signature.snapshot": "(subcommand) (template_filtering)",
    "signature.snapshot.add": "<base_template_name> <snapshot_template_name>",
    "signature.snapshot.remove": "<base_template_name> <snapshot_template_name>",
    "signature.template.update": "<name> (-n|--name) (-x) (-y) (-i|--image)",

    # Examples
    "example.alertchannel":
        [("clear", "Clear the alert channel if there is one"),
         ("set #bot-spam", "Set the alert channel to a channel named 'bot-spam'")],
    "example.alertchannel.set": [("#bot-spam", "Set the alert channel to a channel named 'bot-spam'")],
    "example.alert-stats":
        [("my_template", "Fetches a comparision graph for the template named 'my_template' for the past day"),
         ("cool_flower_art --days 7 --type gain", "Fetches a gain graph for the template named 'cool_flower_art' for the past 7 days")],
    "example.assemble":
        [("CoolFaction", "Assembles your guild into a faction named 'CoolFaction'"),
         ("\"Cool Faction\" cf", "Assembles your guild into a faction named 'Cool Faction' with alias 'cf'")],
    "example.canvas":
        [("", "Show the currently set default canvas"),
         ("pc", "Set the default canvas to Pixelcanvas.io")],
    "example.check":
        [("", "Check the completion status of all of this guild's templates"),
         ("-e", "Check the completion status of all of this guild's templates and only show those that have errors"),
         ("-f factionName", "Check the completion status of all of the templates of 'factionName'"),
         ("-s errors_za", "Check the completion status of all templates and sort the results by number of errors in decending order")],
    "example.dither":
        [("", "(with an attachment) Dither an image using the default canvas palette, bayer dithering and the default threshold and order settings"),
         ("geo32 --ditherType y --order 4", "(with an attachment) Dither an image using the geo32 palette, yliluoma dithering and an order of 4"),
         ("-d bayer -t 512 -o 8", "(with an attachment) Dither an image using the default canvas palette, bayer dithering, a threshold of 512/4 and an order of 8")],
    "example.diff":
        [("pc 100 100", "(with an attachment) Check an image against Pixelcanvas.io at (100, 100)"),
         ("520 -94 -z 7", "(with an attachment) Check an image against the default canvas at (520, -94) and magnify the result 7 times"),
         ("-256 345 -e", "(with an attachment) Check an image against the default canvas at (-256, 345) and print a short list of specific error pixels"),
         ("100 22 -s", "(with an attachment) Check an image against the default canvas at (100, 22) and generate a snapshot, where correct pixels display as they are on the template, and the rest are transparent."),
         ("CoolTemplate -f CoolFaction", "Check a template named 'CoolTemplate' belonging to the faction 'CoolFaction'"),
         ("CoolTemplate -e -t -oc 0", "Check a template named 'CoolTemplate' and display a short list of errors, filtered to only show those that should be color index 0. (white on pc)"),
         ("CoolTemplate -c -cb", "Check a template named 'CoolTemplate' and display the resulting diff in color highlight and colorblind mode.")],
    "example.diff.pixelcanvas":
        [("100 100", "(with an attachment) Check an image against Pixelcanvas.io at (100, 100)"),
         ("100 100 -z 7", "(with an attachment) Check an image against Pixelcanvas.io at (100, 100) and magnify the result 7 times")],
    "example.diff.pixelzone":
        [("100 100", "(with an attachment) Check an image against Pixelzone.io at (100, 100)"),
         ("100 100 -z 7", "(with an attachment) Check an image against Pixelzone.io at (100, 100) and magnify the result 7 times")],
    "example.diff.pxlsspace":
        [("100 100", "(with an attachment) Check an image against Pxls.space at (100, 100)"),
         ("100 100 -z 7", "(with an attachment) Check an image against Pxls.space at (100, 100) and magnify the result 7 times")],
    "example.ditherchart": [("pc", "Get the ditherchart for Pixelcanvas.io")],
    "example.faction":
        [("name", "Print your faction's current name"),
         ("desc set Hello World!", "Sets your faction's description to 'Hello World!'"),
         ("alias clear", "Clears your faction's alias")],
    "example.faction.alias":
        [("", "Print your faction's current alias"),
         ("set abc", "Sets your faction's alias to 'abc'"),
         ("clear", "Clears your faction's alias")],
    "example.faction.color":
        [("", "Print your faction's current color"),
         ("set FFFFFF", "Sets your faction's color to 'FFFFFF'"),
         ("clear", "Resets your faction color to the default")],
    "example.faction.desc":
        [("", "Print your faction's current description"),
         ("set Hello World!", "Sets your faction's description to 'Hello World!'"),
         ("clear", "Clears your faction's description")],
    "example.faction.emblem":
        [("", "Print your faction's current emblem"),
         ("set https://cdn.discordapp.com/.../emblem.jpg", "Set your faction emblem to the image at the URL"),
         ("clear", "Clears your faction's emblem")],
    "example.faction.invite":
        [("", "Print your faction's current invite link"),
         ("set", "Automatically creates a new instant invite to this channel and sets it"),
         ("set aAbBcC", "Sets your faction's public invite link to an existing invite with the ID 'aAbBcC'"),
         ("set https://discord.gg/<id>", "Sets your faction's public invite link to an existing URL"),
         ("clear", "Clears your faction's invite link")],
    "example.faction.name":
        [("", "Print your faction's current name"),
         ("set \"My Cool New Faction\"", "Sets your faction's name to 'My Cool New Faction'")],
    "example.factioninfo":
        [("\"That Faction\"", "Gets info about a faction named 'That Faction'"),
         ("abc", "Gets info about a faction with the alias 'abc'")],
    "example.gridify":
        [("-z 8", "(with an attachment) Gridify an image magnified 8 times"),
         ("MyTemplate -z 16", "Gridify a template named 'MyTemplate' magnified 16 times"),
         ("MyTemplate -z 10 -c 080808", "Gridify a template named 'MyTemplate' magnified 10 times using hex 0x080808 as the grid color")],
    "example.language":
        [("", "View my current language and available language options"),
         ("en-us", "Set my language to English (US)")],
    "example.online": [("pc", "Gets the number of players currently online on Pixelcanvas.io")],
    "example.prefix":
        [("", "View my current prefix"),
         ("#", "Set my command prefix to '#'")],
    "example.preview":
        [("pc 900 900", "Preview Pixelcanvas.io centered on (900, 900)"),
         ("900 900 -z 7", "Preview the default canvas centered on (900, 900) magnified 7 times"),
         ("900 900 -z -7", "Preview the default canvas centered on (900, 900) zoomed out 7 times"),
         ("\"My Template\"", "Preview a template named 'My Template'"),
         ("\"Their Cool Template\" -t -f \"That Faction\" -z -2", "Create a default-size preview centered on a template named 'Their Cool Template' belonging to the faction 'That Faction', zoomed out 2 times")],
    "example.preview.pixelcanvas":
        [("900 900", "Preview Pixelcanvas.io centered on (900, 900)"),
         ("900 900 -z 7", "Preview Pixelcanvas.io centered on (900, 900) magnified 7 times"),
         ("900 900 -z -7", "Preview Pixelcanvas.io centered on (900, 900) zoomed out 7 times")],
    "example.preview.pixelzone":
        [("900 900", "Preview Pixelzone.io centered on (900, 900)"),
         ("900 900 -z 7", "Preview Pixelzone.io centered on (900, 900) magnified 7 times"),
         ("900 900 -z -7", "Preview Pixelzone.io centered on (900, 900) zoomed out 7 times")],
    "example.preview.pxlsspace":
        [("900 900", "Preview Pxls.space centered on (900, 900)"),
         ("900 900 -z 7", "Preview Pxls.space centered on (900, 900) magnified 7 times"),
         ("900 900 -z -7", "Preview Pxls.space centered on (900, 900) zoomed out 7 times")],
    "example.quantize":
        [("", "(with an attachment) Quantize an attachment to the palette of the default canvas"),
         ("pc", "(with an attachment) Quantize an attachment to the palette of Pixelcanvas.io"),
         ("pc MyTemplate", "Quantize a template named 'MyTemplate' to the palette of Pixelcanvas.io")],
    "example.quantize.pixelcanvas":
        [("", "(with an attachment) Quantize an attachment to the palette of Pixelcanvas.io"),
         ("MyTemplate", "Quantize a template named 'MyTemplate' to the palette of Pixelcanvas.io")],
    "example.quantize.pixelzone":
        [("", "(with an attachment) Quantize an attachment to the palette of Pixelzone.io"),
         ("MyTemplate", "Quantize a template named 'MyTemplate' to the palette of Pixelzone.io")],
    "example.quantize.pxlsspace":
        [("", "(with an attachment) Quantize an attachment to the palette of Pxls.space"),
         ("MyTemplate", "Quantize a template named 'MyTemplate' to the palette of Pxls.space")],
    "example.role":
        [("", "Show the available permissions"),
         ("botadmin", "Show the role tied to the botadmin permission"),
         ("botadmin set admin-role", "Set the botadmin permission to a role called 'admin-role'")],
    "example.role.botadmin":
        [("", "Show the role tied to the botadmin permission"),
         ("set admin-role", "Set the botadmin permission to a role called 'admin-role'"),
         ("clear", "Clear the botadmin permission")],
    "example.role.botadmin.set": [("admin-role", "Set the botadmin permission to a role called 'admin-role'")],
    "example.role.templateadder":
        [("", "Show the role tied to the templateadder permission"),
         ("set adder-role", "Set the templateadder permission to a role called 'adder-role'"),
         ("clear", "Clear the templateadder permission")],
    "example.role.templateadder.set": [("adder-role", "Set the templateadder permission to a role called 'adder-role'")],
    "example.role.templateadmin":
        [("", "Show the role tied to the templateadmin permission"),
         ("set t-admin-role", "Set the templateadmin permission to a role called 't-admin-role'"),
         ("clear", "Clear the templateadmin permission")],
    "example.role.templateadmin.set": [("t-admin-role", "Set the templateadmin permission to a role called 't-admin-role'")],
    "example.suggest": [("you're mom gay lol", "Send 'you're mom gay lol' to the dev as a suggestion")],
    "example.template":
        [("", "List all templates for this guild"),
         ("all", "List all public templates for all factions"),
         ("add pc MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for Pixelcanvas.io at (100, 100)"),
         ("-f OtherFaction", "List all public templates for a faction named 'OtherFaction'")],
    "example.template.add":
        [("MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for the default canvas at (100, 100)"),
         ("pc MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for Pixelcanvas.io at (100, 100)"),
         ("pc MyTemplate 100 100 https://cdn.discordapp.com/.../avatar.jpg", "Create a template named 'MyTemplate' for Pixelcanvas.io at (100, 100) using the image at the URL")],
    "example.template.add.pixelcanvas":
        [("MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for Pixelcanvas.io at (100, 100)"),
         ("MyTemplate 100 100 https://cdn.discordapp.com/.../avatar.jpg", "Create a template named 'MyTemplate' for Pixelcanvas.io at (100, 100) using the image at the URL")],
    "example.template.add.pixelzone":
        [("MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for Pixelzone.io at (100, 100)"),
         ("MyTemplate 100 100 https://cdn.discordapp.com/.../avatar.jpg", "Create a template named 'MyTemplate' for Pixelzone.io at (100, 100) using the image at the URL")],
    "example.template.add.pxlsspace":
        [("MyTemplate 100 100", "(with an attachment) Create a template named 'MyTemplate' for Pxls.space at (100, 100)"),
         ("MyTemplate 100 100 https://cdn.discordapp.com/.../avatar.jpg", "Create a template named 'MyTemplate' for Pxls.space at (100, 100) using the image at the URL")],
    "example.template.info":
        [("MyTemplate", "Get info on a template named 'MyTemplate'"),
         ("CoolTemplate -f CoolFaction", "Get info on a template named 'CoolTemplate' belonging to a faction named 'CoolFaction'"),
         ("RawTemplate -r -z 5", "Get just the image for template named 'RawTemplate' magnified 5 times"),
         ("CoolRawTemplate -r -f CoolFaction -z 4", "Get just the image for a template named 'CoolRawTemplate' belonging to a faction named 'CoolFaction' magnified 4 times")],
    "example.template.remove": [("MyTemplate", "Remove a template named 'MyTemplate'")],
    "example.snapshot":
        [("", "Try to update all snapshots in this guild."),
         ("cb mb", "Only try to update the snapshots 'cb' and 'mb'.")],
    "example.template.update": [
        ("coolTemplate -x 67 -y 88", "Update the template 'coolTemplate' with the coordinates (67, 88)"),
        ("funtemplate -n funnertemplate -i -x 8", "(with an attachment) Update the template 'funtemplate' with the new name 'funnertemplate' and the new x coordinate 8. The image of the template will be updated with the attached image."),
        ("MyTemplate -i https://cdn.discordapp.com/.../template.png -y 876", "Update the template 'MyTemplate' with the image linked and the y coordinate 876.")],
    "example.alert": [
        ("MyTemplate #alert-channel", "Set up the template 'MyTemplate' to alert for damage in the channel #alert-channel"),
        ("MyTemplate", "Clear any existing alert channels for the template 'MyTemplate', it will no longer alert for damage")],
    "example.mute": [
        ("MyTemplate 4", "Mute alerts for 'MyTemplate' for 4 hours"),
        ("MyTemplate 30m7s", "Mute alerts for 'MyTemplate' for 30 minutes and 7 seconds"),
        ("MyTemplate", "Unmute 'MyTemplate' immediately instead of waiting for the mute time to expire")],

    # Canvas colors
    "color.unknown": "Unknown",

    "color.pixelcanvas.0": "White",
    "color.pixelcanvas.1": "Light Grey",
    "color.pixelcanvas.2": "Dark Grey",
    "color.pixelcanvas.3": "Black",
    "color.pixelcanvas.4": "Pink",
    "color.pixelcanvas.5": "Red",
    "color.pixelcanvas.6": "Orange",
    "color.pixelcanvas.7": "Brown",
    "color.pixelcanvas.8": "Yellow",
    "color.pixelcanvas.9": "Light Green",
    "color.pixelcanvas.10": "Green",
    "color.pixelcanvas.11": "Cyan",
    "color.pixelcanvas.12": "Teal",
    "color.pixelcanvas.13": "Blue",
    "color.pixelcanvas.14": "Light Purple",
    "color.pixelcanvas.15": "Purple",

    "color.pixelzone.0": "Dark Grey",
    "color.pixelzone.1": "Black",
    "color.pixelzone.2": "Light Grey",
    "color.pixelzone.3": "White",
    "color.pixelzone.4": "Brown",
    "color.pixelzone.5": "Pink",
    "color.pixelzone.6": "Light Purple",
    "color.pixelzone.7": "Purple",
    "color.pixelzone.8": "Red",
    "color.pixelzone.9": "Orange",
    "color.pixelzone.10": "Yellow",
    "color.pixelzone.11": "Light Green",
    "color.pixelzone.12": "Green",
    "color.pixelzone.13": "Cyan",
    "color.pixelzone.14": "Teal",
    "color.pixelzone.15": "Blue",

    "color.pxlsspace.0": "White",
    "color.pxlsspace.1": "Lightest Grey",
    "color.pxlsspace.2": "Mid Light Grey",
    "color.pxlsspace.3": "Mid Dark Grey",
    "color.pxlsspace.4": "Darkest Grey",
    "color.pxlsspace.5": "Black",
    "color.pxlsspace.6": "Light Pink",
    "color.pxlsspace.7": "Dark Pink",
    "color.pxlsspace.8": "Light Red",
    "color.pxlsspace.9": "Dark Red",
    "color.pxlsspace.10": "Beige",
    "color.pxlsspace.11": "Tan",
    "color.pxlsspace.12": "Light Orange",
    "color.pxlsspace.13": "Dark Orange",
    "color.pxlsspace.14": "Light Brown",
    "color.pxlsspace.15": "Dark Brown",
    "color.pxlsspace.16": "Dark Yellow",
    "color.pxlsspace.17": "Light Yellow",
    "color.pxlsspace.18": "Light Green",
    "color.pxlsspace.19": "Green",
    "color.pxlsspace.20": "Dark Green",
    "color.pxlsspace.21": "Cyan",
    "color.pxlsspace.22": "Teal",
    "color.pxlsspace.23": "Blue",
    "color.pxlsspace.24": "Dark Blue",
    "color.pxlsspace.25": "Lavender",
    "color.pxlsspace.26": "Magenta",
    "color.pxlsspace.27": "Purple",

    # Quickstart tour text
    "tour.intro": "Welcome to my quickstart tour, say `cancel` at any time to exit. Hope you enjoy!",
    "tour.exit": "Thank you for taking my tour, exiting.",
    "tour.invalid": "Invalid, please type: `{0}`",
    "tour.request": "Please send `{0}`",
    "tour.image": "{0} and also attach this image: {1}",
    "tour.explain": "Explanation:",

    "tour.command.0": "{p}preview 0 0",
    "tour.explain.0": "The preview command renders an image of a canvas, centered at the coordinates you specify. So this is capturing an image from the default canvas for this guild, at (0,0).",

    "tour.command.1": "{p}preview {tl}",
    "tour.explain.1": "Preview can also render images using templates. I will create an image of the area of the canvas that the template you specify covers. I'll explain more about templates in a second.",

    "tour.command.2": "{p}preview {tl} --zoom 8",
    "tour.explain.2": "So far we have only used preview with it's non-optional arguments. Many of my commands also have optional keyword arguments which you can use to change the behaviour of the command. This argument, `-z <factor>` or `--zoom <factor>`, will zoom in the image by a factor you provide, here it is 8.",

    "tour.command.3": "{p}diff -109 -107",
    "tour.explain.3": "The diff command compares an image you provide it with against what is on canvas, and highlights any errors in red. When diffing, you need to provide the canvas coordinates for where you want the top leftmost corner of the image to lie.",

    "tour.command.4": "{p}diff {tl_e}",
    "tour.explain.4": "You can also diff using a template.",

    "tour.command.5": "{p}diff {tl_e} --zoom 8 --errors --highlightCorrect",
    "tour.explain.5": "Diff also has a lot of helpful optional arguments. Zoom works the same as it does on preview. `--errors` or `-e` will make the embed you can see above that lists the exact location of errors appear. `--highlightCorrect` or `-c` makes the different sections of the diff appear in different colors: green for correct, red for incorrect, greyscale for off-template, and blue for off-palette colors.",

    "tour.command.6": "{p}template",
    "tour.explain.6": "The template command lists all of the templates that a guild (discord server) has. Templates are just a way of storing an image and the canvas coordinates for it's top left corner under a name. They make it easier to diff, preview etc repeatedly, as you saw earlier.",

    "tour.command.7": "{p}template info {tl}",
    "tour.explain.7": "Template has a subcommand called info, which allows you to see information on a specific template."
}
