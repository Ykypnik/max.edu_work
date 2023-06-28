import telebot
from token_bot import token

bot = telebot.TeleBot(token)

ban_list = []

number_buy = 0

admin_chatid = [1228391412, 1060339789]


@bot.message_handler(commands=['start'])
def greeting(message):
    if str(message.chat.id) not in ban_list:
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        button_sub = telebot.types.InlineKeyboardButton('ПОДПИСАТЬСЯ!', url='https://t.me/Cashmean_Uc_Shop')
        kb.add(button_sub)

        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
        button_product = telebot.types.KeyboardButton('Товары📦')
        button_contacts = telebot.types.KeyboardButton('📇Контакты')
        button_profile = telebot.types.KeyboardButton('Профиль')
        button_otzivi = telebot.types.KeyboardButton('Отзывы')
        keyboard.add(button_profile, button_product)
        keyboard.add(button_otzivi, button_contacts)
        welcome_text = 'Спасибо что выбрали нас! 🔥'
        bot.send_message(message.chat.id, text=welcome_text, reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Советуем подписаться на наш канал', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def answer(message):
    if str(message.chat.id) not in ban_list:


        if message.text == 'Профиль':
            user_id = message.from_user.id
            user_profile = '''
        👤 Мой профиль

Мой ID:''' + str(user_id)
            bot.send_message(message.chat.id, user_profile)


        if message.text == 'Отзывы':
            kb = telebot.types.InlineKeyboardMarkup(row_width=1)
            otzivi = telebot.types.InlineKeyboardButton('Отзывы здесь!', url='https://t.me/otzivi_cashmeam_Uc')
            kb.add(otzivi)

            bot.send_message(message.chat.id, text='''
            Перейдя по ссылке в наш канал с отзывами вы точно убедитесь! 🤝''', reply_markup=kb)


        if message.text == '📇Контакты':
            kb = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_otzivi = telebot.types.InlineKeyboardButton('Чат для общения!', url='https://t.me/chat_Cashmeam_Uc')
            kb.add(button_otzivi)
            contacts = '''
        👤 Администратор: @cashmeam
( с 8:00 до 24:00 МСК)'''
            bot.send_message(message.chat.id, contacts, reply_markup=kb)


        if message.text == 'Товары📦':
            kb = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_uc = telebot.types.InlineKeyboardButton('⭐️UC⭐️', callback_data='uc')
            kb.add(button_uc)
            bot.send_message(message.chat.id, '''📦Товары''', reply_markup=kb)


        if message.text == 'Главное Меню↩️':
            keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
            button_product = telebot.types.KeyboardButton('Товары📦')
            button_contacts = telebot.types.KeyboardButton('📇Контакты')
            button_profile = telebot.types.KeyboardButton('Профиль')
            button_otzivi = telebot.types.KeyboardButton('Отзывы')
            keyboard.add(button_profile, button_product)
            keyboard.add(button_otzivi, button_contacts)
            welcome_text = '🏠'
            bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


def handler_photo():
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        global number_buy
        number_buy += 1
        file_info = bot.get_file(message.photo[-1].file_id)
        photo_check = bot.download_file(file_info.file_path)

        kb = telebot.types.InlineKeyboardMarkup(row_width=2)
        agree_but = telebot.types.InlineKeyboardButton('Подтвердить', callback_data='ok')
        ban_button = telebot.types.InlineKeyboardButton('Бан', callback_data='ban')
        kb.add(agree_but, ban_button)

        bot.send_photo(1060339789, photo_check, caption='Номер заказа#' + str(number_buy), reply_markup=kb)
        bot.send_photo(1228391412, photo_check, caption='Номер заказа#' + str(number_buy), reply_markup=kb)

        send = bot.send_message(message.chat.id, 'Отправьте ваш игровой айди от Pubg Mobile')
        bot.register_next_step_handler(send, get_pubg_id)


def get_pubg_id(message):
    pubg_id = message.text
    bot.send_message(1060339789, 'Пабг 🆔: ' + f'<code>{pubg_id}</code>' + '\n' + 'Chat 🆔: ' +
                     f'<code>{message.chat.id}</code>' + '\n' + ' Номер заказа#' + str(number_buy),
                     parse_mode='html')
    bot.send_message(1228391412, 'Пабг 🆔: ' + f'<code>{pubg_id}</code>' + '\n' + 'Chat 🆔: ' +
                     f'<code>{message.chat.id}</code>' + '\n' + ' Номер заказа#' + str(number_buy),
                     parse_mode='html')
    bot.send_message(message.chat.id, '👌Всё ОК👌, ждите пополнения! Бот вам напишет')


@bot.callback_query_handler(func=lambda call: True)
def inline_handler(call):
    if str(call.message.chat.id) not in ban_list:
        if call.message:

            def pay():
                kb = telebot.types.InlineKeyboardMarkup(row_width=1)
                sberbank = telebot.types.InlineKeyboardButton('СберБанк🟢', callback_data='sber')
                kiwi = telebot.types.InlineKeyboardButton('Qiwi🟠', callback_data='qiwi')
                kb.add(sberbank, kiwi)
                return kb


            if call.data == 'uc':
                kb = telebot.types.InlineKeyboardMarkup(row_width=2)
                price60 = telebot.types.InlineKeyboardButton('⚡60 UC — 75₽⚡', callback_data='60')
                price325 = telebot.types.InlineKeyboardButton('⚡️325 UC — 370₽⚡️', callback_data='325')
                price385 = telebot.types.InlineKeyboardButton('⚡️385 UC — 420₽⚡️', callback_data='385')
                price660 = telebot.types.InlineKeyboardButton('⚡️660 UC — 710₽⚡️', callback_data='660')
                price985 = telebot.types.InlineKeyboardButton('⚡️985 UC — 1150₽⚡️', callback_data='985')
                price1800 = telebot.types.InlineKeyboardButton('⚡️1800 UC — 1750₽⚡️', callback_data='1800')
                price2460 = telebot.types.InlineKeyboardButton('⚡2460 UC — 2500₽⚡', callback_data='2460')
                price3850 = telebot.types.InlineKeyboardButton('⚡️3850 UC — 3450₽⚡️', callback_data='3850')
                price5650 = telebot.types.InlineKeyboardButton('⚡5650 UC — 5150₽⚡', callback_data='5650')
                price8100 = telebot.types.InlineKeyboardButton('⚡️8100 UC — 6850₽⚡️', callback_data='8100')
                main_menu = telebot.types.InlineKeyboardButton('Назад↩️', callback_data='back_menu')
                kb.add(price60, price325, price385, price660, price985,
                            price1800, price2460, price3850, price5650, price8100, main_menu)
                uc_text = 'Товары📦 › ⭐️UC⭐️'
                bot.edit_message_text(chat_id=call.message.chat.id, text=uc_text, message_id=call.message.id, reply_markup=kb)


            if call.data == 'back_menu':
                kb = telebot.types.InlineKeyboardMarkup(row_width=1)
                button_uc = telebot.types.InlineKeyboardButton('⭐️UC⭐️', callback_data='uc')
                kb.add(button_uc)
                bot.edit_message_text(chat_id=call.message.chat.id, text='''📦Товары''', reply_markup=kb, message_id=call.message.id)


            if call.data == '325':
                inf_prod = '''💰325 UC💰

Цена: 370 рублей

     ⭐️ Без бана
     ⭐️ Без передачи аккаунта
     ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '60':
                inf_prod = '''💰60 UC💰

Цена: 75 рублей

     ⭐️ Без бана
     ⭐️ Без передачи аккаунта
     ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '385':
                inf_prod = '''💰385 UC💰

Цена: 420 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '660':
                inf_prod = '''💰660 UC💰

Цена: 710 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '985':
                inf_prod = '''💰985 UC💰

Цена: 1150 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '1800':
                inf_prod = '''💰1800 UC💰

Цена: 1750 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '2460':
                inf_prod = '''💰2460 UC💰

Цена: 2500 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '3850':
                inf_prod = '''💰3850 UC💰

Цена: 3450 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '5650':
                inf_prod = '''💰5650 UC💰

Цена: 5150 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == '8100':
                inf_prod = '''💰8100 UC💰

Цена: 6850 рублей

        ⭐️ Без бана
        ⭐️ Без передачи аккаунта
        ⭐️ Легальный способ пополнения UC

Выберите удобный способ оплаты:'''
                kb = pay()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=inf_prod,
                                      reply_markup=kb)


            if call.data == 'sber':
                sber1 = '''
                💳КАРТА СБЕРБАНК ✨
Так же можно по СБП 💸\n\n'''

                sber2 = '''
                \nПолучатель : Владислав З.✋
После оплаты жду чек, где видно ФИО отправителя
И игровое ID 
  Айди СТРОГО после чека!'''
                bot.edit_message_text(chat_id=call.message.chat.id, text=sber1 + f'<code>{2202206191495352}</code>' + sber2,
                                      message_id=call.message.id, parse_mode='html')
                bot.send_message(call.message.chat.id, '❗ Мы не несем ответственность если вы перевели деньги не туда.')
                handler_photo()


            if call.data == 'qiwi':
                kb = telebot.types.InlineKeyboardMarkup()
                pay_qiwi = telebot.types.InlineKeyboardButton('Быстрая оплата', url='https://qiwi.com/n/IAGEI')
                kb.add(pay_qiwi)
                qiwi = '''
            Qiwi🟠
Номер карты: '''
                bot.edit_message_text(chat_id=call.message.chat.id, text=qiwi + f'<code>{4890494785500406}</code>',
                                 message_id=call.message.id, parse_mode='html', reply_markup=kb)
                bot.send_message(call.message.chat.id, 'Ожидаю скриншот перевода. Также буду рад чаевым 💫')
                bot.send_message(call.message.chat.id, '❗ Мы не несем ответственность если вы перевели деньги не туда.')
                handler_photo()


            if call.data == 'ban':
                send_ban = bot.send_message(call.message.chat.id, 'Жду chat id для бана😈')
                bot.register_next_step_handler(send_ban, bannan)


            if call.data == 'ok':
                send = bot.send_message(call.message.chat.id, 'Жду chat id⏳')
                bot.register_next_step_handler(send, handler_id)


def bannan(message):
    if message.text != '1060339789':
        try:
            ban_id = message.text
            ban_list.append(ban_id)
            bot.send_message(ban_id, 'НА БОТ! НА БАН!')
            bot.send_message(message.chat.id, 'ЗАБАНЕН🤪')
            print(ban_list)
        except:
            bot.send_message(message.chat.id, 'Не получилось отправить сообщение! Вроде айди не тот😬')
    else:
        bot.send_message(message.chat.id, 'Таких уважаемых людей нельзя банить')


def handler_id(message):
    try:
        chat_id = message.text
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        otzivi = telebot.types.InlineKeyboardButton('Отзывы', url='https://t.me/otzivi_cashmeam_Uc')
        kb.add(otzivi)
        bot.send_message(chat_id, '''Товар успешно выдан✅
Спасибо за покупку!♥️
Оставить отзыв:''', reply_markup=kb)
        bot.send_message(message.chat.id, 'Сообщение отправлено успешно😎😎😎')
    except:
        bot.send_message(message.chat.id, 'Не получилось отправить сообщение! Вроде айди не тот😬')


bot.polling(none_stop=True, timeout=120)