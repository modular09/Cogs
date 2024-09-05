from discord.ext import commands
import discord


class Embeds:
    class on_message(discord.Embed):
        def __init__(self, message: discord.Message):
            super().__init__(color=discord.Color.green(), title='Sent message')
            # Fields
            self.add_field(name='Content', value=f'"{message.content}"', inline=True)
            self.add_field(name='Channel', value=message.channel.mention, inline=True)
            self.add_field(name='Jump to', value=message.jump_url, inline=True)
            # Author & Footer
            self.set_author(icon_url=message.author.avatar, name=message.author.name)
            self.set_footer(text=f'ID: {message.id}')

    class on_message_edit(discord.Embed):
        def __init__(self, before: discord.Message, after: discord.Message):
            super().__init__(color=discord.Color.orange(), title='Edit message')
            # Fields
            self.add_field(name='Before', value=f'"{before.content}"', inline=True)
            self.add_field(name='After', value=f'"{after.content}"', inline=False)

            self.add_field(name='Channel', value=after.channel.mention, inline=True)
            self.add_field(name='Jump to', value=after.jump_url, inline=True)
            # Author & Footer
            self.set_author(icon_url=after.author.avatar, name=after.author.name)
            self.set_footer(text=f'ID: {after.id}')

    class on_message_delete(discord.Embed):
        def __init__(self, message: discord.Message):
            super().__init__(color=discord.Color.red(), title='Deleted message')
            # Fields
            self.add_field(name='Content', value=f'"{message.content}"', inline=True)
            self.add_field(name='Channel', value=message.channel.mention, inline=True)
            # Author & Footer
            self.set_author(icon_url=message.author.avatar, name=message.author.name)
            self.set_footer(text=f'ID: {message.id}')


class Log(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # self.channel = self.bot.get_channel(None)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author is not self.bot:
            if not message.author.bot:
                # await self.channel.send(embed=Embeds.on_message(message=message))
                ...

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if after.author is not self.bot:
            if not after.author.bot:
                # await self.channel.send(embed=Embeds.on_message_edit(before, after))
                ...

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author is not self.bot:
            if not message.author.bot:
                # await self.channel.send(embed=Embeds.on_message_delete(message=message))
                ...

# Setting up the cog
async def setup(bot: commands.Bot):
    await bot.add_cog(Log(bot=bot))
