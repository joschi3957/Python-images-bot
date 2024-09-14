import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

from images import *

TOKEN = 'enter youre token here'

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents, description='j4n0sch_gaming', help_command=None)


@client.event
async def on_ready():
    activity_type = discord.ActivityType.streaming
    activity_name = '!help'
    await client.change_presence(activity=discord.Activity(type=activity_type, name=activity_name))

    print('I am ready for the use')
    print(' ')



@client.event
async def on_message(message):
    await client.process_commands(message)
    user_message = str(message.content)

    if message.author == client.user:
        return

    if user_message.lower() == 'tokyo ghoul':
        await message.channel.send('https://i.pinimg.com/originals/07/25/65/07256543b7243633bd70f1b22237b8ba.gif')

    if user_message.lower() == 'godo':
        await message.channel.send(f'{message.author.mention} sta godendo', await message.channel.send('https://i.pinimg.com/originals/6a/a7/d4/6aa7d437075cf9ee449452f300f2894f.gif'),
                                   reference=message)
    if user_message.lower() == 'not funny':
        await message.channel.send('https://i.pinimg.com/originals/36/4e/a6/364ea6cd7bfd00a0260aaf6e2602cd4d.gif'),

    if user_message.lower() == 'Am i gay ?':
        await message.channel.send('https://i.pinimg.com/originals/da/19/eb/da19ebf0fe2336c362f7c23b20dd8661.gif')



@client.command()
async def test(ctx):
    await ctx.send(ctx.message.content)
    print(ctx.message.content)



@client.command()
async def pfp(ctx):
    try:
        user = ctx.message.mentions[0]
    except:
        user = ctx.author
    if not user:
        return
    pfp = user.avatar.url
    embed = discord.Embed(title=f'{user}profile pictures', description=user, color=0xe91e63)
    embed.set_image(url=(pfp))
    await ctx.channel.send(embed=embed)



@client.command()
async def commands(ctx):
    commands = '**!pfp** [member tag]\n Show the pfp of the member tagged\n\n' \
               '**!test** \n Command used for testing the bot\n\n' \
               '_coming soon_'
    embed = discord.Embed(title='You can find the commands here', description=commands, color=110011)
    await ctx.channel.send(embed=embed)



@client.command()
async def help(ctx):
    help = '**Prefix:** !\n' \
           '**Commands:** !commands\n' \
           '_coming soon_'
    embed = discord.Embed(title='Hi bruh, how can i help you?', description=help, color=110011)
    await ctx.channel.send(embed=embed)



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



@client.command()
async def punch(ctx):
    try:
        user = ctx.message.mentions[0].id
        author = ctx.author.id
    except:
        await ctx.send('Are you punching yourself?')
    if not user:
        return
    await ctx.channel.send(f'<@{author}> punched <@{user}>', await ctx.channel.send('https://i.pinimg.com/originals/48/d5/59/48d55975d1c4ec1aa74f4646962bb815.gif'))



client.run(TOKEN)
