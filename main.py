import discord
import requests
import json
import os
import random
from replit import db
from keep_alive import keep_alive
from discord.utils import get
from discord.ext import commands



client = commands.Bot(command_prefix='!')
idchannel = "913811102796759104"





@client.command(name='December')
async def December(context):

  myEmbed = discord.Embed(title="December Help", description="list of commands:", color=0x00ff00)
  myEmbed.add_field(name="!codeword:", value="enter a codeword to unlock secrets...", inline=False)
  myEmbed.add_field(name="!coinflip:", value="flip a coin to help make a decision", inline=False)
  myEmbed.add_field(name='!inspire:', value="send yourself an inspirational quote", inline=False)
  myEmbed.add_field(name="!ping:", value="display Ping and confirm the bot is working", inline=False)
  myEmbed.add_field(name="!rng:", value="random number generator. Enter the command followed by a space and your maximum number.", inline=False)
  
  myEmbed.set_footer(text="December v2.1.2 released 24th May 2021")

  await context.message.channel.send(embed=myEmbed)

@client.command(name='december')
async def december(ctx):
  await ctx.send('I think you meant to capitalize that...')

#PING
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!! {round(client.latency * 1000)}ms')








@client.command(name="pict")
@commands.has_role('Admin')
async def pict(ctx):
  await ctx.send(file=discord.File('hello.png'))



@client.command()
async def rankup(ctx):
    embed=discord.Embed(title="Get a rank", url="https://XboxBot.the-bestbest12.repl.co", description="To get a rank click this link", color=0xFF5733)
    await ctx.send(embed=embed)

  
@client.command()
async def welcome(ctx):
  member =  ctx.message.author
  await member.send('Hello! Üdvözöllek az Xbox közzöségen! Érezd jól magad! Jó játékot! Xbox bot')
  await member.send(file=discord.File('hello.png'))



@client.command(pass_context=True)
async def sf(ctx):
  memberk = ctx.message.author
  role = 'Test'
  try:
    await memberk.add_roles(discord.utils.get(memberk.guild.roles, name=role)) #add the role
  except Exception as e:
    await ctx.send('There was an error running this command ' + str(e)) #if error
  else:    await ctx.send("""👏�Mostantól Test rangot kapott:@{}""".format(memberk)) 


def addrole(id):
  role = 'Admin'
  try:
    await id.add_roles(discord.utils.get(id.guild.roles, name=role))
    id.send("Mostantól Xbox+ vagy!")
 




 




       





@client.event
async def on_member_join(member):
   await client.get_channel(idchannel).send(f"Üdvözlünk {member.name} az Xbox szerveren!")

@client.event
async def on_member_remove(member):
   await client.get_channel(idchannel).send(f"{member.name} elhagyta a szervert!")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status, activity=discord.Game('Már várja !December'))
  print('We have logged in as {0.user}'.format(client))

keep_alive()
client.run(os.getenv('TOKEN'))
