# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:59:07 2022

@author: tfluan0606
"""


import discord
import tweepy
from tweepy.asynchronous import AsyncStream
from discord.ext import commands
import os
import asyncio


consumer_key= 'twiiterAPI consumer_key'
consumer_secret= 'twiiterAPI consumer_secret'
access_token= 'twiiterAPI access_token'
access_token_secret= 'twiiterAPI access_token_secret'


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$",intents=intents)

class MyStreamListener(AsyncStream):

    async def on_status(self, status):
        print('pass on_status')
        image = status.extended_entities['media']
        image_url = image[0]['media_url_https']
        print(image_url)
        asyncio.run_coroutine_threadsafe(post_tweet(image_url), bot.loop)
        



@bot.event
async def on_ready():
    stream = MyStreamListener(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(follow=['your twitter account ID'])
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
# placeholder command
async def hello(ctx):
    print('pass on hello')
    await ctx.send('Hello!')
    
@bot.event
async def post_tweet(image_url):
    print('pass on post_tweet')
    # here goes your channel id
    channel = bot.get_channel(discord channel id where you want to send)
    await channel.send(image_url)

bot.run('discord bot token')



