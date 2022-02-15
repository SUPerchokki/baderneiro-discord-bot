# Bot do discord da taverna
# Autor: Gabriel de Nazaré / SUPerchokki
# Importando o configurador de comandos
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from decouple import config

# Criando o client(usuario) do discord
bot = commands.Bot('!')


# Evento on ready para quando o bot entra online
@bot.event
async def on_ready():
    # Discord.activity para mudar o "status" do bot para Ouvindo
    activity = discord.Activity(type=discord.ActivityType.listening, name="Bot da Taverna")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    # print para avisar que o bot ta online
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Esse comando não existe, digite !help para a lista de comandos")
    else:
        raise error


# Comando para dar uma saudação
@bot.command(name="oi", help="Dá Uma saldação")
async def send_hello(ctx):
    name = ctx.author.name
    if str(ctx.author) == "marechal#3177":
        response = "Ola papai"
    elif str(ctx.author) == "SUPerchokki#4524":
        response = "Nhain Gabs"
    elif str(ctx.author) == "SH4Z4N#0215":
        response = "Fala corno"
    elif str(ctx.author) == "SrLemont#2725":
        response = "oi Limão"
    elif str(ctx.author) == "lecare#8428":
        response = "T=Tech soluções de tecnologia, a melhor assistencia para o seu aparelho" \
                   "https://www.instagram.com/ttech_solucoes/"
    else:
        response = 'nome: ' + name
    await ctx.send(response)


# Comando que faz calculos matematicos
@bot.command(name="calcular", help="Calcula uma expressão Matematica")
async def calculate_expression(ctx, *expression):
    try:
        # cuidado com eval, ele pode fazer com que terceiros rodem codigos dentro do meu bot
        expression = ''.join(expression)
        response = eval(expression)
        await ctx.send(response)
    except AttributeError:
        await ctx.send('por favor digite uma expressão matematica')


@bot.command(name="zap", help="link do grupo do zap")
async def whatsapp_group(ctx):
    embed_zap = discord.Embed(
        title="Grupo da Taverna no Whatsapp",
        description="http://bit.ly/TavernaWhats",
        color=0x25D366
    )
    embed_zap.set_author(name="Taverna dos Games")
    embed_zap.set_footer(text="feito por " + bot.user.name, icon_url=bot.user.avatar_url)
    embed_zap.set_image(url='https://comunicall.com.br/wp-content/uploads/2017/03/whatsapp-icon.png')
    await ctx.send(embed=embed_zap)


# Teste do Aviso que vou usar para avisar a twitch
@bot.command(name="teste", help="comando que uso para testar novas funcionalidades")
async def get_random_image(ctx):
    url_image = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"
    embed_ig = discord.Embed(
        title="aqui ta o titulo",
        description="e aqui outra coisa",
        color=0x0000FF
    )
    embed_ig.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_ig.set_footer(text="feito por " + bot.user.name, icon_url=bot.user.avatar_url)
    embed_ig.set_thumbnail(url=url_image)

    embed_ig.add_field(name="Teste1", value="textin")
    embed_ig.add_field(name="teste2", value="textin2")
    embed_ig.add_field(name="teste3", value="textin3", inline=False)

    await ctx.send(embed=embed_ig)

TOKEN = config("TOKEN")
bot.run(TOKEN)
