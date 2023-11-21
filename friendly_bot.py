import discord 
import datetime

token = 'MTE3MTQ0ODY3NzgzNjAwOTU5Mg.Go7me1.LypGkQgAIu6HA7T-XcCD9gPcCKZTI0xYzA5QbY'
bot = discord.Bot(intents = discord.Intents.all())
c = discord.commands.context.ApplicationContext

@bot.slash_command(description = 'Текущее время.')
async def time(ctx:c, timezone:discord.Option(int)):
    Moscow = datetime.timezone(datetime.timedelta(hours = timezone))
    data = datetime.datetime.now(Moscow)
    await ctx.respond(f'Текущее время: {data.hour}:{data.minute}') 
    
@bot.slash_command(description = 'Сложение.')
async def summ(ctx:c,number_1:discord.Option(int), number_2:discord.Option(int)):
    sum = number_1 + number_2
    await ctx.respond(f'Результат сложения: {sum}')


@bot.slash_command(description = 'Вычитание.')
async def sub(ctx:c,number_1:discord.Option(int), number_2:discord.Option(int)):
    sum = number_1 - number_2
    await ctx.respond(f'Результат вычитание: {sum}')

@bot.slash_command(description = 'Деление.')
async def div(ctx:c,number_1:discord.Option(int), number_2:discord.Option(int)):
    sum = number_1 / number_2
    await ctx.respond(f'Результат деление: {sum}')

@bot.slash_command(description = 'Умножение.')
async def mult(ctx:c,number_1:discord.Option(int), number_2:discord.Option(int)):
    sum = number_1 * number_2
    await ctx.respond(f'Результат умножение: {sum}')



@bot.message_command(name = 'Повысить репутацию.', )
async def plus_rep(ctx:c, message:discord.Message):
    await ctx.respond(f'Ваша репутация повышена {message.author.name}')




@bot.user_command(name = 'Дата регистрации.')
async def account_creation_date(ctx:c, member:discord.Member):
    await ctx.respond(f'{member.name} создал аккаунт {member.created_at}')


@bot.event
async def on_member_join(member:discord.Member):
    channels = member.guild.channels
    for i in channels:
        if i.name == 'прихожая':
            await i.send(f'Добро пожаловать {member.name}.')
            
            
            
@bot.event
async def on_member_remove(member:discord.Member):
    for i in member.guild.channels:
        if i.name == 'прихожая':
            await i.send(f'Прощай {member.name}.')
    
            

@bot.event
async def on_member_update(old:discord.Member, new:discord.Member):
    channels = None
    members = bot.get_all_members()
    for mem in members:
        if mem.name == new.name:
            channels = mem.guild.channels
    for chan in channels:
        if chan.name == 'основной':
            channel = chan
    if old.avatar != new.avatar:
        await channel.send(f'У {new.name} новая аватарка.')
        await channel.send(new.avatar.url)
        
@bot.event
async def on_user_update(old:discord.User, new:discord.User):
    channels = None
    members = bot.get_all_members()
    for mem in members:
        if mem.name == new.name:
            channels = mem.guild.channels
    for chan in channels:
        if chan.name == 'основной':
            channel = chan
    if old.avatar != new.avatar:
        await channel.send(f'У {new.name} новая аватарка.')
        await channel.send(new.avatar.url)
        
@bot.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    for ban in bun_warlds:
        if ban in message.content:
            await message.delete(delay=2)

bun_warlds = ['зебра', 'зебры', 'зеброй', 'Mq', 'MQ', 'mQ', 'мкью', 'ью', 'mq','мамаq', 'мамеq', 'Мамеq' ]
# @bot.event#работает на каком-то событие 
# async def on_message(message:discord.Message): #message:discord.Message - информация о сообщений
#     if message.author.bot:
#         return
#     # await message.reply('Hello')
#     await message.channel.send(message.content)







bot.run(token)