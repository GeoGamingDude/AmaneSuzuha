import discord
import os
import praw
import random
from discord import app_commands
from discord.ext import commands

redditClientID = os.environ['RedditClientID']
redditClientSecret = os.environ['RedditClientSecret']
redditUsername = os.environ['RedditUsername']
redditPassword = os.environ['RedditPassword']

class SteinsGate(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="worldline", description="Gets a Steins;Gate meme.")
  async def SGMeme(self, ctx):
    reddit = praw.Reddit(
    client_id = redditClientID,
    client_secret = redditClientSecret,
    username = redditUsername,
    password = redditPassword,
    user_agent = "Manuel is gay"
    )

    subreddit = reddit.subreddit("SteinsGateMemes")
    redditPosts = []

    top = subreddit.top(limit = 50)
    for submission in top:
      redditPosts.append(submission)
    randomPost = random.choice(redditPosts)
    name = randomPost.title
    url = randomPost.url

    memeEmbed = discord.Embed(title=name)
    memeEmbed.set_image(url=url)
    await ctx.channel.send(embed=memeEmbed)

async def setup(bot):
  await bot.add_cog(SteinsGate(bot))