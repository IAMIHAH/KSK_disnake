import disnake
from disnake.ext import commands

class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="이건 버튼입니다!", style=disnake.ButtonStyle.blurple)
    async def thisisbutton(self, button: disnake.Button, i: disnake.Interaction):
        await i.response.send_message("버튼을 클릭했습니다!")

class CmdButton(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(
		name="button",
		description="Send Button!",
		guild_ids=[742188157424107679]
	)
	async def slash(self, i: disnake.CommandInteraction):
		await i.response.send_message("Buttons!", view=ButtonView(), ephemeral=True)

def setup(bot):
	bot.add_cog(CmdButton(bot))