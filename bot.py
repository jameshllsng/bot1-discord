# Importando bibliotecas
import discord
from discord import Embed
from datetime import datetime

#Informandop ID do chat de logs
log_channel_id = CODIGO REMOVIDO DEVIDO A RISCOS DE PRIVACIDADE
#Definindo permissões do bot
client = discord.Client(intents=discord.Intents.all())

#Iniciando event listener de mensagens deletadas
@client.event
async def on_message_delete(message):
    # Pega as horas
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Cria o embed
    embed = Embed(
        title = "🚨 Mensagem Apagada!",
        description=f"> {message.content}",
        color=0xff0000
    )
    # Adiciona os campos do embed
    embed.add_field(name="Autor", value=str(message.author), inline=True)
    embed.add_field(name="Canal", value=message.channel.mention, inline=True)
    embed.set_footer(text=f"Data e hora: {data_hora}")

    # Envia no canal original
    await message.channel.send(embed=embed)

    # Reenvia no canal de logs
    log_channel = client.get_channel(log_channel_id)
    await log_channel.send(embed=embed)

#Iniciando event listener de mensagens editadas
@client.event
async def on_message_edit(before, after):
    # Pega as horas
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Cria o embed
    embed = Embed(
        title = "⚠️ Mensagem Editada!",
        description=f"> {after.content}",
        color=0xffd400
    )
    # Adiciona os campos do embed
    embed.add_field(name="Mensagem original: ", value=str(before.content), inline=False)
    embed.add_field(name="Autor", value=str(before.author), inline=True)
    embed.add_field(name="Canal", value=before.channel.mention, inline=True)
    embed.set_footer(text=f"Data e hora: {data_hora}")

    # Envia no canal original | Resolvi não habilitar isso
    #await before.channel.send(embed=embed)

    # Reenvia no canal de logs
    log_channel = client.get_channel(log_channel_id)
    await log_channel.send(embed=embed)

#Token do BOT
client.run('CODIGO REMOVIDO DEVIDO A RISCOS DE PRIVACIDADE')
