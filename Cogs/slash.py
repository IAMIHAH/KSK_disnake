import disnake
from disnake.ext import commands

class Slash(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(
		name="slash",
		description="Slash Commands!",
		guild_ids=[742188157424107679]
	)
	async def slash(self, i: disnake.CommandInteraction):
		await i.response.send_message("Slash Commands!", ephemeral=True)

def setup(bot):
	bot.add_cog(Slash(bot))