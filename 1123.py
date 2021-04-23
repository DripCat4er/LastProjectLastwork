from pathlib import Path
import asyncio

import discord
from discord.ext import commands
import discord
import logging
import sqlite3
import time
import random
import re
from config import settings
from discord import Member

bot = commands.Bot(command_prefix='!')
TOKEN = "ODMxNTYwNDg2MTYzMDU0NjEy.YHXBDQ._4C6zqK9u4K6eqvKnaKON7uq1fE"
prefix = '!'
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")


@bot.command()
async def start(ctx):
    print('cnfhn')
    await ctx.message.channel.send('Полученная команда')


@bot.command(aliases=['chanel','канал'
                               ''])
async def __chanel(ctx):
    embed = discord.Embed(
        title="Киречка приглашает вас на канал",
        description="Канал на ютубе",
        url='https://www.youtube.com/channel/UCtGl_kePXcFHEcJ_wlopkPQ',
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['kirya','киря'])
async def __kirya(ctx):
    embed = discord.Embed(
        title="Кирин стрим задерживается",
        description="Ладно"
    )
    await ctx.send(embed=embed)

@bot.command(aliases=['gh','гш'])
async def __gh(ctx):
    embed = discord.Embed(
        title="Модер проходит подземку в геншине",
        description="Ладно"
    )
    await ctx.send(embed=embed)

@bot.command(aliases=['luba','люба'])
async def __Luba(ctx):
    embed = discord.Embed(
        title="Привет славяне сегодня будет стрим",
        description="Слава богу"
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['донат','donate'])
async def __donate(ctx):
    embed = discord.Embed(
        title="Киря скажет вам спасибо(и Илюша ему тож процентик)",
        description="донат кире(но я скоро поменяю на свой)",
        url='https://www.donationalerts.com/r/brick_nenok',
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['фб','fb'])
async def __fb(ctx):
    embed = discord.Embed(
        title="facebook",
        description="Таг кири",
        url='https://www.facebook.com/profile.php?id=100004317485627',
    )
    await ctx.send(embed=embed)


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}")


