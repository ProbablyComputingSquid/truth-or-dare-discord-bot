import discord
from discord import app_commands, ext
from discord.ui import Button, View
import os
from random import randint
from dotenv import load_dotenv
from tord import truth, dare

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


async def truthEmbed(interaction):
    info = truth()
    embed=discord.Embed(title=f'{info["question"]}', color=0x58b9ff)
    User = await client.fetch_user(int(interaction.user.id))
    embed.set_author(name=f'Requested by: {User.display_name}', icon_url=User.avatar)
    
    embed.set_footer(text=f'Type: Truth | Rating: {info["rating"]} | ID: {info["id"]}')
    return embed
async def dareEmbed(interaction):
    info = dare()
    embed=discord.Embed(title=f'{info["question"]}', color=0x58b9ff)
    User = await client.fetch_user(int(interaction.user.id))
    embed.set_author(name=f'Requested by: {User.display_name}', icon_url=User.avatar)
    
    embed.set_footer(text=f'Type: Dare | Rating: {info["rating"]} | ID: {info["id"]}')
    return embed
# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
GUILD = 1320526719626645504
@tree.command(
    name="ping",
    description="Pong!",
    guild=discord.Object(id=GUILD)
)
async def ping(interaction):
    await interaction.response.send_message("Pong!")
    
@tree.command(
    name="profile",
    description="get user profile",
    guild=discord.Object(id=GUILD),
)
async def profile(interaction):
    User = await client.fetch_user(int(interaction.user.id))
    await interaction.response.send_message(User.avatar)

class EmbedButtons(View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="Truth", style=discord.ButtonStyle.green, custom_id="truth_button")
    async def truth_button_callback(self, interaction: discord.Interaction, button: Button):
        await truthQuestion.callback(interaction)
        await interaction.message.edit(view=None)
    @discord.ui.button(label="Dare", style=discord.ButtonStyle.red, custom_id="dare_button")
    async def dare_button_callback(self, interaction: discord.Interaction, button: Button):
        await dareQuestion.callback(interaction)
        await interaction.message.edit(view=None)
    @discord.ui.button(label="Random", style=discord.ButtonStyle.blurple, custom_id="random_button")
    async def hello_button_callback(self, interaction: discord.Interaction, button: Button):
        if randint(0,1) == 0:
            await truthQuestion.callback(interaction)
        else:
            await dareQuestion.callback(interaction)
        await interaction.message.edit(view=None)


@tree.command(
    name="embed_test",
    description="Embedding Test",
    guild=discord.Object(id=GUILD),
)
async def embedTest(interaction):
    info = truth()
    embed=discord.Embed(title=f'{info["question"]}')
    view=EmbedButtons()
    User = await client.fetch_user(int(interaction.user.id))
    embed.set_author(name=f'Requested by:{User.display_name}', url=User.avatar)
    
    embed.set_footer(text=f'Type: Truth, Rating: {info["rating"]}, ID: {info["id"]}')

    await interaction.response.send_message(embed=embed, view=view)


@tree.command(
    name="truth",
    description="Get a random question that must be answered truthfully",
    guild=discord.Object(id=GUILD),
)
async def truthQuestion(interaction):
    view = EmbedButtons()
    embed = await truthEmbed(interaction)
    await interaction.response.send_message(embed=embed, view=view)

@tree.command(
    name="dare",
    description="Do you dare to complete this task?",
    guild=discord.Object(id=GUILD),
)
async def dareQuestion(interaction):
    view = EmbedButtons()
    embed = await dareEmbed(interaction)
    await interaction.response.send_message(embed=embed, view=view)
@tree.command(
    name="random",
    description="Get a random Truth or Dare",
    guild=discord.Object(id=GUILD),
)
async def randomQuestion(interaction):
    if randint(0,1) == 0:
        await truthQuestion.callback(interaction)
    else:
        await dareQuestion.callback(interaction)
@tree.command(
    name="credits",
    description="Get the credits for this bot",
    guild=discord.Object(id=GUILD),
)
async def credits(interaction):
    description = """
    This was a remake of the classic Truth or Dare bot that is widespread accross the discord platform. I attempted to remake it in discord.py with added customizability and transparency. 
    No longer will there be paywalls, open access forever!
    Truth or Dare 2 - Electric Boogaloo was created in part for Hack Club's High Seas initiative, and is hosted on Hack Club's nest service.
    Made with discord.py, sweat, and tears by <@697889258215702588>
    """
    embed = discord.Embed(title="Credits | Truth or Dare 2 - Electric Boogaloo", description=description)
    
    await interaction.response.send_message(embed=embed)

@app_commands.choices(type=[
    app_commands.Choice(name="Truth", value=0),
    app_commands.Choice(name="Dare", value=1),
])

@tree.command(
    name="add",
    description="add a truth or dare to the questions list (admins only)",
    guild=discord.Object(id=GUILD),
)

async def addQuestion(interaction, type: app_commands.Choice[int], question: str):
    if question.strip() == "":
        await interaction.response.send_message("You can't add an empty question!")
        return
    if interaction.user.guild_permissions.administrator:
        if type.value == 0:
            with open("questions/t.txt", "a") as f:
                f.write("\n" + question)
        elif type.value == 1:
            with open("questions/d.txt", "a") as f:
                f.write("\n" + question)
        await interaction.response.send_message(f"Successfully added {type.name} `{question}` to the {type.name}s list.")
    else:
        await interaction.response.send_message("You aren't an administrator, you can't add questions!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    print("All Ready!")


load_dotenv()
client.run(os.environ['TORDTOKEN'])