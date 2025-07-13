import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")

async def main():
    # Load extensions
    await bot.load_extension("cogs.addmoney")
    await bot.load_extension("cogs.bank") 
    await bot.load_extension("cogs.bj")
    await bot.load_extension("cogs.cash")
    await bot.load_extension("cogs.claim")
    await bot.load_extension("cogs.coinflip")
    await bot.load_extension("cogs.give")
    await bot.load_extension("cogs.daily")
    await bot.load_extension("cogs.hhelp")
    await bot.load_extension("cogs.hlevel")
    await bot.load_extension("cogs.hpage")
    await bot.load_extension("cogs.inventory")
    await bot.load_extension("cogs.profile")
    await bot.load_extension("cogs.shop")
    await bot.load_extension("cogs.top")
    await bot.load_extension("cogs.vatpham")
    await bot.load_extension("cogs.xoso")

    # Load the token securely from an environment variable
    TOKEN = os.getenv("MTM5NDAyNjgxMjc5OTA2MjA3Ng.GLIgBD.5uxEXZoK7FAEgCkYkygR3rJyS397Gdh5qgcUGM")
    if not TOKEN:
        print("❌ Token not found!")
        return
    await bot.start(TOKEN)

# Run the bot with asyncio
asyncio.run(main())
