import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")

async def main():
    # Load extension đúng cách (phải await)
    await bot.load_extension("daily")

    # Dán token của bạn ở đây
    TOKEN = "MTM5NDAyNjgxMjc5OTA2MjA3Ng.G5-uXD.4eq7D090EBfflDhmatRoPbqe5qpKsBpM9fwKpM"
    await bot.start(TOKEN)

# Chạy bot đúng cách với asyncio
asyncio.run(main())
