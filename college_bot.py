import telebot
from telebot import types
bot = telebot.TeleBot("")

# Обработка команды для старта
@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
    types.InlineKeyboardButton(text='👩‍🎓 Абитуриенту', callback_data='admission'),
    types.InlineKeyboardButton(text='📒 Наши проекты', callback_data='projects'),
    types.InlineKeyboardButton(text='📢 Новости', callback_data='news'),
    types.InlineKeyboardButton(text='🏺 Виртуальный музей', callback_data='museum'),
    types.InlineKeyboardButton(text='✨ О колледже', callback_data='about_us'),
    types.InlineKeyboardButton(text='☎️ Контакты', callback_data='contacts'),
    types.InlineKeyboardButton(text='📮 Оставить сообщение', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=1081')
    ]
    keyboard.add(*buttons)
    bot.send_photo(message.chat.id, photo=open('D:\DS/projects/college_bot/img/banner.png', 'rb'))
    bot.send_message(message.chat.id,"Добро пожаловать, <b>{0.first_name}</b>! Я - <b>{1.first_name}</b>, "
                                     "бот Минского городского педагогического колледжа."
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)


# Обработка команды для выхода
@bot.message_handler(commands=['stop'])
def bye(message):
    bot.send_message(message.chat.id, 'Досвидания'.format(message.from_user, bot.get_me()), parse_mode='html')
    exit()

# Повторный вызов главного меню
@bot.callback_query_handler(func=lambda call: call.data in ['main_page'])
def callback_inline_main_page(call):
    if call.message:
        if call.data == 'main_page':
            bot.send_message(call.message.chat.id, '/main_page', parse_mode="html")

@bot.message_handler(commands=['main_page'])
def main_page(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
    types.InlineKeyboardButton(text='👩‍🎓 Абитуриенту', callback_data='admission'),
    types.InlineKeyboardButton(text='📒 Наши проекты', callback_data='projects'),
    types.InlineKeyboardButton(text='📢 Новости', callback_data='news'),
    types.InlineKeyboardButton(text='🏺 Виртуальный музей', callback_data='museum'),
    types.InlineKeyboardButton(text='✨ О колледже', callback_data='about_us'),
    types.InlineKeyboardButton(text='☎️ Контакты', callback_data='contacts'),
    types.InlineKeyboardButton(text='📮 Оставить сообщение', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=1081')
    ]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,"Главная страница"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)


