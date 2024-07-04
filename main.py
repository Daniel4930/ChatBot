import discord, os
import gemini_API
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    chatting = False
    chat_session = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Log) {message.author}: {message.content}')

        content = str(message.content).lower()

        if message.author.id != self.user.id:
            if content == '/help':
                await message.channel.send("Command available:\n/chat: You can chat with me\n/endChat: End the chat session")
            elif content == '/chat':
                self.chatting = True
                self.chat_session = gemini_API.start_model()
                await message.channel.send("Start chatting! You can go first.")
                return
            elif content == '/endchat':
                self.chatting = False
                await message.channel.send("End chat session")
                return

            if self.chatting:
                response = gemini_API.chatting(self.chat_session, content)
                await message.channel.send(response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])