import os
import disnake
from disnake.ext import commands

# Читаем токен из переменной окружения Render
TOKEN = os.getenv("DISCORD_TOKEN")

# Создаём бота
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен и готов к работе!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Запуск
bot.run(TOKEN)
