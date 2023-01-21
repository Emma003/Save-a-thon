import discord
import responses

async def send_message(message, user_message, is_private):
    print("test message" + user_message)
    try:
        response = responses.get_response(user_message)
        print("test response" + response)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

    print("test response" + response)
def run_discord_bot():
    TOKEN = 'MTA2NjM5NDM3OTAyOTMxOTY5Mw.GH9zmI.Ym9hlN8z4KVfCg6498fN555SrbJh3ZkZY1UqyE'

    intents = discord.Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)

    #defining what the bot does when a certain event happens
    @client.event
    async def on_ready():
        print("im running and im online")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said '{user_message}' ({channel})")

        if user_message[0] == '$':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)


