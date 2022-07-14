from discord.ext import commands
import os
import discord


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()


        super().__init__(command_prefix=commands.when_mentioned_or('%'), intents=intents)

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
    await ctx.send(f"**Pong!** Latency: {round(bot.latency * 1000)}ms")
@bot.event
async def on_member_join(member):
    welcome = discord.Embed(title="'•.¸♡ helllooo ♡¸.•'", color=0xE6E6FA,
                            description=f"Welcome To the server {member.name} !!! \n Please Read all the Rules listed in <#935914067057578056> \n Make Sure to get your self-roles in <#935915930368753694> \n We also have great profile-colors so make sure to check those too <#936976679908298862>")
    welcome.set_image(
        url="https://media3.giphy.com/media/Ulyubf7eYczLO/giphy.gif?cid=790b761197ac7ec60a21ee41ce9122d24380d159e69aded2&rid=giphy.gif&ct=g")

    view = Confirm()
    await bot.get_channel(933980949421621279).send(f" <@&953549791265185832> {member.mention}")
    main_embed = await bot.get_channel(933980949421621279).send(embed=welcome, view=view)
    Homies = 934391119041687593
    await member.add_roles(member.guild.get_role(Homies))
    Level = 934009554134519838
    await member.add_roles(member.guild.get_role(Level))
    Continent = 934015398418993193
    await member.add_roles(member.guild.get_role(Continent))
    Age = 934017875096764426
    await member.add_roles(member.guild.get_role(Age))
    Pronoun = 934018772279382017
    await member.add_roles(member.guild.get_role(Pronoun))
    interest = 934019879722434600
    await member.add_roles(member.guild.get_role(interest))
    pingr = 953550452979535883
    await member.add_roles(member.guild.get_role(pingr))
    await bot.get_channel(935913776379752448).send(f"<:GreenRight:953568769207332864> __*{member.name}*__ has joined")
    await view.wait()
    if view.value is None:
        return
    else:
        await main_embed.reply(f"{view.value} welcomes {member.mention}")

        
@bot.event
async def on_member_remove(member):
   await bot.get_channel(935913776379752448).send(f"<:RedLeft:953568727188791366> __*{member.name}*__ has left")
class stat(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Member Count",emoji=discord.PartialEmoji.from_str("<:Flower_glow:934721253066022962>"),
                       style=discord.ButtonStyle.green)
    async def members(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"Current member count :- __***{interaction.guild.member_count}***__", ephemeral=True)

    @discord.ui.button(label="stats",
                       emoji=discord.PartialEmoji.from_str("<:Flower_glow:934721253066022962>"),
                       style=discord.ButtonStyle.green)
    async def stats(self, interaction: discord.Interaction, button: discord.ui.Button):
        format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
        stats_embed = discord.Embed(title="Server lastest stats",description=f"Member Count - {interaction.guild.member_count} \n \nRole count - {len(interaction.guild.roles)} \n \n Text Channels - {len(interaction.guild.text_channels)} \n \nserver created - {interaction.guild.created_at.strftime(format)}  ||  <t:1647442054:R> \n \n Boost count - {str(interaction.guild.premium_subscription_count)}",color=0xE6E6FA)
        stats_embed.set_thumbnail(url=interaction.guild.icon)
        await interaction.response.send_message(embed=stats_embed, ephemeral=True)




bot = Bot()

@bot.command()
async def stonks(ctx):
    main_embed = discord.Embed(title=" *•.¸♡ Welcome to Ecstasy ♡¸.•* ", description="♡ *• Anime • Social • Dating • Fun* ♡ \n \n  ꘎♡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━♡꘎ \n \n˗ˏˋ ♡ ˎˊ˗ AN anime, Dating, Social, And chill server where you can meet open minded people who share the same interest as you! ˗ˏˋ ♡ ˎˊ˗\n \nೃ⁀➷ Here's what we offer: ೃ⁀➷\n \n ʚɞ Ecstasy is a casual and chill server, the main purpose of the server is for you to have someone to talk and spend time with. You can meet many new people, make new friends and perhaps even find yourself a date or partner.\n  \nʚɞ We have chill staff, and an amazing atmosphere where you'll be able to fit in and meet people just like yourself.\n \n ʚɞ We have many bots to entertain you, for example, mudae, dank-memer, truth & dare and many more!\n \nʚɞ LGBTQ+ supporting and accepting server.\n \nʚɞ Friendly and SFW server\n \nʚɞ We'll make sure you never feel lonely again <3.\n \n˚ ༘♡ ⋆｡˚ 𝒮𝓉𝒾𝓁𝓁 𝓃𝑜𝓉 𝒸𝑜𝓃𝓋𝒾𝓃𝒸𝑒𝒹? Just chat and check for yourself !! ˚ ༘♡ ⋆｡˚",color=0xE6E6FA)
    main_embed.set_thumbnail(url=ctx.guild.icon)

    view = stat()
    await ctx.send(embed=main_embed,view=view)
    return
bot.run(os.environ.get('TOKEN'))  
