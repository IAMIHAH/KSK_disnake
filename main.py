import os
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print("Ready!")

for filename in os.listdir("Cogs"):
	if filename.endswith(".py"):
		fn = filename[:-3]
		try:
			bot.load_extension(f"Cogs.{fn}")
			print(f"{fn}: Sucessfully Loaded!")
		except Exception as e:
			print(f"{fn}: Error: {e}")

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

bot.run("OTQ2MjgwOTM3MjAzODM0ODgw.YhcazA.CiYXYVr0mD2-iUi2bblurfEglfQ")