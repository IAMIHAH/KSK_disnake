import disnake
from disnake.ext import commands

class SelectClass(disnake.ui.Select):
    def __init__(self):
        options=[
            disnake.SelectOption(
                label="Label1",
                description="Desc1"
            ),
            disnake.SelectOption(
                label="Label2",
                description="Desc2"
            )
        ]
        super().__init__(
            placeholder="선택하세요!",
            options=options,
            max_values=2
        )
    
    async def callback(self, i: disnake.Interaction):
        await i.response.send_message(f"{self.values[0]}", ephemeral=True)

class SelectView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectClass())

class SelectCmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(
		name="select",
		description="Send Select!",
		guild_ids=[742188157424107679]
	)
	async def slash(self, i: disnake.CommandInteraction):
		await i.response.send_message("Select!", view=SelectView(), ephemeral=True)

def setup(bot):
	bot.add_cog(SelectCmd(bot))