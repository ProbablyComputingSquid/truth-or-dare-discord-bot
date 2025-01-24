import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from tord import tr, da

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
GUILD = 1320526719626645504
@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=GUILD)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
@tree.command(
    name="profile",
    description="get user profile",
    guild=discord.Object(id=GUILD),
)
async def profile(interaction):
    User = await client.fetch_user(int(interaction.user.id))
    #print(User.avatar)
    await interaction.response.send_message(User.avatar)
@tree.command(
    name="embed_test",
    description="Embedding Test",
    guild=discord.Object(id=GUILD),
)
async def embedTest(interaction):
    embed=discord.Embed(title="Question here")
    User = await client.fetch_user(int(interaction.user.id))
    embed.set_author(name="Username", url=User.avatar)
    embed.set_footer(text="Type: X, Rating: Y, ID: Z")
    await ctx.send(embed=embed)


@tree.command(
    name="truth",
    description="Is it the truth?",
    guild=discord.Object(id=GUILD),
)
async def truth(interaction):
    await interaction.response.send_message(tr())

@tree.command(
    name="dare",
    description="Do you dare?",
    guild=discord.Object(id=GUILD),
)
async def dare(interaction):
    await interaction.response.send_message(da())
    
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    print("Ready!")


load_dotenv()
client.run(os.environ['TORDTOKEN'])