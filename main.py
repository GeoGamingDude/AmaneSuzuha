import discord
import os
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="s!", intents=discord.Intents.all())
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
  print("Bot is ready.")

async def load():
  for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
  await load()
  keep_alive()
  try:
    await bot.start(my_secret)
  except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("kill 1")
    os.system("python restarter.py")

asyncio.run(main())