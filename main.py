import discord
import os
import asyncpraw
import random
from discord.embeds import Embed
from discord.flags import Intents
from discord.player import FFmpegOpusAudio, FFmpegPCMAudio
import redditend
import asyncio
from discord.ext import commands
from pytube import YouTube

from ytquery import searchyoutube
from subprocess import call
from ytp import getAudio
from website import keep_alive

intent = discord.Intents.default()
intent.message_content = True
FFMPEG_OPTIONS = "'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'"
bot = commands.Bot(command_prefix="!", intents=intent)


@bot.command()
async def get_back_to_work(ctx):
  await ctx.send("Ok my lord")


@bot.event
async def on_ready():
  print("ready!")


@bot.command()
async def meme(ctx):
  post = redditend.getMemes()
  if post.over_18:
    pass
  else:

    embed = Embed(title=post.title)
    embed.set_image(url=post.url)
    await ctx.send(embed=embed)


@bot.command()
async def kırbaç(ctx, arg):
  if arg == "1":
    await ctx.send("ah")
  elif arg == "2":
    await ctx.send("ahhh")
  elif arg == "3":
    await ctx.send("heelp mee help")
  else:
    pass


@bot.command()
async def pause(ctx):
  if bot.voice_clients[0].is_paused():
    await ctx.send("Already Paused")
  else:
    bot.voice_clients[0].pause()


@bot.command()
async def stop(ctx):
  await bot.voice_clients[0].disconnect(force=False)


@bot.command()
async def contin(ctx):

  if bot.voice_clients[0].is_playing():
    await ctx.send("Already Playing!")
  else:
    bot.voice_clients[0].resume()


@bot.command()
async def youtube(ctx, searchquery: str):

  vc = ctx.author.voice.channel
  voiceurl = searchyoutube(query=searchquery)
  voice = getAudio(voiceurl)
  newurl = voice.title.replace(" ", "") + ".mp4"
  newvoice = voice.streams.get_highest_resolution()
  out_file =newvoice.download(filename=newurl)
  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)

  vsource = FFmpegOpusAudio(voice.title.replace(" ", "") + ".mp3")
  vclient = await vc.connect()
  vclient.play(vsource)
  
  await ctx.send("Now Playing: " + voice.title)


keep_alive()
bot.run(os.environ['BOT_TOKEN'])
