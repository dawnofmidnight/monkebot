import asyncio
from typing import Optional

import discord
from discord.ext import commands

from bot import constants

NUMBER_EMOJIS = {i: f"{i}\N{COMBINING ENCLOSING KEYCAP}" for i in range(1, 10)}


class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(
        self,
        ctx: commands.Context,
        duration: Optional[int] = 60,
        *,
        args: str,
    ):
        """Creates poll in the #polls channel on the given topic for given duration (in seconds).
        Usage: !poll duration topic: option1|option2|option3"""

        channel = self.bot.get_channel(constants.Channels.polls)
        topic, args = args.split(":")  # separate poll topic and options

        options = {i + 1: option for i, option in enumerate(args.split("|"))}

        embed = discord.Embed(title="Poll")

        embed.add_field(
            name=topic,
            value="\n".join(f"{i}. {option}" for i, option in options.items()),
        )

        embed_message = await channel.send(embed=embed)

        used_reactions = set()

        for i in options.keys():
            await embed_message.add_reaction(NUMBER_EMOJIS[i])
            used_reactions.add(NUMBER_EMOJIS[i])

        await asyncio.sleep(duration)

        # fetch reactions on the poll message
        reactions = [
            reaction
            for reaction in (await channel.fetch_message(embed_message.id)).reactions
            if reaction.emoji in used_reactions
        ]
        winner = max(reactions, key=lambda reaction: reaction.count)

        await channel.send(f"Poll won by: {options[int(winner.emoji[0])]}")


def setup(bot: commands.Bot) -> None:
    """Add Polls Cog."""
    bot.add_cog(Polls(bot))
