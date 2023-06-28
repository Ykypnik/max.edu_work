import telebot
from telebot import types
from so2_bottoken import token

bot = telebot.TeleBot(token)

ban_list = []

@bot.message_handler(commands=['start'])
def hello_bot(message):
    if message.chat.id not in ban_list:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        profile_but = types.KeyboardButton('📥Профиль')
        buy_but = types.KeyboardButton('🍯 Купить голду')
        account_but = types.KeyboardButton('🕹 Аккаунты')
        support_but = types.KeyboardButton('🧑‍💻 Поддержка')
        keyboard.add(profile_but, buy_but, account_but, support_but)
        text_hello = '''▶️ Для продолжения выбери нужную команду на клавиатуре 👇
🙋‍♂️ Если есть дополнительные вопросы по поводу бота, обратитесь в Поддержку
📊Курс: 70₽ — 100G'''
        bot.send_message(message.chat.id, text_hello, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def button_handler(message):
    if message.chat.id not in ban_list:
        if message.text == '📥Профиль':
            profile_text = f'''📋 Краткая информация о вашем аккаунте:

Имя: <code>{message.from_user.first_name}</code>
UID: <code>{message.chat.id}</code>'''
            bot.send_message(message.chat.id, profile_text, parse_mode='html')

        if message.text == '🕹 Аккаунты':
            bot.send_message(message.chat.id, 'Упс, похоже здесь пусто 🥱')

        if message.text == '🍯 Купить голду':
            questions = bot.send_message(message.chat.id, 'Введите сумму, на которую желаете приобрести голду🥇')
            bot.register_next_step_handler(questions, kapusta)


def kapusta(message):
    try:
        if int(message.text) >= 70:
            money = int(message.text)
            gold = money // 0.7
            bot.send_message(message.chat.id, f'''💸 За {money} рублей вы сможете купить {gold} золота

🖋 Выберите наиболее удобный для вас способ оплаты

📩 СберБанк реквизиты:
💳 По номеру карты: 2202206191495352

📩 QIWI реквизиты:
💳 По номеру карты: 4890494785500406

📷 Отправьте нам скриншот чека.''')

            @func_decorator
            def
        else:
            bot.send_message(message.chat.id, '⚠️ Минимальная сумма для пополнения 70 рублей')
    except:
        bot.send_message(message.chat.id, '❗️ Введите целое число.')


def func_decorator(func):
    @bot.message_handler(content_types=['photo'])
    def handler_photo(message):
        file_info = bot.get_file(message.photo[-1].file_id)
        photo_check = bot.download_file(file_info.file_path)
        chat_id = message.chat.id
        func(photo_check, chat_id)
    return handler_photo


bot.polling()