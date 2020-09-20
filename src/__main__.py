# 3rd-party
import discord
from discord.ext import commands
# Local
import filepaths
import gamedata

bot = commands.Bot(command_prefix="!")
bot.games = {}


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Alice is Missing"))


@bot.before_invoke
async def before_invoke(ctx):
    ctx.game = bot.games.setdefault(ctx.guild.id, gamedata.Data(ctx.guild))
    ctx.text_channels = {
        channel.name: channel
        for channel in ctx.guild.text_channels
    }

# Load all extensions
EXTENSIONS = ["admin", "debug", "game", "players"]
for extension in EXTENSIONS:
    bot.load_extension(extension)

# Import bot token
with open(filepaths.WHITE_RABBIT_DIR / "token.txt") as token_file:
    token = token_file.read()
bot.run(token)
