import discord
from discord.ext import commands

import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA2NjM5NDM3OTAyOTMxOTY5Mw.GaD34_.C-v3YEWhZ-4h7nfdc8ddiVJIEau_1CbVZ33oiM'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    #defining what the bot does when a certain event happens
    @client.event
    async def on_ready():
        print("im running and im online")

    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)
    #     print(f"{username} said '{user_message}' ({channel})")
    #     if user_message[0] == '$':
    #         user_message = user_message[1:]
    #         split_message = user_message.split(' ')
    #         dms_index = len(split_message) - 1
    #         dms = split_message[dms_index]
    #         if dms == 'mute' :
    #             is_private = True
    #             msg_length = len(user_message) - 5
    #             user_message = user_message[:msg_length]
    #         else:
    #             is_private = False
    #         print(user_message)
    #         await ctx.send(embed=send_message(message, user_message, is_private))
    # @client.event
    # async def embed(ctx):
    #     embed = discord.Embed(
    #         title="Here are $ave-a-thon's possible commands",
    #         description="How to access the different commands",
    #         color=discord.Color.blue())
    #     embed.set_thumbnail(
    #         url="https://th.bing.com/th/id/R.bd382a74a382c1a3a20cf3ffd1bfc6cd?rik=M00Efr8m1TP%2baw&riu=http%3a%2f%2fwww.moorgateacoustics.co.uk%2fwp-content%2fuploads%2f2014%2f06%2fhelp.jpg&ehk=aQLQP7HYubrfeyk9At80bMM%2brSORKn2THoreN7zZzuY%3d&risl=&pid=ImgRaw&r=0")
    #     embed.add_field(name="$calculator",
    #                    value="Built-in calculator functions to help you calculate (tax, interest, inverse_interest)\n",
    #                    inline=False)
    #     embed.add_field(name="$new_profile", value="Creating your profile \n", inline=False)
    #     embed.add_field(name="$profile", value="Allows you to view the specifics of your account \n", inline=False)
    #     embed.add_field(name="$FAQ", value="Frequently asked Questions and their answers \n", inline=False)
    #     return ctx.send(embed=embed)

    client.run(TOKEN)