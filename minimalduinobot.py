import discord
from discord.ext.commands import Bot
import serial
import time

TOKEN = 'insert bot token here'
serialcomm = serial.Serial('insert serial port here',9600) #serial port of microcontroller you use, example COM5
#serialcomm.timeout=1
intents = discord.Intents().all()
bot = Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("bot is ready to serve you")

@bot.command()
async def hi(ctx):
    await ctx.send("Oh, Hi there.")

@bot.command()
async def gf(ctx):
    aa = ctx.message.content.replace('!gf ','').lower()
    serialcomm.write(aa.encode())
    await ctx.send("LED set to " + aa)
    print(aa)


bot.run(TOKEN)