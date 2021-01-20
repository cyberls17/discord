import discord
import os
from discord.ext import commands

#Discord Bot Setting
game = discord.Game("!명령어")
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),status=discord.Status.online,activity=game)

#Bot Start
@bot.event
async def on_ready():
    print("Bot ID: " + bot.user.name)
    print('Connection was successful')

@bot.command()
async def 명령어(ctx):
    await ctx.send("현재 존재하는 명령어는 info, ping, hello 입니다.")
    await ctx.send("Beta: info, 인사말")

@bot.command()
async def info(ctx):
    """Discord Bot info"""
    embed=discord.Embed(title= f"Information", description=f"디스코드 봇에 대한 정보입니다.", color=0xf3bb76)
    embed.add_field(name=f"Name", value="{}".format(bot.user.name), inline=False)
    latency = ctx.bot.latency
    latency = latency * 1000
    latency = round(latency)
    embed.add_field(name=f"Ping", value="{}ms".format(latency), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello {}~".format(bot.user.name))

@bot.command()
async def ping(ctx):
    """Ping! Pong!"""
    latency = ctx.bot.latency
    latency = latency * 1000
    latency = round(latency)
    await ctx.send("{}ms".format(latency))

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

token = os.environ["token"]
bot.run(token)

# sibal