@bot.command(aliases=['Ping', 'PING', 'pING', 'ping', 'Пинг', 'ПИНГ', 'пИНГ', 'пинг', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
async def __ping(ctx):
    ping = bot.ws.latency

    ping_emoji = '🟩🔳🔳🔳🔳'

    if ping > 0.10000000000000000:
        ping_emoji = '🟧🟩🔳🔳🔳'

    if ping > 0.15000000000000000:
        ping_emoji = '🟥🟧🟩🔳🔳'
    if ping > 0.20000000000000000:
        ping_emoji = '🟥🟥🟧🟩🔳'
    if ping > 0.25000000000000000:
        ping_emoji = '🟥🟥🟥🟧🟩'

    if ping > 0.30000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟧'

    if ping > 0.35000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟥'
    await ctx.send(ping_emoji)


@bot.command(aliases=['инфо', 'ИНФО', 'Инфо', 'Info', 'info', 'INFO', 'iNFO', 'information', 'информация'])
async def __info(ctx):
    embed = discord.Embed(
        title="Сервер Brick_nenok. Бот создан 17.04.21. Все команды вы можете посмотреть по команде !хелп. Удачного Дня!",

    )
    await ctx.send(embed=embed)


@bot.command
async def Hello(ctx):
    embed = discord.Embed(
        title="Приветствую, новоприбывший! Список доступных команд ты можешь посмотреть по команде !help",
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['twich', 'твич'])
async def __twich(ctx):
    embed = discord.Embed(
        title="Твич",
        url='https://www.twitch.tv/brick_nenok',
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['author', 'Author', 'AUTHOR', 'aUTHOR', 'автор', 'Автор', 'аВТОР'])
async def __author(ctx):
    embed = discord.Embed(
        title="Автор бота непревзойденный Маклаков Илья Русланович а автор спит и он Киречка. Стример шлет вам Привет!",
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['rules', 'правила'])
async def __rules(ctx):
    embed = discord.Embed(
        title="Правила: Существует система правил, которая подразумевается так: 3 предупреждения - кик. Предупреждение можно получить за мат, флуд и оскорбления. Удачного дня, и не нарушайте правила!",
    )
    await ctx.send(embed=embed)


@bot.command(aliases=['Help', 'help', 'HELP', 'hELP', 'хелп', 'Хелп', 'ХЕЛП', 'хЕЛП'])
async def __help(ctx):
    emb = discord.Embed(title='ДОСТУПНЫЕ КОМАНДЫ:',
                        colour=discord.Color.red())

    emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.add_field(name='Инфа о канале',
                  value=f'`{prefix}хелп` `{prefix}инфо` `{prefix}автор` `{prefix}rules` `{prefix}twich` `{prefix}Hello` `{prefix}ping` `{prefix}chanel` `{prefix}donate` `{prefix}fb`',
                  inline=False)
    emb.add_field(name='Для модеров',
                  value=f'`{prefix}mute``{prefix}кик`', inline=False)
    emb.set_thumbnail(url=bot.user.avatar_url)
    emb.set_footer(icon_url=bot.user.avatar_url, text=f'{bot.user.name} © Copyright 2020 | Все права защищены')

    await ctx.send(embed=emb)

    print(f'[Logs:info] Справка по командам была успешно выведена | {prefix}help ')


@bot.command(aliases=['кик', 'Кик', 'кИК', 'КИК', 'Kick', 'kICK', 'KICK', 'kick'])
@commands.has_permissions(administrator=True)
async def __kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    emb = discord.Embed(title='kick', description=f'Пользователь {member}  был кикнут по причине {reason} ',
                        colour=discord.Color.red())
    emb.set_author(name=bot.user.name)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url=bot.user.avatar_url)

    await ctx.send(embed=emb)

    print(f'[Logs:moderation] Пользователь {member} был кикнут по причине {reason} | {prefix}kick ')


@__kick.error
async def kick_error(ctx, goodbye):
    if isinstance(goodbye, commands.MissingRequiredArgument):
        emb = discord.Embed(title=f'**Команда "{prefix}кик"**',
                            description=f'Изгоняет указаного участника с сервера с возможностью возвращения ',
                            colour=discord.Color.red())
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.add_field(name='Использование', value="!кик <@⁣Участник | ID>", inline=False)
        emb.add_field(name='Пример', value="`!кик @⁣Участник`\n┗ Кикнет указаного участника.", inline=False)
        emb.set_thumbnail(url=bot.user.avatar_url)
        emb.set_footer(icon_url=bot.user.avatar_url,
                       text=f"{settings['OWNER NAME']} © Copyright 2020 | Все права защищены")
        await ctx.send(embed=emb)
        print(f"[Logs:error] Необходимо указать участника | {prefix}kick")

    if isinstance(goodbye, commands.MissingPermissions):
        emb = discord.Embed(title=f'**Команда "{prefix}кик"**',
                            description=f'Изгоняет указаного участника с сервера с возможностью возвращения ',
                            colour=discord.Color.red())
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.add_field(name='ОШИБКА!', value="У вас недостаточно прав!", inline=False)
        emb.set_thumbnail(url=bot.user.avatar_url)
        await ctx.send(embed=emb)
        print(f"[Logs:Error] [Ошибка доступа] Пользователь [{ctx.author}] попытался кикнуть | {prefix}kick")


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, time: int, reason=None):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Muted')
    if not mute_role:
        mute_role = await ctx.guild.create_role(name='Muted',
                                                permissions=discord.Permissions(send_messages=False),
                                                color=discord.Color.red())
        for i in ctx.guild.channels:
            await i.set_permissions(mute_role, send_messages=False)
        mute_role = discord.utils.get(ctx.message.guild.roles, name='Parrot Muted')
    if mute_role:
        emb = discord.Embed(title='Мут', timestamp=ctx.message.created_at,
                            colour=discord.Colour.from_rgb(207, 215, 255))
        emb.add_field(name='Выдал мут', value=ctx.message.author.mention, inline=True)
        emb.add_field(name='Нарушитель', value=member.mention)
        emb.add_field(name='Причина', value=reason, inline=True)
        emb.add_field(name='Время', value=time, inline=True)
        emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await member.add_roles(mute_role)
        await ctx.send(embed=emb)
        await asyncio.sleep(time * 60)
        await member.remove_roles(mute_role)
    else:
        await ctx.send("Неверный аргумент!")


@mute.error
async def mute_error(ctx, goodbye):
    if isinstance(goodbye, commands.MissingRequiredArgument):
        emb = discord.Embed(title=f'**Команда "{prefix}mute"**',
                            description=f'Блокирует пользователя на некоторое время',
                            colour=discord.Color.red())
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.add_field(name='Использование', value="!mute <@⁣Участник | ID>", inline=False)
        emb.add_field(name='Пример', value="`!mute @⁣Участник`\n┗ Замутит указаного участника.", inline=False)
        emb.set_thumbnail(url=bot.user.avatar_url)
        await ctx.send(embed=emb)
        print(f"[Logs:error] Необходимо указать участника | {prefix}kick")

    if isinstance(goodbye, commands.MissingPermissions):
        emb = discord.Embed(title=f'**Команда "{prefix}кик"**',
                            description=f'Изгоняет указаного участника с сервера с возможностью возвращения ',
                            colour=discord.Color.red())
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.add_field(name='ОШИБКА!', value="У вас недостаточно прав!", inline=False)
        emb.set_thumbnail(url=bot.user.avatar_url)
        await ctx.send(embed=emb)
        print(f"[Logs:Error] [Ошибка доступа] Пользователь [{ctx.author}] попытался кикнуть | {prefix}kick")


bot.run(settings['TOKEN'])
