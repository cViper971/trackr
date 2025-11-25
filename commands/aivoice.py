from discord import Interaction, Object

def setup_aivoice_commands(tree, guild_id):
    @tree.command(name="join", description="Bot joins your current voice channel", guild=Object(id=guild_id))
    async def join(interaction: Interaction):
        if interaction.user.voice:
            channel = interaction.user.voice.channel
            await channel.connect()
            await interaction.response.send_message(f"Joined {channel.name}")
        else:
            await interaction.response.send_message("You're not in a voice channel!")

    @tree.command(name="leave", description="Bot leaves the current voice channel", guild=Object(id=guild_id))
    async def leave(interaction: Interaction):
        voice_client = interaction.guild.voice_client
        if voice_client:
            await voice_client.disconnect()
            await interaction.response.send_message("Left the voice channel.")
        else:
            await interaction.response.send_message("I'm not in a voice channel.")