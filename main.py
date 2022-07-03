from discord.ext import commands
import os
import discord


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()


        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


# Define a simple View that gives us a confirmation menu
class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(emoji=discord.PartialEmoji.from_str("<:Flower_glow:934721253066022962>"), style=discord.ButtonStyle.grey)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = interaction.user.mention
        self.stop()

bot = Bot()

@bot.command()
async def ping(ctx):
    await ctx.send("**Pong!** Latency: {round(bot.latency * 1000)}ms")

@bot.event
async def on_member_join(member):
    welcome = discord.Embed(title="'•.¸♡ helllooo ♡¸.•'", color=0xE6E6FA,
                            description=f"Welcome To the server {member.name} !!! \n Please Read all the Rules listed in <#935914067057578056> \n Make Sure to get your self-roles in <#935915930368753694> \n We also have great profile-colors so make sure to check those too <#936976679908298862>")
    welcome.set_image(
        url="https://media3.giphy.com/media/Ulyubf7eYczLO/giphy.gif?cid=790b761197ac7ec60a21ee41ce9122d24380d159e69aded2&rid=giphy.gif&ct=g")

    view = Confirm()
    await bot.get_channel(992752744018493440).send(f" <@&953549791265185832> {member.mention}")
    main_embed = await bot.get_channel(992752744018493440).send(embed=welcome, view=view)
    await view.wait()
    if view.value is None:
        return
    else:
        await main_embed.reply(f"{view.value} welcomes {member.mention}")

bot.os.environ.get('TOKEN')
