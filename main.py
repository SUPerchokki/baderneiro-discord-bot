# Bot do discord da taverna
# Autor: Gabriel de Nazaré / SUPerchokki
# Importando o configurador de comandos
import discord
from discord.ext import commands

# Criando o client(usuario) do discord
bot = commands.Bot('!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name="oi")
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


@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    try:
        # cuidado com eval, ele pode fazer com que terceiros rodem codigos dentro do meu bot
        expression = ''.join(expression)
        response = eval(expression)
        await ctx.send(response)
    except AttributeError:
        await ctx.send('por favor digite uma expressão matematica')

@bot.command(name="teste")
async def get_random_image(ctx):
    url_image="https://picsum.photos/1920/1080.jpg"
    embed_ig=discord.Embed(
        title="aqui ta o titulo",
        description="e aqui outra coisa",
        color=0x0000FF,
    )
    embed_ig.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_ig.set_footer(text="feito por " + bot.user.name, icon_url=bot.user.avatar_url)

    embed_ig.add_field(name="Teste1", value="textin")
    embed_ig.add_field(name="teste2", value="textin2")
    embed_ig.add_field(name="teste3",value="textin3", inline=False)
    embed_ig.set_image(url=url_image)

    await ctx.send(embed=embed_ig)

@bot.command(name="h")
async def ajuda(ctx):
    await ctx.send("Comandos:\n"
                   "!oi\n"
                   "!calcular\n")


with open('TOKEN.txt', 'r') as f:
    token = f.read()

bot.run(token)
