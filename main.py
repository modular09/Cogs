from discord.ext import commands
import discord, os

# Create (commands.Bot)
class Bot(commands.Bot):
    def __init__(self):
        # May be edit intents if facing error
        intents = discord.Intents.all()
        # Modifying `command_prefix` and etcetera
        super().__init__(command_prefix='', intents=intents)

    async def on_ready(self):
        # Loads all extensions on `cogs` folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        # Syncing tree
        await self.tree.sync()

# Gets (commands.Bot)
bot: commands.Bot = Bot()

# Set your token
if __name__ == '__main__':
  bot.run(token=None)
