import discord
import random

def generate_the_word(word_list):
    return random.choice(word_list)

intents = discord.Intents().all()
client = discord.Client(intents=intents);

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$z'):
        infile = open("/PATH/TO/words.txt","r")
        lines = infile.readlines()
        infile.close()
        quote = generate_the_word(lines)
        await message.channel.send(quote)

#encode key somehow?
client.run('API KEY HERE')
