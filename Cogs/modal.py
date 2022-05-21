import disnake
from disnake.ext import commands

class ModalUI(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="label",
                custom_id="customid",
                style=disnake.TextInputStyle.short,
                placeholder="placeholder",
                required=True,
                min_length=1,
                max_length=10
            )
        ]
        super().__init__(
            title="title",
            components=components,
            custom_id="modalid",
            timeout=None
        )
    
    async def callback(self, i: disnake.ModalInteraction):
        await i.response.send_message(f"{i.text_values['label']}", ephemeral=True)
        

class Modal(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(
		name="modal",
		description="This is Modal!",
		guild_ids=[742188157424107679]
	)
	async def modal(self, i: disnake.CommandInteraction):
		await i.response.send_message("Slash Commands!", ephemeral=True)

def setup(bot):
	bot.add_cog(Modal(bot))