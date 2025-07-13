import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

async def main():
    # Load extensions correctly (must await)
    await bot.load_extension("addmoney")
    await bot.load_extension("hlevel")
    await bot.load_extension("b")
    await bot.load_extension("claim")
    await bot.load_extension("coinflip")
    await bot.load_extension("daily")
    await bot.load_extension("inventory")
    await bot.load_extension("shop")
    await bot.load_extension("profile")
    await bot.load_extension("top")
    await bot.load_extension("xoxo")

    # Add your token here
    bot.run('MTM5NDAyNjgxMjc5OTA2MjA3Ng.GP1YYJ.sUzQLlLaoydWlPl1lvTWsjQuA2AxgCEQCpZwXg')

# Run the bot using asyncio
asyncio.run(main())
