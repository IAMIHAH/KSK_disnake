import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready!")

@bot.slash_command(
    name="ping",
    description="pong!",
    guild_ids=[742188157424107679],
    options=[
        disnake.Option(
            name="foo",
            description="bar",
            type=disnake.OptionType.string,
            required=True
        )
    ]
)
async def pingpong(
    i: disnake.CommandInteraction,
    foo: str
):
    await i.response.send_message(f"{foo}", ephemeral=True)

bot.run("OTQ2MjgwOTM3MjAzODM0ODgw.YhcazA.H6HrQ3VgBSQzRDiduX8I0wgxhEc")