import os
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='&', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')


@bot.command()
async def ping(ctx):

    await ctx.send('Pong!')
    

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = None):
    if amount is None:
        deleted = await ctx.channel.purge(limit=2)
        await ctx.send(f"🗑 Удалено 1 сообщение.", delete_after=3)
        return
    
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🗑 Удалено {len(deleted) - 1} сообщений.", delete_after=3)

@bot.command()
@commands.has_permissions(manage_webhooks=True)
async def create_webhook(ctx, name: str):
    
    webhook = await ctx.channel.create_webhook(name=name)
    
    webhook_url = webhook.url
    await ctx.send(f"✅ Вебхук {name} создан! URL: {webhook_url}")
    
@bot.command()
async def help(ctx):
    await ctx.send(f"&help - показать этот список\n&clear <к-во> - удалить сообщения\n&create_webhook <название> - создать вебхук с именем")
    return


bot.run(TOKEN)