import os

def clear_console(pressing_enter: bool = True):
    if os.name == 'nt':
        if pressing_enter:
            input('Нажмите Enter, чтобы продолжить...')
        os.system('cls')
    else:
        if pressing_enter:
            input('Нажмите Enter, чтобы продолжить...')
        os.system('clear')


def action_selection(list_options: tuple, description: str):
    while True:
        print(description)
        try:
            qwe = int(input('Введите число: '))
        except:
            print('Вы ввели не число +', end=' ')
        if qwe in list_options:
            break
        else:
            print('Такой операции нет')
            clear_console()
    return qwe