# Работа кнопок главного меню
@bot.callback_query_handler(func=lambda call: call.data in ['admission', 'projects', 'news', 'museum', 'about_us', 'contacts'])
def callback_inline_main_page(call):
    if call.message:
        if call.data == 'admission':
            admission_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="👩‍🏫 Специальности", callback_data='specialties'),
            types.InlineKeyboardButton(text="📅 Сроки проведения вступительной кампании", callback_data='terms'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            admission_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '👩‍🎓 Информация для абитуриентов:', parse_mode="html", reply_markup=admission_keybord)

        elif call.data == 'projects':
            projects_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="🔸 Читательский видео-марафон, посвящённый Году народного единства", callback_data='marathon_1'),
            types.InlineKeyboardButton(text="🔸 Конкурс цифровых образовательных ресурсов «ПрофStart»", callback_data='profstart'),
            types.InlineKeyboardButton(text="🔸  IV Педагогические чтения «Среднее специальное педагогическое образование: традиции и инновации»",
                                                           callback_data='conf'),
            types.InlineKeyboardButton(text="🔸 Читательский видео-марафон «Великой Победе - 75!»",
                                                           callback_data='marathon_2'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            projects_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '📒 Наши проекты:', parse_mode="html", reply_markup=projects_keybord)

        elif call.data == 'news':
            news_keybord = types.InlineKeyboardMarkup(row_width=1)

            buttons = [
            types.InlineKeyboardButton(text="🔥 Последние новости", url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=1031'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            news_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '📢 Новости учреждения:', parse_mode="html", reply_markup=news_keybord)

        elif call.data == 'museum':
            museum_keybord = types.InlineKeyboardMarkup(row_width=2)
            buttons = [
            types.InlineKeyboardButton(text="🔹 Из истории профессионального педагогического образования г. Минска", callback_data='history_minsk'),
            types.InlineKeyboardButton(text="🔹 Колледж сегодня", callback_data='college_today'),
            types.InlineKeyboardButton(text="🔹 Учащиеся изучают историю колледжа", callback_data='college_history'),
            types.InlineKeyboardButton(text="🔹 Наши достижения", callback_data='achievements'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            museum_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '🏺 Виртуальный музей Минского городского педагогического колледжа:', parse_mode="html", reply_markup=museum_keybord)

        elif call.data == 'about_us':
            about_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="🏛️ Администрация", url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=1261'),
            types.InlineKeyboardButton(text="✒️ О нас пишут СМИ", url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=3781'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            about_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '✨ О колледже:', parse_mode="html")
            bot.send_message(call.message.chat.id, 'Учреждение создано на основании решения Минского городского исполнительного комитета № 632 от 10 марта 2016 г. '
                                                   '«О создании государственного учреждения образования» как учреждение образования в системе среднего специального '
                                                   'образования и обеспечивает получение общего среднего и среднего специального образования.',
                             parse_mode="html", reply_markup=about_keybord)

        elif call.data == 'contacts':
            bot.send_message(call.message.chat.id, '<b>Наши контакты:</b>', parse_mode="html")
            bot.send_message(call.message.chat.id, '<b>Почтовый адрес:</b> 220114, г. Минск, ул. Макаенка, 29.\n'
                                                   '<b>Телефон:</b> +375 17 373-15-90, +375 17 257 64 50\n'
                                                   '<b>Адрес электронной почты:</b> pedkol@minsk.edu.by', parse_mode="html")
            contacts_keyboard = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            contacts_keyboard.add(*buttons)
            bot.send_location(call.message.chat.id, 53.916207, 27.619692, reply_markup=contacts_keyboard)

# Работа кнопок раздела "Информация для абитуриентов"
@bot.callback_query_handler(func=lambda call: call.data in ['specialties', 'terms', 'preschool_education', 'primary_education'])
def callback_inline_admission(call):
    if call.message:
        if call.data == 'specialties':
            specialties_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="💠 Дошкольное образование", callback_data='preschool_education'),
            types.InlineKeyboardButton(text="💠 Начальное образование", callback_data='primary_education'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')]
            specialties_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '👩‍🏫 Специальности:', parse_mode="html", reply_markup=specialties_keybord)

        elif call.data == 'terms':
            terms_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            terms_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, 'Сроки проведения вступительной кампании в государственном учреждении образования '
                                                   '«Минский городской педагогический колледж» в 2021 году', parse_mode="html")
            bot.send_photo(call.message.chat.id, photo=open('D:\DS/projects/college_bot/img/terms.PNG', 'rb'), reply_markup=terms_keybord)

        elif call.data == 'preschool_education':
            preschool_education_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="ℹ️  Подробнее на сайте колледжа", url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=3381'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            preschool_education_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '<b>Квалификация:</b>\nВоспитатель дошкольного образования\n'
                                                   '<b>Срок получения образования:</b>\n2 года 10 месяцев на основе общего базового образования (9 классов) в дневной форме;\n'
                                                   '2 г. 10 мес. на основе общего среднего образования (11 классов) (заочная форма получения образования – платно)\n'
                                                   '<b>Сферой профессиональной деятельности воспитателя дошкольного образования является:</b>\n'
                                                   'педагогическое взаимодействие с воспитанниками, его родителями, другими педагогами, направленное на'
                                                   ' разностороннее развитие личности ребенка в соответствии с его возрастными и индивидуальными возможностями, '
                                                   'способностями и потребностями при реализации учебной программы дошкольного образования',
                             parse_mode="html", reply_markup=preschool_education_keybord)

        elif call.data == 'primary_education':
            primary_education_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text="ℹ️  Подробнее на сайте колледжа",
                                                                      url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=3391'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            primary_education_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '<b>Квалификация:</b>\nУчитель\n'
                                                   '<b>Срок получения образования:</b>\n2 года 10 месяцев на основе общего базового образования в дневной форме\n'
                                                   '<b>Сферой профессиональной деятельности учителя</b> является образовательная деятельность в учреждении общего среднего образования.',
                             parse_mode="html", reply_markup=primary_education_keybord)

# Работа кнопок раздела "Наши проекты"
@bot.callback_query_handler(func=lambda call: call.data in ['marathon_1', 'profstart', 'conf', 'marathon_2'])
def callback_inline_admission(call):
    if call.message:
        if call.data == 'marathon_1':
            marathon_1_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4081'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            marathon_1_keybord.add(*buttons)

            bot.send_message(call.message.chat.id, '24 мая 2021 года стартует читательский видео-марафон, посвящённый Году народного единства. '
                                                   'Для участия в марафоне поданы заявки от учреждений образования Республики Беларусь.',
                             parse_mode="html", reply_markup=marathon_1_keybord)

        elif call.data == 'profstart':
            profstart_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4081'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            profstart_keybord.add(*buttons)

            bot.send_message(call.message.chat.id, 'С 20 февраля по 23 марта 2021 года с целью формирования профессиональных '
                                                   'компетенций будущих воспитателей дошкольного образования, учителей начальных '
                                                   'классов в процессе разработки цифровых образовательных ресурсов для '
                                                   'применения в педагогической деятельности с детьми дошкольного и '
                                                   'младшего школьного возраста проходит конкурс цифровых '
                                                   'образовательных ресурсов <b>«ПрофStart»</b> (с международным участием). '
                                                   'Организатором конкурса выступает Государственное учреждение образования '
                                                   '«Минский городской педагогический колледж».',
                             parse_mode="html", reply_markup=profstart_keybord)

        elif call.data == 'conf':
            conf_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4081'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            conf_keybord.add(*buttons)

            bot.send_message(call.message.chat.id, 'Комитет по образованию Мингорисполкома, государственное учреждение '
                                                   '«Национальная библиотека Беларуси», государственное учреждение образования '
                                                   '«Минский городской педагогический колледж» приглашают вас принять '
                                                   'участие в IV Педагогических чтениях (с международным участием) '
                                                   '«Среднее специальное педагогическое образование: традиции и инновации», '
                                                   'посвящённых Году народного единства.\nКонференция состоится 25 марта '
                                                   '2021 года в государственном учреждении «Национальная библиотека Беларуси» '
                                                   '(г.Минск, пр.Независимости, 116), государственном учреждении образования '
                                                   '«Минский городской педагогический колледж» (г. Минск, ул. Макаёнка, 29).',
                             parse_mode="html", reply_markup=conf_keybord)

        elif call.data == 'marathon_2':
            marathon_2_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4081'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            marathon_2_keybord.add(*buttons)

            bot.send_message(call.message.chat.id, '<b>7 мая 2020 года стартует читательский видео-марафон «Великой Победе - 75!».</b>\n'
                                                   'Для участия в марафоне поданы заявки от учреждений образования Республики Беларусь, '
                                                   'Российской Федерации и Республики Казахстан!',
                             parse_mode="html", reply_markup=marathon_2_keybord)


