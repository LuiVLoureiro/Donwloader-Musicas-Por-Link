import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents = intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    canal = bot.get_channel(O_CANAL_DO_SEU_SERVIDOR_AQUI)
    with open('temporaria/variavel.txt', 'r') as file:
        new_file_name = file.read()
        print(new_file_name)
    with open(f"temporaria/{new_file_name.split('.mp4')[0]}.mp3", 'rb') as f:
        await canal.send(file=discord.File(f, f'{new_file_name.split(".mp4")[0]}.mp3'))
    await bot.close()

bot.run(CODIGO_DO_SEU_BOT_CRIADO)