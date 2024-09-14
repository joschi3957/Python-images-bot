import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

from images import *

TOKEN = 'token'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='f!', intents=intents, description='j4n0sch_gaming', help_command=None)


@client.event
async def on_ready():
    activity_type = discord.ActivityType.listening
    activity_name = 'J4n0sch_gaming'
    await client.change_presence(activity=discord.Activity(type=activity_type, name=activity_name))

    print('I am ready for the use')
    print(' ')


# On message function
# ----------------------------------------------------------------------------------------------------------------------
@client.event
async def on_message(message):
    await client.process_commands(message)
    user_message = str(message.content)

    if message.author == client.user:
        return

    if user_message.lower() == 'monke':
        await message.channel.send('https://tenor.com/view/overwatch-echo-winston-echo-echo-ow-meme-gif<W-17200162')

    if user_message.lower() == 'godo':
        await message.channel.send(f'{message.author.mention} sta godendo', file=discord.File(fes_godo),
                                   reference=message)
    if user_message.lower() == 'not funny':
        await message.channel.send(file=discord.File(mei_not_funny), reference=message)

    if user_message.lower() == 'milord gay':
        await message.channel.send('_yessir_')


# Test command
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
async def test(ctx):
    await ctx.send(ctx.message.content)
    print(ctx.message.content)


# Show his or the tagged member's pfp
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
async def pfp(ctx):
    try:
        user = ctx.message.mentions[0]
    except:
        user = ctx.author
    if not user:
        return
    pfp = user.avatar_url
    embed = discord.Embed(title=f'{user}profile pictures', description=user, color=0xe91e63)
    embed.set_image(url=(pfp))
    await ctx.channel.send(embed=embed)


# Show a list of all commands
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
async def commands(ctx):
    commands = '**f!pfp** [member tag]\n Show the pfp of the member tagged\n\n' \
               '**f!test** \n Command used for testing the bot\n\n' \
               '_coming soon_'
    embed = discord.Embed(title='You can find the commands here', description=commands, color=110011)
    await ctx.channel.send(embed=embed)


# Help command
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
async def help(ctx):
    help = '**Prefix:** f!\n' \
           '**Commands:** f!commands\n' \
           '_coming soon_'
    embed = discord.Embed(title='Hi bruh, how can i help you?', description=help, color=110011)
    await ctx.channel.send(embed=embed)


# Kick/Ban commands
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, memeber: discord.Member, *, reason=None):
    await memeber.kick(reason=reason)
    await ctx.send(f'{memeber} has been kicked')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick people")


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, memeber: discord.Member, *, reason=None):
    await memeber.ban(reason=reason)
    await ctx.send(f'{memeber} has been banned')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban people")


# Punching people
# ----------------------------------------------------------------------------------------------------------------------
@client.command()
async def punch(ctx):
    try:
        user = ctx.message.mentions[0].id
        author = ctx.author.id
    except:
        await ctx.send('Are you punching yourself?')
    if not user:
        return
    await ctx.channel.send(f'<@{author}> punched <@{user}>', file=discord.File(markiplier_punch))


# ----------------------------------------------------------------------------------------------------------------------

client.run(TOKEN)