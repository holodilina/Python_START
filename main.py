## Домашнее задание №9

##Прикрутить бота к задаче с предыдущими семинарами и домашними заданиями 
# (3 любых):
## Вычисление выражений, заданных строкой
## Перевод числа в двоичную систему
## Вывод чисел НегаФибоначчи
## RLE шифрование
## Попробуйте отделить ввод данных от ввода данных. 
# Можно создать одну бота для всех задач, 
# организовав меню и разнеся функционал по модулям.

## Задание повышенной сложности. 
# Добавить какую-нибудь перспективу к игре «Крестики-нолики»
##

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Привет {update.effective_user.first_name}! вот мой список команд:'
        f'\n/bin - форматирование в двоичный код числа \n'
        f'/fib - задать список чисел Негафибоначчи \n'
        f'/rle -  зашифровать код \n'
        f'/decod - расшифровка кода \n')


async def bin_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    num = int(input_num[1])
    print(num)
    bin_num = ''
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num = num // 2
    print(bin_num)
    await update.message.reply_text(f'число {input_num[1]} в двоичной системе: {bin_num}')


async def fib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    num = int(input_num[1])
    fib_list = [0] * (2 * num + 1)
    fib_list[num + 1], fib_list[num - 1] = 1, 1
    coef = -1
    for i in range(num + 2, 2 * num + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        fib_list[-i - 1] = fib_list[i] * coef
        coef *= -1
    print(fib_list)
    await update.message.reply_text(f'список чисел Негафибоначчи: {fib_list}')


async def rle_coding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print_data = update.message.text.split()
    data = print_data[1]
    code = ""
    symbol = ""
    for s in data:
        if symbol:
            if s in symbol and len(symbol) < 9:
                symbol += s
            else:
                code += str(len(symbol)) + symbol[0]
                symbol = s
        else:
            symbol = s
    code += str(len(symbol)) + symbol[0]
    print(data)
    await update.message.reply_text(f'зашифрованный код {code}')


async def decoding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    data = data[1]
    code = ""
    for i in range(0, len(data), 2):
        code += int(data[i]) * data[i + 1]
    await update.message.reply_text(f'раскодированный код {code}')

app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bin", bin_number))
app.add_handler(CommandHandler("fib", fib))
app.add_handler(CommandHandler("rle", rle_coding))
app.add_handler(CommandHandler("decod", decoding))

app.run_polling()