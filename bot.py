import discord
import os
from scraper import check_target_stock

# Securely grabs the secret token from Render environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot has logged in as {client.user}')

@client.event
async def on_message(message):
    # Stop the bot from responding to itself
    if message.author == client.user:
        return

    # A command you can type in your Discord server to test it!
    if message.content.startswith('!checkpeach'):
        await message.channel.send("🕵️ Checking Target for the Squeezy Peach...")
        
        # TCIN is Target's ID for the item (84770895 for Squeezy Peach)
        is_in_stock = check_target_stock(tcin_id="84770895", store_zip="54911")
        
        if is_in_stock:
            # Creates the public thread in Discord
            thread = await message.channel.create_thread(
                name="🚨 PEACH IN STOCK", 
                type=discord.ChannelType.public_thread
            )
            await thread.send(f"<@{message.author.id}> The Sunny Days Squeezy Peach is EXACTLY IN STOCK at your store! Go go go!")
        else:
            await message.channel.send("No luck. Out of stock or limited quantity.")

def run_discord_bot():
    if TOKEN:
        client.run(TOKEN)
    else:
        print("No Discord token found! (This is normal if testing locally)")