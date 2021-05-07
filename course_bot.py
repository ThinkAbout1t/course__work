import telebot
from telebot import types

bot = telebot.TeleBot('1794679515:AAG_8EIxUGAQA_5E2Jcvyyf_CpYQVnaqndw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Тест Роршаха')
    markup.add(btn1)
    send_mess = (f'<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЕсли хотите начать тест нажмите кнопку снизу')
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "тест роршаха":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Бабочки')
        btn2 = types.KeyboardButton('Моль')
        btn3 = types.KeyboardButton('Морда животного')
        btn4 = types.KeyboardButton('Летучая мышь')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/xrorschach_test_1.jpg.pagespeed.ic.giOoaM8WNN.webp')
        final_message = "Фото №1"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "бабочки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №2')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Бабочки символизируют переходный период, трансформацию, а также способность расти, изменяться и преодолевать препятствия.",reply_markup=markup)
    elif get_message_bot == "моль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №2')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Моль символизирует чувство недооцененности, недовольство собственной внешностью, а также слабость и раздражение.",reply_markup=markup)
    elif get_message_bot == "морда животного":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №2')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Морда животного, в частности слона, символизирует умение реагировать на проблемы, страх и нежелание заглянуть внутрь себя",reply_markup=markup)
    elif get_message_bot == "летучая мышь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №2')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Для кого-то летучая мышь означает что-то нечистое или демоническое, для кого-то — путь сквозь тьму и перерождение.",reply_markup=markup)

    elif get_message_bot == "фото №2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Две фигуры')
        btn2 = types.KeyboardButton('Человек который смотрит на себя в зеркало')
        btn3 = types.KeyboardButton('Собака')
        btn4 = types.KeyboardButton('Слон')
        btn5 = types.KeyboardButton('Медведь')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_2.jpg')
        final_message = "Фото №2"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "две фигуры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №3')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Две фигуры символизируют созависимость, одержимость сексом, неоднозначные чувства в отношении секса или зацикленность на отношениях.",reply_markup=markup)
    elif get_message_bot == "человек который смотрит на себя в зеркало":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №3')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Человек, который смотрит на себя в зеркало, символизирует эгоцентризм или самолюбование. Это может быть и отрицательная, и положительная черта, в зависимости от чувств человека.",reply_markup=markup)
    elif get_message_bot == "собака":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №3')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Собака символизирует преданного и верного друга. Если пациент увидел что-то негативное, это может свидетельствовать о необходимости осознать собственные страхи и чувства.",reply_markup=markup)
    elif get_message_bot == "слон":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №3')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Слон может символизировать глубокомыслие, память и ум, но также — отрицательное физическое самовосприятие.",reply_markup=markup)
    elif get_message_bot == "медведь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №3')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Медведь может символизировать агрессию, конкуренцию, независимость, восстановление, а также — чувство уязвимости, незащищенность или открытость и честность (игра слов по-английски: bear — медведь, bare — обнажать, обнаруживать, разоблачать).",reply_markup=markup)

    elif get_message_bot == "фото №3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Общая трапеза двух человек')
        btn2 = types.KeyboardButton('Двое людей которые моют руки')
        btn3 = types.KeyboardButton('Двое людей которые играют в игру')
        btn4 = types.KeyboardButton('Человек который смотрит в зеркало')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_3.jpg')
        final_message = "Фото №3"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "общая трапеза двух человек":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №4')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Если вы видите общую трапезу двух человек, это свидетельствует об активной общественной жизни",reply_markup=markup)
    elif get_message_bot == "двое людей которые моют руки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №4')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Если вы видите двух человек, моющих руки, вы можете чувствовать себя незащищенным или нечистым, а также страдать паранойей.",reply_markup=markup)
    elif get_message_bot == "двое людей которые играют в игру":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №4')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Если вы видите двух человек, играющих в определенную игру, вы подвержены конкуренции в социальном взаимодействии.",reply_markup=markup)
    elif get_message_bot == "человек который смотрит в зеркало":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №4')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Человек, который смотрит в зеркало, символизирует эгоцентризм, пренебрежение другими или несостоятельность воспринимать людей такими, какие они есть.",reply_markup=markup)

    elif get_message_bot == "фото №4":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Большое животное')
        btn2 = types.KeyboardButton('Монстр')
        btn3 = types.KeyboardButton('Шкура большого животного')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_4.jpg')
        final_message = "Фото №4"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "большое животное":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №5')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Большое животное может символизировать чувства неполноценности, сильный страх перед авторитетами или представителями власти, в частности перед отцом.",reply_markup=markup)
    elif get_message_bot == "монстр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №5')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Монстр может символизировать чувства неполноценности, сильный страх перед авторитетами или представителями власти, в частности перед отцом.",reply_markup=markup)
    elif get_message_bot == "шкура большого животного":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №5')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Шкура большого животного может символизировать существенный дискомфорт, связанный с темой отца. С другой стороны, она может свидетельствовать, что человек не имеет проблем с авторитетностью и неполноценностью.",reply_markup=markup)

    elif get_message_bot == "фото №5":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Летучая мышь или бабочка или моль')
        btn2 = types.KeyboardButton('Что-то другое')
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_5.jpg')
        final_message = "Фото №5"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "летучая мышь или бабочка или моль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №6')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Ассоциация, вызванная им, как и образ на первой карточке, отображает наше истинное «Я»",reply_markup=markup)
    elif get_message_bot == "что-то другое":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №6')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Если увиденный образ очень отличается от ответа, данного при виде первой карточки, это означает, что карточки со второй по четвертую, скорее всего, произвели на него большое впечатление.",reply_markup=markup)

    elif get_message_bot == "фото №6":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Кожа')
        btn2 = types.KeyboardButton('Нора')
        btn3 = types.KeyboardButton('Шкура животного')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_6.jpg')
        final_message = "Фото №6"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "кожа":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №7')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Кожа, может свидетельствовать о страхе перед близкими отношениями",reply_markup=markup)
    elif get_message_bot == "шкура животного":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №7')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Шкура животного, может свидетельствовать о страхе перед близкими отношениями",reply_markup=markup)
    elif get_message_bot == "нора":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №7')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Нора может указывать на нежелание вступать в близкие отношения с другими людьми и, как следствие, на ощущение внутренней пустоты и изолированности от общества.",reply_markup=markup)

    elif get_message_bot == "фото №7":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Головы женщин')
        btn2 = types.KeyboardButton('Головы детей')
        btn3 = types.KeyboardButton('Поцелуй')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_7.jpg')
        final_message = "Фото №7"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "головы женщин":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №8')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Головы женщин символизируют чувства человека, связанные с образом матери. Эти чувства влияют на отношение к лицам женского пола в целом.",reply_markup=markup)
    elif get_message_bot == "головы детей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №8')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Головы детей символизируют чувства, связанные с детством и необходимостью заботиться о внутреннем ребенке. Такое восприятие может также свидетельствовать о необходимости анализа и корректировки отношений человека с матерью.",reply_markup=markup)
    elif get_message_bot == "поцелуй":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №8')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Поцелуй символизирует стремление человека к любви и воссоединения с материнским образом. Это может свидетельствовать, что человек когда-то имел близкие отношения с матерью и теперь ищет этой близости в других отношениях — романтических или социальных.",reply_markup=markup)

    elif get_message_bot == "фото №8":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Затрудняетесь ответить или Вы испытываете дискомфорт')
        btn2 = types.KeyboardButton('Четырехлапое животное или бабочка или моль')
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_8.jpg')
        final_message = "Фото №8"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "затрудняетесь ответить или вы испытываете дискомфорт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №9')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Это может свидетельствовать о трудностях с реагированием на сложные ситуации или эмоциональные раздражители.",reply_markup=markup)
    elif get_message_bot == "четырехлапое животное или бабочка или моль":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №9')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Вы хорошо реагируете на сложные ситуации или эмоцианальные раздражители",reply_markup=markup)

    elif get_message_bot == "фото №9":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Человек')
        btn2 = types.KeyboardButton('Жуткая финура')
        markup.add(btn1, btn2)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_9.jpg')
        final_message = "Фото №9"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "человек":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №10')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Когда речь идет о человеке, свидетельствует о его умении справляться с бессистемностью времени и информации.",reply_markup=markup)
    elif get_message_bot == "жуткая финура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Фото №10')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Образ зла может свидетельствовать, что для внутреннего комфорта человеку нужна структурированность в жизни и он не терпит неопределенности.",reply_markup=markup)

    elif get_message_bot == "фото №10":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Краб')
        btn2 = types.KeyboardButton('Лобстер')
        btn3 = types.KeyboardButton('Паук')
        btn4 = types.KeyboardButton('Морда кролика')
        btn5 = types.KeyboardButton('Змеи')
        btn6 = types.KeyboardButton('Гусеницы')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_photo(message.chat.id, 'https://psyfactor.org/lib/i/rorschach_test_10.jpg')
        final_message = "Фото №10"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "краб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Краб может символизировать склонность к зацикливанию на определенных вещах или людях или свидетельствовать о назойливости человека.",reply_markup=markup)
    elif get_message_bot == "лобстер":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Лобстер может символизировать силу, настойчивость и умение справляться с незначительными проблемами. Лобстер может также свидетельствовать, что человек боится нанести себе вред или быть раненным другими.",reply_markup=markup)
    elif get_message_bot == "паук":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Паук может символизировать страх, ощущение запутанности или свидетельствовать, что человек оказался в неудобном положении из-за собственной лжи. Паук также символизирует властную мать и женскую силу.",reply_markup=markup)
    elif get_message_bot == "морда кролика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Морда кролика может символизировать плодородие и позитивное мышление.",reply_markup=markup)
    elif get_message_bot == "змеи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Змеи могут символизировать опасность. Человек, который видит змей, может чувствовать, что его обманывают или предают, а еще бояться неизвестного. ",reply_markup=markup)
    elif get_message_bot == "гусеницы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Начать тест заново')
        btn2 = types.KeyboardButton('Закончить тест')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,"Если человек видит гусениц на последней карте в тесте, это свидетельствует о перспективах развития и осознания того, что личность постоянно меняется и эволюционирует.",reply_markup=markup)

    elif get_message_bot == "начать тест заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('тест роршаха')
        markup.add(btn1)
        final_message = "Решил попробовать опять?"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    # Здесь различные дополнительные проверки и условия

    elif get_message_bot == "закончить тест":
        final_message = "Спасибо за прохождение"
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Тест Роршаха')
        markup.add(btn1)
        final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)