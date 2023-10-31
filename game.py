import random
ver = 0
i = 1
player_count = 0
bot_count = 0

p = int(input('Выберите режим игры. Повторяющийся - 1, турнир - 2: \n'))

if p == 1:
    while i == 1:
        answer = int(input('1 - камень, 2 - ножницы, 3 - бумага:\n ')) #Значение от пользователя

        if answer == 1 or answer == 2 or answer == 3:
            ver = 1
        if answer == 1:
            print('Вы выбрали камень :)')
        if answer == 2:
            print('Вы выбрали ножницы :)')
        if answer == 3:
            print('Вы выбрали бумагу :)')

        bot = random.randint(1, 3) #Значение "компьютера"

        if bot == 1:
            print('Компьютер выбрал камень')
        if bot == 2:
            print('Компьютер выбрал ножницы')
        if bot == 3:
            print('Компьютер выбрал бумагу')

        if answer == bot:
            win = 0 #Никто не победил
        if answer == 1 and bot == 2:
            win = 1 #Победа пользователя
        if answer == 1 and bot == 3:
            win = 2 #Победа компьютера
        if answer == 2 and bot == 1:
            win = 2
        if answer == 2 and bot == 3:
            win = 1
        if answer == 3 and bot == 1:
            win = 1
        if answer == 3 and bot == 2:
            win = 2

        if win == 0:
            print('Ничья!')
        if win == 1:
            print('Вы победили!!!!')
        if win == 2:
            print('Побежил компуктер :(')

        r = int(input('Желаете продолжить игру? 1 - да, 2 - нет:\n '))
        if r != 1 or r != 2:
            print('Вы введи неправильное значение! Введите 1 или 2!')
            exit()
        if r == 2:
            i += 1
            print('До свидания! Спасибо за игру!')

if p == 2:
    print('Введите количество раундов:')
    number = int(input())

    if number <= 0:
        number = int(input('Вы ввели неправильное значение! Повторите попытку\n'))

    else:
        for i in range(1, number + 1 ):
            answer = int(input('1 - камень, 2 - ножницы, 3 - бумага:\n'))

            if answer == 1 or answer == 2 or answer == 3:
                ver = 1
            else:
                answer = int(input('Вы ввели неправильное значение, поторите попытку!'))

            if answer == 1:
                print('Вы выбрали камень :)')
            if answer == 2:
                print('Вы выбрали ножницы :)')
            if answer == 3:
                print('Вы выбрали бумагу :)')

            bot = random.randint(1, 3) #Значение "компьютера"

            if bot == 1:
                print('Компьютер выбрал камень')
            if bot == 2:
                print('Компьютер выбрал ножницы')
            if bot == 3:
                print('Компьютер выбрал бумагу')

            if answer == bot:
                win = 0 #Никто не победил
            if answer == 1 and bot == 2:
                win = 1 #Победа пользователя
            if answer == 1 and bot == 3:
                win = 2 #Победа компьютера
            if answer == 2 and bot == 1:
                win = 2
            if answer == 2 and bot == 3:
                win = 1
            if answer == 3 and bot == 1:
                win = 1
            if answer == 3 and bot == 2:
                win = 2

            if win == 0:
                print('Ничья!')

            if win == 1:
                print('Вы победили!!!')
                player_count += 1

            if win == 2:
                print('Победил компуктер :(')
                bot_count += 1

            print(player_count, ' : ', bot_count)

else:
    p = int(input('Вы ввели неправильное число! Повторите попытку'))





