import colorama
import random
import time


colorama.init()
def game_random():
    print('Отгадай за 7 попыток.\nКакое число я загадал? от 1 до 100')

    total = 7
    random_number = random.randrange(1, 101)
    while total != 0:
        print()
        try:
            num = int(input())
            if 0 < num < random_number:
                print(f'Слишком мало, попробуйте ещё раз\nПопыток осталось [ {total-1} ]')
            elif 101 > num > random_number:
                print(f'Слишком много, попробуйте ещё раз\nПопыток осталось [ {total-1} ]')
            elif num == random_number:
                print(f'Вы угадали, поздравляю!\nПопыток осталось [ {total-1} ]')
                break
            else:
                print('Я загадал число от 1 до 100, попробуйте снова')
        except (TypeError, ValueError):
            print('Нужно вводить только число')
        total -= 1
    return colorama.Fore.RED + "К сожалению, вы проиграли."

while True:
    print(colorama.Fore.RED + colorama.Fore.YELLOW + 'Сыграем? Нажми [ + ] или [ - ]')
    if input() == '+':
        print(game_random())
    else:
        print('Спасибо за игру, приходи ещё :)')
        time.sleep(2)
        exit()