# Работа кнопок раздела "Виртуальный музей"
@bot.callback_query_handler(func=lambda call: call.data in ['history_minsk', 'college_today', 'college_history', 'achievements'])
def callback_inline_admission(call):
    if call.message:
        if call.data == 'history_minsk':
            history_minsk_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=3351'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            history_minsk_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, '<b>Минский Белорусский педагогический техникум</b>\nВ начале 1921/1922 '
                                                   'учебного года в Минске был закрыт Институт народного образования. '
                                                   'На его базе были созданы педагогическое отделение при факультете гражданских '
                                                   'наук Белорусского государственного университета, а также Минский '
                                                   'Белорусский педагогический техникум (Белпедтехникум), которому '
                                                   'перешло здание на ул. Захарьевской (с 1922 г. – ул. Советская; '
                                                   'здание пережило войну, но было снесено в послевоенные годы при '
                                                   'расширении ул. Советской – нынешнего пр. Независимости; библиотека '
                                                   '(насчитывала примерно 10000 книг), кабинеты (в том числе лучший в '
                                                   'г.Минске кабинет физики) Института народного образования. '
                                                   'Занятия в техникуме начались 1 октября 1921 г.',
                             parse_mode="html")
            bot.send_photo(call.message.chat.id, photo=open('D:\DS/projects/college_bot/img/building.jpg', 'rb'))
            bot.send_message(call.message.chat.id, '<i>Минский Белорусский педагогический техникум (Белпедтехникум) имени В.М. Игнатовского</i>',
                             parse_mode="html", reply_markup=history_minsk_keybord)

        elif call.data == 'college_today':
            college_today_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4111'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            college_today_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, 'Колледж сегодня - это коллектив профессионалов, благодаря работе которых '
                                                   'можно уверенно сказать, что будущие воспитатели дошкольного образования '
                                                   'и учителя начальной школы смогут научить и воспитать достойных граждан Республики Беларусь.',
                             parse_mode="html")
            bot.send_photo(call.message.chat.id, photo=open('D:\DS/projects/college_bot/img/diplom.jpg', 'rb'))
            bot.send_message(call.message.chat.id,
                             '<i>Лучшее учреждение среднего специального образования г.Минска 2020 года!</i>',
                             parse_mode="html", reply_markup=college_today_keybord)


        elif call.data == 'college_history':
            college_history_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4131'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            college_history_keybord.add(*buttons)
            bot.send_message(call.message.chat.id, 'Учащиеся Минского городского педагогического колледжа активно включены '
                                                   'в научно-исследовательскую работу, принимают участие в конкурсах и '
                                                   'конференциях. Изучение истории педагогического образования, '
                                                   'деятельность отечественных педагогов - одно из приоритетных направлений '
                                                   'их научной деятельности, ведь без знаний об истории педагогики и '
                                                   'профессиональном пути отечественных педагогов тяжело достичь новых высот в выбранной профессии.',
                             parse_mode="html", reply_markup=college_history_keybord)

        elif call.data == 'achievements':
            achievements_keybord = types.InlineKeyboardMarkup(row_width=1)
            buttons = [
            types.InlineKeyboardButton(text='ℹ️  Подробнее на сайте колледжа', url='http://pedkol.minsk.edu.by/ru/main.aspx?guid=4121'),
            types.InlineKeyboardButton(text="🏠 На главную", callback_data='main_page')
            ]
            achievements_keybord.add(*buttons)

            bot.send_message(call.message.chat.id, 'Несмотря на молодой возраст Минского городского педагогического колледжа, '
                                                   'его коллектив неоднократно подтвердил свою компетентность и профессионализм, завоевав ряд престижных наград.',
                             parse_mode="html", reply_markup=achievements_keybord)

bot.polling(none_stop=True, interval=0)
