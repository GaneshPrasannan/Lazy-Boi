import discord
from discord.colour import Color
from discord.ext import commands
import sys
import os



intents = discord.Intents.all()
client = commands.Bot(command_prefix=";", intents = intents)
client.remove_command('help')

commands_prefix = ';'


id = 776867805727031336

# Help
@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title="Help", description=f"Use {commands_prefix}help [command_name] for extended infomation on a command.", color=Color.blue())

  em.add_field(name="Moderation", value="`kick`, `ban`, `set_mute`, `mute`", inline=False)
  em.add_field(name="Roles", value="`create_role`, `remove_role`, `add_role`, `delete_role`", inline=False)
  em.add_field(name="Others", value="`create_channel`, `delete_channel`, `clear`, `change_servername`", inline=False)
  await ctx.send(embed=em)

# Dedicated Help Commands
@help.command()
async def kick(ctx):
  em = discord.Embed(title="kick", description='Kicks a member from the guild.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}kick <member> [reason]``")

  await ctx.send(embed = em)

@help.command()
async def ban(ctx):
  em = discord.Embed(title="Ban", description='Bans a member from the guild.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}ban <member> [reason]``")

  await ctx.send(embed = em)
  
@help.command()
async def create_channel(ctx):
  em = discord.Embed(title="Create Channel", description='Creates a channel, in a specific category.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}create_channel <channel_name> [category]``")

  await ctx.send(embed = em)
  
@help.command()
async def delete_channel(ctx):
  em = discord.Embed(title="Delete Channel", description='Deletes a specific channel from the guild.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}delete_channel <channel_name>``")

  await ctx.send(embed = em)
  
@help.command()
async def clear(ctx):
  em = discord.Embed(title="Clear", description='Clears a specific amount of number from the channel.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}clear <amount>``")

  await ctx.send(embed = em) 

@help.command()
async def add_role(ctx):
  em = discord.Embed(title="Add Role", description='Adds a role to a user.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}add_role <user> <role>``")
  await ctx.send(embed = em)

   
@help.command()
async def remove_role(ctx):
  em = discord.Embed(title="Remove Role", description='Removes a role from a user.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}remove_role <user> <role>``")

  await ctx.send(embed = em)
   
@help.command()
async def create_role(ctx):
  em = discord.Embed(title="Create Role", description='Creates a role in the guild.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}create_role <role_name>``")

  await ctx.send(embed = em)


@help.command()
async def delete_role(ctx):
  em = discord.Embed(title="Delete Role", description='Deletes a role from the guild.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}delete_role <role_name>``")

  await ctx.send(embed = em)


   
@help.command()
async def change_servername(ctx):
  em = discord.Embed(title="Change Server Name", description='Changes the server name.', color=Color.blue())
  em.add_field(name="**Syntax**", value=f"``{commands_prefix}change_servername <new_name>``")

  await ctx.send(embed = em)

# On ready
@client.event
async def on_ready():
    bot_channel = client.get_channel(929394664182808696)
    await bot_channel.purge()
    em = discord.Embed(title="Hi, I'm *Lazy Boi*", description="I have all the features which will make your life easier, type `;help` to get the list of all commands!, type `;set_prefix` to change the prefix! ", color=Color.blue())
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/929078645367111730/6facaaf2edb6997d9875ad432c07f813.png?size=1024")
    await bot_channel.send(embed=em)
    print("The bot has been started")


@client.command(name="version", aliases=["v"], help="Shows the version of the bot")
async def version(ctx):
    myEmbed = discord.Embed(
                title="Current Version",
                description="The bot is in Version 1.0",
                color=3447003
            )
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="8 Jan 2022", inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    await ctx.message.channel.send(embed=myEmbed)


# @client.event
# async def on_member_join(member):
#     memberJoin = discord.Embed(
#         title=f"{member} has joined the guild!", 
#         description=f"Welcome {member} to {member.guild.name}",
#         color=Color.blue()
#     )
#     memberJoin.set_image(url="https://c.tenor.com/LDuF2jVabwoAAAAC/banner-welcome.gif")
#     welcome_channel = client.get_channel(917754508984066091)
#     await welcome_channel.send(embed=memberJoin)
#     await member.send(f"Hi {member}! Welcome to {member.guild.name}!")
    
# @client.event
# async def on_member_remove(member):
#     memberLeave = discord.Embed(
#         title=f"{member} has left the server.", 
#         description=f"{member} has left the guild :cry:.",
#         color=Color.blue()
#     )
#     memberLeave.set_image(url="https://c.tenor.com/Z6Dpmoc6UnkAAAAC/bye-bye-bye.gif")
#     welcome_channel = client.get_channel(917754508984066091)
#     await welcome_channel.send(embed=memberLeave)
        



# Other commands
# Create channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def create_channel(ctx, channel_name=None, *, category_name=None):
    if category_name:
      name = category_name
      category = discord.utils.get(ctx.guild.categories, name=name)
      await ctx.guild.create_text_channel(channel_name, category=category)

    error = discord.Embed(title="Error", description="No channel name given.", color=Color.red())
    success = discord.Embed(title="Channel created successfuly!", description=f"Channel `{channel_name}` has been created successfuly", color=Color.green())
    if not channel_name:
      await ctx.channel.send(embed=error)
    guild = ctx.guild

    if not category_name:
      await guild.create_text_channel(channel_name)
    await ctx.channel.send(embed=success)

@client.command()
@commands.has_permissions(manage_channels=True)
async def delete_channel(ctx, channel_name):
    guild = ctx.message.guild
    # check if the channel exists
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
   
    # if the channel exists
    if existing_channel is not None:
        await existing_channel.delete()
        success = discord.Embed(title="Channel Removed successfuly!", description=f"Channel `{channel_name}` has been deleted successfuly", color=Color.green())
        await ctx.channel.send(embed=success)
    # if the channel does not exist, inform the user
    else:
        error = discord.Embed(title="Error", description=f'No channel named, `{channel_name}`, was found.', color=Color.red())
        await ctx.send(embed=error)

@client.command()
async def restart(ctx, aliases=['!', 'restart_bot']):
    if ctx.author.id == id:
      restartEmbed = discord.Embed(title="Restarting", description="The program is beginning it's restarting process", color=Color.blue())
      restartEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/929078645367111730/6facaaf2edb6997d9875ad432c07f813.png?size=1024")
      await ctx.send(embed = restartEmbed)
      os.execv(sys.executable, ['python'] + sys.argv)
    else:
      noPerms = discord.Embed(title="Permission Denied", description="  You do not have the required permissions.", color=Color.red())
      await ctx.send(embed = noPerms)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    if amount>0:
      await ctx.message.delete()
      await ctx.channel.purge(limit=amount)
    else:
      error = discord.Embed(title="Error", description="Amount cannot be less than 1, please give an amount of more than or equal to 1.", color=Color.red())

      await ctx.channel.send(embed=error)

@client.command()
@commands.has_permissions(administrator = True)
async def change_servername(ctx, *, server_name):
    oldServerName = ctx.guild.name

    success = discord.Embed(title="Server Name Changed successfuly!", description=f"Server Name has been changed from `{oldServerName}` to `{server_name}` successfuly.", color=Color.green())
    await ctx.guild.edit(name=server_name)
    await ctx.channel.send(embed=success)


# Kick a user
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,  *, reason = "No reason provided."):
  await member.kick(reason = reason)
  dmEmbed = discord.Embed(title=":boot: Kicked", description=f"**{ctx.guild.name}**: You have been kicked by {ctx.message.author}\n**Reason: **{reason}", color=Color.blue())

  guildEmbed = discord.Embed(title=":boot: Kicked", description=f"**{member}** has been kicked by {ctx.message.author}\n**Reason: **{reason}", color=Color.blue())
  try:
    await member.send(embed=dmEmbed)
  except:
    print("Dms closed")
  await ctx.channel.send(embed=guildEmbed)


# Ban a user
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "No reason provided."):
  await member.ban(reason = reason)
  dmEmbed = discord.Embed(title=":hammer: Banned", description=f"**{ctx.guild.name}**: You have been Banned by {ctx.message.author}\n**Reason: **{reason}", color=Color.blue())

  guildEmbed = discord.Embed(title=":hammer: Banned", description=f"**{member}** has been Banned by {ctx.message.author}\n**Reason: **{reason}", color=Color.blue())
  try:
    await member.send(embed=dmEmbed)
  except:
    print("Dms closed")
  await ctx.channel.send(embed=guildEmbed)

@client.command()
@commands.has_permissions(administrator=True) #permissions
async def add_role(ctx, user : discord.Member, role : discord.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
      errorAbove = discord.Embed(title="Permissions Denied",description="That role is above your top role!", color=Color.red())
      ctx.channel.send(embed=errorAbove)

  elif role in user.roles:
      hasAlready = discord.Embed(title="Role already added", description=f"{user} already has the given role!", color=Color.blue())
      await ctx.channel.send(embed=hasAlready)

  else:
      success = discord.Embed(title="Successfuly Added Role", description=f"{role} role has been successfuly added to {user}", color=Color.green())
      await user.add_roles(role) #adds role if not already has it
      await ctx.channel.send(embed=success) 

@client.command()
async def check(ctx):
  em = discord.Embed(title="Online", description=f"Hi, {ctx.message.author}", color=Color.green())
  await ctx.channel.send(embed=em)

@client.command()
@commands.has_permissions(administrator=True) #permissions
async def remove_role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
      errorAbove = discord.Embed(title="Permissions Denied",description="That role is above your top role!", color=Color.red())
      ctx.channel.send(embed=errorAbove)

  elif role not in user.roles:
      hasAlready = discord.Embed(title="Error", description=f"{user} doesnt have {role} role.", color=Color.blue())
      await ctx.channel.send(embed=hasAlready)

  else:
      success = discord.Embed(title="Successfuly Removed Role", description=f"{role} role has been successfuly removed from {user}.", color=Color.green())
      await user.remove_roles(role) #removes role if already has it
      await ctx.channel.send(embed=success) 


@client.command()
@commands.has_permissions(administrator=True) #permissions
async def create_role(ctx, *, role_name):
  if role_name in str(ctx.guild.roles):
    alreadyExist = discord.Embed(title="Role Already Exist", description="This role already exist.", color=Color.red())
    await ctx.channel.send(embed=alreadyExist)
  else:
    success = discord.Embed(title="Role Successfuly Created.", description=f"``{role_name}`` Role has been successfuly created..", color=Color.green())
    guild = ctx.guild
    await guild.create_role(name=role_name)
    await ctx.channel.send(embed=success)

@client.command()
@commands.has_permissions(administrator=True) #permissions
async def delete_role(ctx, *, role_name):
  if role_name not in str(ctx.guild.roles):
    doesntExist = discord.Embed(title="Role Does'nt Exist", description="This role does'nt exist.", color=Color.red())
    await ctx.channel.send(embed=doesntExist)
  else:
    success = discord.Embed(title="Role Successfuly Deleted.", description=f"``{role_name}`` Role has been successfuly deleted.", color=Color.green())
    #find role object
    role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
    #delete role
    await role_object.delete()
    
    await ctx.channel.send(embed=success)

@client.command()
@commands.has_permissions(manage_channels=True)
async def create_mute(ctx, role_name=None):
    if role_name:
      success = discord.Embed(title="Successfuly Created Mute Role", description="Muted role has been successfuly created.", color=Color.green())
      perms = discord.Permissions(send_messages=False, read_messages=True)
      guild = ctx.guild
      await guild.create_role(name=role_name, permissions=perms)
      await ctx.channel.send(embed=success)
    else:
      success = discord.Embed(title="Successfuly Created Mute Role", description="Muted role has been successfuly created.", color=Color.green())
      perms = discord.Permissions(send_messages=False, read_messages=True)
      guild = ctx.guild
      await guild.create_role(name=role_name, permissions=perms)
      await guild.create_role(name="Muted", permissions=perms)
      await ctx.channel.send(embed=success)


@client.command(aliases=['nick'])
async def change_nickname(ctx, member: discord.Member, nick):
  em = discord.Embed(title="Nickname Changed", description=f"Nickname changed from {ctx.message.author} to {nick}")
  await member.edit(nick=nick)
  await ctx.channel.send(embed=em)

@client.command()
async def saitamasignal(ctx):
  await ctx.channel.send(f"<@776867805727031336> You have been summoned by {ctx.message.author}")
  await ctx.channel.send("https://tenor.com/view/saitama-one-punch-man-gif-22096414")


# Error handling
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      error = discord.Embed(title="Permission Denied", description="You do not have the required permissions.", color=Color.red())

      await ctx.channel.send(embed=error)
    else:
      raise error


@create_channel.error
async def channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      error = discord.Embed(title="Permission Denied", description="You do not have the required permissions.", color=Color.red())

      await ctx.channel.send(embed=error)
    else:
      raise error

@change_servername.error
async def servername_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      error = discord.Embed(title="Permission Denied", description="You do not have the required permissions.", color=Color.red())

      await ctx.channel.send(embed=error)
    else:
      raise error



client.run(os.getenv('TOKEN'))