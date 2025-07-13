import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")
from keep_alive import keep_alive
keep_alive()

async def main():
    # Load extension đúng cách (phải await)
    await bot.load_extension('cogs."addmoney')
    await bot.load_extension('cogs."bank') 
    await bot.load_extension('cogs."bj')
    await bot.load_extension('cogs."cash')
    await bot.load_extension('cogs."claim')
    await bot.load_extension('cogs."coinflip')
    await bot.load_extension('cogs."give')
    await bot.load_extension('cogs."daily')
    await bot.load_extension('cogs."hhelp')
    await bot.load_extension('cogs."hlevel')
    await bot.load_extension('cogs."hpage')
    await bot.load_extension('cogs."inventory')
    await bot.load_extension('cogs."profile')
    await bot.load_extension('cogs."shop')
    await bot.load_extension('cogs."top')
    await bot.load_extension('cogs."vatpham')
    await bot.load_extension('cogs."xoso')











    # Dán token của bạn ở đây
    TOKEN = "MTM5NDAyNjgxMjc5OTA2MjA3Ng.G5Ju1W.SAuAd8Y-gL7pBNCzssUCI7MPYS79OS6hC1cEsc"
    await bot.start(TOKEN)

# Chạy bot đúng cách với asyncio
asyncio.run(main())
