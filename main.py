# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
username = ''
user_age = 0
user_ph = ''
user_email = ''
user_info = ''
index_home = ''
living_address = ''

# business info
ogrnip = ''
inn = ''
ch_acc = '' # Рассчетный счет
name_bank = ''
bik = ''
corr_acc = '' # Корреспондентский счёт

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                username = input('Введите имя: ')
                while 1:
                        # validate user age
                        user_age = int(input('Введите возраст: '))
                        if user_age > 0:
                            break
                        print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                user_ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        user_ph += ch

                user_email = input('Введите адрес электронной почты: ')
                index_home = int(input('Введите индекс: '))
                living_address = input('Введите почтовый адрес без индекса: ')
                user_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input info pred
                while True:
                    ogrnip = int(input('Введите ОГРНИП: '))
                    if len(str(ogrnip)) == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр!')
                while True:
                    inn = int(input('Введите ИИН: '))
                    if len(str(inn)) == 20:
                        break
                    print('ИИН должен содержать 20 цифр!')
                ch_acc = int(input('Введите рассчетный счёт: '))
                name_bank = input('Введите название банка: ')
                bik = int(input('Введите БИК: '))
                corr_acc = int(input('Введите кореспанденский счёт: '))

            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # print general information
                print(SEPARATOR)
                print('Имя:    ', username)
                if 11 <= user_age % 100 <= 19: years_name = 'лет'
                elif user_age % 10 == 1: years_name = 'год'
                elif 2 <= user_age % 10 <= 4: years_name = 'года'
                else: years_name = 'лет'


                print('Возраст:', user_age, years_name)
                print('Телефон:', user_ph)
                print('E-mail: ', user_email)
                print('Индекс: ', index_home)
                print('Адрес: ', living_address)
                if user_info:
                        print('')
                        print('Дополнительная информация:')
                        print(user_info)

            elif option2 == 2:
                # print full information
                print(SEPARATOR)
                print('Имя:    ', username)
                if 11 <= user_age % 100 <= 19:    years = 'лет'
                elif user_age % 10 == 1:    years = 'год'
                elif 2 <= user_age % 10 <= 4:      years = 'года'
                else:  years = 'лет'
                print('Возраст:', user_age, years)
                print('Телефон:', user_ph)
                print('E-mail: ', user_email)
                print('Индекс: ', index_home)
                print('Адрес: ', living_address)
                if user_info:
                            print('')
                            print('Дополнительная информация:')
                            print(user_info)

                print('\nИнформация о предпринимателе')
                print(f'ОГРНИП: {ogrnip}')
                print(f'ИНН: {inn}')
                print('Банковские реквизиты')
                print(f'Р/с: {ch_acc}')
                print(f'Банк: {name_bank}')
                print(f'Бик: {bik}')
                print(f'К/с: {corr_acc}')


            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')
