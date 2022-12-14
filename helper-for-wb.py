from gtts import gTTS
import time
import playsound
import speech_recognition as sr
import pyperclip
import os
import pyautogui
sr.pause_threshold = 0.5

def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language='ru')
        print('Вы сказали: '+our_speech)
        return our_speech

    except sr.UnknownValueError:
        return 'ошибка'
    except sr.RequestError as e:
        return 'ошибка'
    #return input("Скажите вашу команду: ")

pyautogui.PAUSE = 0.5

def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет, Дима!")
    elif "баланс" in message:
        pyperclip.copy("Денежные средства были отправлены на баланс, чтобы у Вас была возможность оплачивать товары сразу с баланса Личного Кабинета, но также Вы можете выводить средства на карту по реквизитам. ")
        say_message("хорошо")
    elif "задержка" in message:
        pyperclip.copy("Мы ранее действительно зафиксировали задержку заказа. На данный момент мы оформили отдельный внутренний запрос по доставке товара и в ближайшее время мы предоставим Вам ответ с разъяснением в каком статусе товар, когда он поступит в пункт выдачи или порекомендуем сделать отмену заказа. Как только запрос будет решен, Вам поступит ответ на Вашу электронную почту, указанную в Личном кабинете. Приносим извинения за сложившуюся ситуацию.")
        say_message("хорошо")
    elif "оформлен" in message:
        pyperclip.copy("Понимаю, что Вы очень ждете этот товар и рассчитывали на конкретные сроки. Ваш товар пока еще не был отправлен продавцом. Мы предпринимаем все необходимые меры, чтобы заказ был отправлен. Приносим Вам свои извинения за задержку товара. Также если ожидание доставки станет не актуальным, либо товары будут в таком статусе продолжительное время, Вы сможете отменить ее в Личном кабинете в разделе «Покупки/Доставки». Деньги после отмены вернутся Вам  в полном объеме на счёт оплаты. Кнопка отмены заказа станет доступна на 6-й день задержки с первой даты интервала доставки.")
        say_message("хорошо")
    elif "файл" in message:
        pyperclip.copy("Передал информацию сотрудникам. Данный товар будет отменен. Это может занять некоторое время. Пожалуйста, ожидайте. Приносим свои извинения за данную ситуацию.")
        say_message("хорошо")
    elif "деньги" in message:
        pyperclip.copy("Мы ранее действительно зафиксировали возврат денежных средств. На данный момент мы оформили отдельный внутренний запрос по возврату денежных средств и в ближайшее время мы предоставим Вам номер транзакции для возврата денежных средств в полном объёме на счёт, с которого ранее была произведена оплата данного заказа. Как только возврат средств будет произведен, Вам поступит ответ на Вашу электронную почту, указанную в Личном кабинете. Приносим извинения за сложившуюся ситуацию.")
        say_message("хорошо")
    elif "100 руб" in message:
        pyperclip.copy("Ваши денежные средства в размере 100 руб. отправлены и будут зачислены на счет, с которого производилась оплата, срок перечисления составляет в среднем 1-5 дней, но может занимать до 10 календарных дней. Просим ожидать зачисления денежных средств.")
        say_message("хорошо")
    elif "выписка" in message:
        pyperclip.copy("По нашей информации данный товар был с оплатой при получении, поэтому возврата денежных средств не осуществлялось. Если списание 1199 руб. за этот товар было, отправьте пожалуйста выписку с банка, где показано что списание прошло успешно в WB чат. После этого мы будем решать этот вопрос.")
        say_message("хорошо")
    elif "бабло" in message:
        pyperclip.copy("Ваши денежные средства в размере 2409р были перечислены на ваш счет 10.07.22.")
        say_message("хорошо")
    elif "рн" in message:
        pyperclip.copy("Денежные средства в размере 143р были перечислены на ваш счет 12.07.22 на карту номер **2619\nИдентификационный номер возврата 308097465231.\nС этими данными Вы сможете обратиться в банк для уточнения информации по зачислению.")
        say_message("хорошо")
    elif "понимаю" in message:
        pyperclip.copy("Понимаю, что Вы очень ждете этот товар и рассчитывали на конкретные сроки. Ваш товар из-за большого объема заказов задержался на одном из этапов доставки дольше запланированного. Мы предпринимаем все необходимые меры, чтобы заказ поступил как можно быстрее (по точной дате доставке я Вас сориентировать пока не могу). Приносим Вам свои извинения за задержку товара. Также если ожидание доставки станет не актуальным, Вы сможете отменить  ее в Личном кабинете в разделе «Покупки/Доставки». Деньги после отмены вернутся Вам  в полном объеме на счёт оплаты. Кнопка отмены заказа станет доступна на 6-й день задержки с первой даты интервала доставки.")
        say_message("хорошо")
    elif "брак" in message:
        pyperclip.copy("Для того, чтобы вернуть денежные средства по браку или несоответствию, необходимо оформить заявку в Личном кабинете в разделе 'Проверка товара' вкладка 'Возврат товара по браку после оплаты'. Там Вам надо будет указать фото и видео с дефектом. Если ваша заявка удовлетворится, Ваши средства будут возвращены. Результат рассмотрения Вы всегда можете увидеть в личном кабинете в разделе 'Проверка товара'. ")
        say_message("хорошо")
    elif "сроки доставки" in message:
        pyperclip.copy("Ваш товар с артикулом 26402928 находится в пути в Ваш пункт самовывоза. Отслеживать информацию о передвижении товара Вы можете в разделе 'Доставка'. Информация может отображаться с небольшой задержкой. Ориентировочная дата доставки с 10.08.2022 по 12.08.2022. Пожалуйста, ожидайте доставку. Мы делаем всё возможное чтобы Ваш товар пришел к Вам как можно скорее. ")
        say_message("хорошо")
    elif "данные" in message:
        pyperclip.copy("Для решения Вашего вопроса, укажите, пожалуйста, следующие данные: \n- Ваш банк и платежную систему. \n- Какое устройство Вы использовали (если телефон, то версию ОС) \n- Какую площадку Вы использовали. \n- На каком этапе возникает проблема. \n- Код ошибки (если есть).  \nДанную информацию Вы можете указать в новом обращении.")
        say_message("хорошо")
    elif "артикул" in message:
        pyperclip.copy("Для решения Вашего вопроса укажите, пожалуйста, артикул товара в новом обращении.\nАртикул товара Вы можете посмотреть в карточке товара.")
        say_message("хорошо")
    elif "отмена" in message:
        pyperclip.copy("Отмена заказа в личном кабинете в разделе 'Доставка' возможна только в течение 10 минут с момента его оформления или в случае задержки поступления на 6-й день с первой ориентировочной даты доставки. Отказаться от неактуальных товаров Вы также сможете при их получении в Вашем пункте самовывоза. При отказе от товаров при получении необходимо назвать трёхзначный код, который отображается в разделе личного кабинета 'Доставка'. ")
        say_message("хорошо")
    elif "постоплата 2" in message:
        pyperclip.copy("Заказ оформлен с оплатой при получении. Товары Вы сможете оплатить при получении на пункте выдачи.")
        say_message("хорошо")
    elif "постоплата 1" in message:
        pyperclip.copy("Способы оплаты системой определяются автоматически, они могут регулярно меняться у каждого клиента, чаще совершайте покупки и Вам станет доступно больше привилегий в нашем маркетплейсе, мы ценим наших постоянных клиентов. Постоплата или оплата при получении это акция которая доступна не всем клиентам.")
        say_message("хорошо")
    elif "сбой" in message:
        pyperclip.copy("Ранее процент выкупа был изображен не корректно. В данный момент ошибка была устранена и процент выкупа обновился, теперь все данные корректны.")
        say_message("хорошо")
    elif "регистрация 3" in message:
        pyperclip.copy("Сообщил клиенту информацию по его вопросу")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(484,767)#- координаты кнопки "Зарегистрировать"
        say_message("хорошо")
    elif "регистрация 1" in message:
        pyautogui.click(167,662)#- координаты кнопки "Заказ"
        pyautogui.PAUSE = 0.2
        pyautogui.click(238,495)#- координаты кнопки "Активные доставки"
        pyautogui.PAUSE = 0.5
        pyautogui.click(1317,840)#- координаты кнопки "Регистрация обращения"
        pyautogui.PAUSE = 0.5
        pyautogui.click(666,311)#- координаты кнопки "Источник - Обращение"
        pyautogui.PAUSE = 0.2
        pyautogui.click(579,422)#- координаты кнопки "Задержка доставки. Доставка со склада ВБ"
        pyautogui.PAUSE = 0.2
        pyautogui.click(548,674)#- координаты поля "Комментарий"
        pyautogui.PAUSE = 0.2
        pyperclip.copy('Сказал клиенту информацию по его вопросу')
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.click(484,767)#- координаты кнопки "Зарегистрировать"
        say_message("Регистрация готова")
    elif "регистрация 2" in message:
        pyautogui.click(237,608) #- координаты кнопки "Детализация"
        pyautogui.PAUSE = 0.2
        pyautogui.click(1317,840)#- координаты кнопки "Регистрация обращения"
        pyautogui.PAUSE = 0.5
        pyautogui.click(670,323)#- координаты кнопки "Источник - Обращение"
        pyautogui.PAUSE = 0.2
        pyautogui.click(748,443) #- координаты кнопки "Запрос РРН, нет в ЛК"
        pyautogui.PAUSE = 0.2
        pyautogui.click(548,674)#- координаты поля "Комментарий"
        pyautogui.PAUSE = 0.2
        pyperclip.copy('Сказал клиенту информацию по его вопросу')
        pyautogui.hotkey('ctrl', 'v')
        #pyautogui.click(484,767)#- координаты кнопки "Зарегистрировать"
        say_message("Регистрация готова")
    elif "оценка" in message:
        pyperclip.copy("Пожалуйста, оцените мою консультацию.")
        say_message("хорошо")
    elif "сбой" in message:
        pyperclip.copy("Ранее процент выкупа был изображен не корректно. В данный момент ошибка была устранена и процент выкупа обновился, теперь все данные корректны.")
        say_message("хорошо")
    elif "платный" in message:
        pyperclip.copy("Информация о платном возврате отображается в разделе 'Корзина', ориентируясь на эту информацию, Вы можете принимать заказывать товар или нет.")
        say_message("хорошо")
    elif "утерян" in message:
        pyperclip.copy("Возможно товар был утерян и уже вряд ли придет. Рекомендуем отменить заказ и заказать заново если есть необходимость в товаре. Вы можете отменить заказ в Личном Кабинете в разделе 'Доставка'. После отмены денежные средства вернуться Вам в полном объеме. Приносим свои извинения за длительное ожидание заказа.")
        say_message("хорошо")
    elif "доставка" in message:
        pyperclip.copy("Для клиентов, которые проживают в дальних регионах, была введена платная доставка. Информацию о платной доставке Вы можете увидеть в разделе 'Корзина'.")
        say_message("хорошо")
    elif "курьер" in message:
        pyperclip.copy("Данный товар не был еще передан курьеру. В день доставки, когда товары будут переданы курьеру, в Ваш личный кабинет поступит уведомление. Курьер свяжется с Вами для согласования времени своего визита. В личном кабинете также будет указан номер телефона курьера, который привезет Ваш заказ, при необходимости Вы сможете связаться с ним самостоятельно.")
        say_message("хорошо")
    elif "ошибка отгрузки" in message:
        pyperclip.copy("Ваш товар поступит на тот пункт самовывоза, который вы указали при оформлении, на адрес г. Туапсе (Туапсинский р-н.), ул. Ленина, 2. Товар будет доставлен с небольшой задержкой, мы сделаем все возможное чтобы вы получили товар как можно скорее. Приносим свои извинения за ожидание.")
        say_message("хорошо")
    elif "выписка" in message:
        pyperclip.copy("По нашей информации данный товар был с оплатой при получении, поэтому возврата денежных средств не осуществлялось. Если списание 1199 руб. за этот товар было, отправьте пожалуйста выписку с банка, где показано что списание прошло успешно в WB чат. После этого мы займёмся вашим вопросом, и он будет решен.")
        say_message("хорошо")
    elif "кэш" in message:
        pyperclip.copy("Пожалуйста, попробуйте переустановить мобильное приложение, если вы пользуетесь им, на полную версию приложения. Если же Вы заходите на сайт с браузера, почистить кэш и куки. Также рекомендуем использовать браузер Google Chrome для входа на сайт.")
        say_message("хорошо")
    elif "сертификат" in message:
        pyperclip.copy("Вы можете обратиться за сертификатом/декларацией о соответствии к продавцу товара. Связаться с продавцом можно через раздел «Вопросы» карточки товара.\nВы сможете увидеть ответ продавца в разделе «Отзывы и вопросы» личного кабинета, вкладка «Вопросы».")
        say_message("хорошо")
    elif "смена номера" in message:
        pyperclip.copy("Для  смены номера, Вам нужно указать следующие данные:\n1. старый номер телефона\n2. новый номер телефона\n3. эл. почта указанная в кабинете\n4. есть ли доступ к почте.\n- Имя, указанное в Личном кабинете\n- Дата рождения\n- Адрес и способ последней доставки\n- Последние заказанные товары.")
        say_message("хорошо")
    elif "продавец" in message:
        pyperclip.copy("Для наших действующих партнеров и тех, кто планирует начать сотрудничество, работает партнерский портал. Там собраны все необходимые инструменты управления и коммуникации, а также размещена подробная информация о сотрудничестве. Ссылка на портал находится внизу главной страницы сайта Вайлдберриз под кнопкой «Партнерам».\nЕсли у Вас возникли вопросы о правилах поставки, требованиях к упаковке, спецификации или другие вопросы по сотрудничеству - Вы можете ознакомиться с информацией, размещенной в разделе «Инструкции» на портале, а также Вы можете связаться с сотрудниками компании для решения вопроса с помощью следующих ресурсов:\n1) Раздел Service Desk на портале, где можно создать обращение в различные отделы компании. Обращаем Ваше внимание, если Вы создали заявку, не нужно дублировать вопрос, создавая новое обращение с тем же вопросом, необходимо ожидать поступление ответа по уже оформленному ранее запросу.\n2) Чат только по вопросам перед первой поставкой https://t.me/wbofficialfirst")
        say_message("хорошо")
    elif "отзыв" in message:
        pyperclip.copy("Благодарим Вас за отзыв. Мы искренне сожалеем, что Вам пришлось столкнуться с подобной ситуацией. Мы делаем все возможное, чтобы нашим клиентам доставлялись качественные товары, но к сожалению, полностью исключить доставку товара с неверным вложением, браком или неполной комплектацией не можем. Мы предоставляем Вам возможность проверки и примерки товаров в момент получения. Надеемся что в дальнейшем у Вас будут только исключительно успешные и приятные покупки.")
        say_message("хорошо")
    elif "не туда" in message:
        pyperclip.copy("Мы искренне сожалеем, что Вам пришлось столкнуться с данной ситуацией, но после оформления заказа изменить способ и адрес доставки, а также состав заказа будет невозможно. Если при оформлении Вы ошибочно указали не тот адрес курьерской доставки или пункта самовывоза, выбрали неверный способ доставки, "
                       "Вы можете отменить заказ в течение 10 минут с момента его оформления и сделать заказ заново, указав верные данные по доставке. Если 10 минут после оформления заказа прошли, то Вы сможете отказаться от товара при получении или отменить доставку в случае задержки на 6 день от первой предполагаемой даты доставки. "
                       "Добавить товары в доставку, можно оформив новый заказ. Пожалуйста, выбирайте правильный пункт самовывоза при заказе. После 15 дней с момента поступления товара в пункт самовывоза, товар уедет обратно на склад и Вам вернутся денежные средства за Ваш заказ, за исключением 100 руб. за обратную логистику на склад.")
        say_message("хорошо")
    elif "даты" in message:
        pyperclip.copy("Просим свои извинения за доставленные неудобства. Для того, что бы мы могли провести проверку и указать сроки доставки в Вашем Личном кабинете, для появления функции отмены заказа в личном кабинете, пожалуйста, укажите в новом обращении устройство которым Вы пользуетесь (Android/IOS).")
        say_message("хорошо")
    elif "кредит" in message:
        pyperclip.copy("Для того чтобы оплатить товар в рассрочку или кредит:\n• Выберите понравившееся товары и положите их в корзину\n• Выберите способ оплаты «Рассрочка» или «Кредит»\n• Заполните анкету и дождитесь решения банка\n• Подпишите кредитный договор по SMS и получите ваш заказ\nКредитные условия индивидуальны для каждого покупателя. С условиями можно будет ознакомиться в момент оформления кредитного договора.\nКредит доступен на все товары при стоимости корзины от 5000 рублей\n• Для оформления кредита необходимо:\n• Быть гражданином РФ\n• Иметь постоянную регистрацию\n• Быть старше 18 лет\n• Иметь постоянный доход")
        say_message("хорошо")
    elif "возврат" in message:
        pyperclip.copy("Не подошедшие товары Вы можете вернуть в пункт самовывоза или оформить курьера, при условиях:\n1. Полная комплектация товара;\n2. Товар не был в употреблении, сохранен товарный вид и потребительские свойства;\n3. Присутствуют пломбы, фабричные ярлыки, навесные бирки, упаковка (при наличии);\n4. Подлежит обмену и возврату.")
        say_message("хорошо")
    elif "курьером" in message:
        pyperclip.copy("Оформить заявку на возврат курьером можно в полной версии сайта в разделе 'покупки' - необходимо выбрать товар и нажать кнопку 'вернуть товар'. Далее необходимо перейти во вкладку 'оформление возврата' и закончить оформление заявки, выбрав причину, адрес и дату для приезда курьера.")
        say_message("хорошо")
    elif "невозвратный" in message:
        pyperclip.copy("Данный товар является невозвратным. Его нельзя вернуть после покупки по причине 'Не подошло'. Если товар Вам не подходит, отказаться от него можно при получении в пункте выдачи. Сожалеем, что такая ситуация произошла и надеемся, что в дальнейшем все покупки у Вас будут исключительно удачными.")
        say_message("хорошо")
    elif "запрос" in message:
        pyperclip.copy("Мы занимаемся Вашим вопросом. Для этого был сформирован отдельный внутренний запрос. Ответ с решением по Вашему вопросу будет отправлен на Вашу электронную почту, указанную в Личном Кабинете. Мы сделаем все возможное, чтобы Ваш вопрос решился как можно скорее. Приносим свои извинения за сложившуюся ситуацию.")
        say_message("хорошо")
    elif "проблема 1" in message:
        pyautogui.click(668,322) #- координаты кнопки "Проблемы"
        pyautogui.PAUSE = 0.2
        pyautogui.click(184, 482)  # - координаты кнопки "Создать проблему"
        pyautogui.click(184, 482)  # - координаты кнопки "Создать проблему"
        pyautogui.click(184, 482)  # - координаты кнопки "Создать проблему"
        pyautogui.click(184, 482)  # - координаты кнопки "Создать проблему"
        pyautogui.PAUSE = 0.2
        pyautogui.click(668,318) #- координаты поля "Источник"
        pyautogui.PAUSE = 0.2
        pyautogui.click(581,452) #- координаты кнопки Сайт "Обращения"
        pyautogui.PAUSE = 0.2
        pyautogui.click(636,401) #- координаты поля "Группа"
        pyautogui.PAUSE = 0.2
        pyautogui.click(603,724) #- координаты кнопки "Проблемы - Доставка"
        pyautogui.PAUSE = 0.2
        pyautogui.click(641,478) #- координаты поля "Класс"
        pyautogui.PAUSE = 0.2
        pyautogui.click(621,692) #- координаты кнопки "Задержка в сроках доставки"
        pyautogui.PAUSE = 0.2
        pyautogui.click(620,514) #- координаты поля "Укажите 1 rid"
        pyautogui.PAUSE = 0.2
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.PAUSE = 0.2
        pyautogui.click(657,632) #- координаты поля "Проблема"
        pyautogui.PAUSE = 0.2
        pyperclip.copy('Задержка, клиент ждет')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        say_message("Все готово")
    elif "проблема 2" in message:
        pyautogui.click(668,322) #- координаты кнопки "Проблемы"
        pyautogui.PAUSE = 0.2
        pyautogui.click(184,482) #- координаты кнопки "Создать проблему"
        pyautogui.click(184,482) #- координаты кнопки "Создать проблему"
        pyautogui.click(184,482) #- координаты кнопки "Создать проблему"
        pyautogui.click(184,482) #- координаты кнопки "Создать проблему"
        pyautogui.PAUSE = 0.2
        pyautogui.click(668,318) #- координаты поля "Источник"
        pyautogui.PAUSE = 0.2
        pyautogui.click(581,452) #- координаты кнопки Сайт "Обращения"
        pyautogui.PAUSE = 0.2
        pyautogui.click(636,401) #- координаты поля "Группа"
        pyautogui.PAUSE = 0.2
        pyautogui.click(601,682) #- координаты кнопки "Проблемы - Взаиморасчеты"
        pyautogui.PAUSE = 0.2
        pyautogui.click(641,478) #- координаты поля "Класс"
        pyautogui.PAUSE = 0.2
        pyautogui.click(570,654) #- координаты кнопки "Запрос РРН"
        pyautogui.PAUSE = 0.2
        pyautogui.click(657,632) #- координаты поля "Проблема"
        pyautogui.PAUSE = 0.2
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('клиент ждет дс')
        say_message("Все готово")
    elif "жми" in message:
        try:
            x, y = pyautogui.locateCenterOnScreen(r"img\Автоклик.png")
            for i in range(50):
                pyautogui.click(x, y)
                pyautogui.PAUSE = 0
            say_message("Ура")
        except TypeError:
            pass
    elif "слава украине" in message:
        say_message("Героям Слава!")
    elif "расскажи анекдот" in message:
        say_message("Не знаю я никаких анекдотов, а знаешь почему? Потому что ты ленивая жопа!")
    elif "молодец" in message:
        say_message("Спасибо, хозяин")
    elif "умница" in message:
        say_message("Спасибо, хозяин")
    elif "спасибо" in message:
        say_message("Рада помочь!")
    elif "пока" in message:
        say_message("Пока, хозяин!")
        exit()
    else:
        pass

def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = '_audio_'+str(time.time())+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)



if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)

