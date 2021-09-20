# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:25:44 2021

@author: Swansy
"""
import os
import discord
import asyncio
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from dotenv import load_dotenv

schowekpath= os.getcwd() + "\schowek\\"
path = os.getcwd()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
siva = commands.Bot(command_prefix='-', intents=intents)


@siva.event
async def on_ready():
    global voice_channel_list
    print('Connected to: ' + str(GUILD))
    voice_channel_list = []
    for guild in siva.guilds:
        for channel in guild.voice_channels:
            voice_channel_list.append(channel)
    print('Kanały Voice na Serverze To:')
    for i in range(len(voice_channel_list)):
        print(str(i) + ' | ' + str(voice_channel_list[i]))
        print('----------------')

@siva.command('pobierz')
async def wyslij(ctx, text):
    await ctx.channel.send(file=discord.File(schowekpath + text))
    await asyncio.sleep(20)
    await ctx.channel.purge(limit=2)

@siva.command('send')
async def pobieranie(ctx):
    await ctx.channel.send("Podaj plik do wysłania:")
    msg = await siva.wait_for('message')
    for attachment in msg.attachments:
        await attachment.save(schowekpath+attachment.filename)
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)

@siva.command('schowek')
async def pokaz_schowek(ctx):
    plik = "```\n"
    for r, dirs, f in os.walk(schowekpath):
        for file in f:
            plik += file + "\n"
    plik += "```"
    await ctx.channel.send(plik)
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)

@siva.command('come')
async def join(ctx):
    if ctx.author.voice != None:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.channel.purge(limit=1)
    else:
        mes = await ctx.send('A może wbij na kanał co?')
        await asyncio.sleep(4)
        await mes.delete()


@siva.command('out')
async def leave(ctx):
    if ctx.voice_client != None:
        await ctx.channel.purge(limit=1)
        await ctx.voice_client.disconnect()
    else:
        await ctx.channel.purge(limit=1)
        return


@siva.command('wejdz')
async def wchodzenie(ctx, text):
    if ctx.voice_client:
        await ctx.channel.purge(limit=1)
        return
    else:
        await ctx.channel.purge(limit=1)
        await voice_channel_list[int(text)].connect()


@siva.command('powiedz')
async def gadanie(ctx, text):
    await ctx.send(text, tts=True)
    await ctx.channel.purge(limit=2)


@siva.command('listakanałówV')
async def wlistV(ctx):
    await ctx.channel.purge(limit=1)
    print(ctx.channel.id)
    wiad = ''
    for i in range(len(voice_channel_list)):
        wiad += str(i) + ' | ' + str(voice_channel_list[i]) + '\n' + '----------------' + '\n'
    msg = await ctx.send(wiad)
    await asyncio.sleep(10)
    await msg.delete()

async def czyruch():
    timer = 0
    while(True):
        with open(path + "\\ruch.txt", "r") as ruch:
            ruszasie = ruch.read()
        if int(ruszasie) == 1 and timer == 0:
            channel = siva.get_channel(803953800879669258)
            await channel.send('Ruszyło sie')
        timer += 1
        if timer == 10:
            timer = 0

        await asyncio.sleep(1)

siva.loop.create_task(czyruch())
siva.run(TOKEN)