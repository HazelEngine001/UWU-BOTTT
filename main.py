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
    TOKEN = "MTM5MzkyOTY2Mzk5ODQ1OTkzNA.GvCQY8.SwYuhid9PTXqaKi3Jy6_xw7DIBcJZiaCP_GUNU"
    await bot.start(TOKEN)

# Chạy bot đúng cách với asyncio
asyncio.run(main())
