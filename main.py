import discord
from discord.ext import commands

# Tùy chỉnh intents
intents = discord.Intents.default()
intents.message_content = True  # Bắt buộc để đọc tin nhắn người dùng

# Khởi tạo bot với prefix ?
bot = commands.Bot(command_prefix='?', intents=intents)

# Khi bot đăng nhập thành công
@bot.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập với tên: {bot.user}')
from keep_alive import keep_alive
keep_alive()
  
# Load lệnh coinflip
@bot.event
async def setup_hook():
    await bot.load_extension("coinflip")
    await bot.load_extension("daily")
    await bot.load_extension("bank")
    await bot.load_extension("top")
    await bot.load_extension("profile")
    await bot.load_extension("cash")
    await bot.load_extension("give")
    await bot.load_extension("shop")
    await bot.load_extension("vatpham")
    await bot.load_extension("inventory")
    await bot.load_extension("equip")
    await bot.load_extension("hpage")
    await bot.load_extension("hlevel")
    await bot.load_extension("hhelp")
    await bot.load_extension("addmoney")
    await bot.load_extension("bj")
    await bot.load_extension("xoso")
    












# Nhớ thay token ở đây bằng token bot của bạn
TOKEN = "MTM5MzkyOTY2Mzk5ODQ1OTkzNA.GVBYSw.gppNMG9qYRYsLleCWqKj4EPqz1PFql-0GHGMlA"

# Chạy bot
bot.run(TOKEN)
