import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "ODQ2Njg2MTEyNzYzMDg0ODEw.GmMfxW.ojc4HHL1MrnhI4h8jUq1FgfQBoe40skdfcQhnI" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(TOKEN)
