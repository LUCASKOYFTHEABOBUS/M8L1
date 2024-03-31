
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send(f'Привет! Я {bot.user} чем я могу помоч вы можеть задать впорос как здесь что такойа глобальном потеплении, причинах и последствиях глобального потепления, Что провоцирует глобальное потепление, Как мы можем сдерживать глобальное потепление,  Насколько эта проблема серьезна, и касается ли она нас, и все я зню что много но разберотес удаче!')

@bot.command()
async def hi(ctx):
    await ctx.send(f'')

bot.run("MTIyMzk5MDMxMTcxMDIzMjY1Nw.GG3F4b.EJftB_0b5rfQcy09SVnWSARvs3P7fDzjjvaGx8")