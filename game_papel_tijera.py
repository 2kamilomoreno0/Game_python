import random


def choose_options():
    OPTIONS = ('piedra', 'papel', 'tijera')
    user = input('Introduce su opcion: ')
    user = user.lower()

    if not user in OPTIONS:
        print('esa opcion no es valida')
        return None, None

    computer = random.choice(OPTIONS)
    print('opcion usada por humano es =>', user)
    print('opcion usada es =>', computer)
    return user, computer


def check_rules(user, computer, user_win, computer_win):
    if user == computer:
        print('Empate!')
    elif user == 'Piedra':
        if computer == 'Tijera':
            print('piedra gana a tijera')
            print('Humano gano')
            user_win += 1
        else:
            print('papel gana a tijera')
            print('maquina gano')
            computer_win += 1

    elif user == 'Papel':
        if computer == 'piedra':
            print('papel gana a piedra')
            print('humano gano')
            user_win += 1
        else:
            print('tijera gana a papel')
            print('maquina gano')
            computer_win += 1

    elif user == 'tijera':
        if computer == 'papel':
            print('tijera gana a papel')
            print('humano gano')
            user_win += 1
        else:
            print('piedra gana a tijera')
            print('maquina gano')
            computer_win += 1
    return user_win, computer_win


def run_game():
    computer_win = 0
    user_win = 0
    round = 1
    while True:
        print('*' * 10)
        print('ROUND', round)
        print('*' * 10)

        print('maquina gano', computer_win)
        print('humano gano', user_win)
        round += 1

        user, computer,  = choose_options()
        user_win, computer_win = check_rules(
            user, computer, user_win, computer_win)

        if computer_win == 2:
            print('el ganador es la maquina')
            break

        if user_win == 2:
            print('el ganador es el humano')
            break


run_game
