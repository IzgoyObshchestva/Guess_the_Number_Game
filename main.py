from file_zxc_manager import create_file_config
from func import clear_console, action_selection
from working_files import working_with_files
from game import start_game


# def file_selection():
#     print('выберите файл со словами для игры:')
#     list_file = get_all_file_words()
#     while True:
#         if list_file:
#             for index, name in enumerate(list_file):
#                 print(f'{index+1}) {name}')
#             qwe = input('число: ')

#             if int(qwe)-1 < len(list_file) and int(qwe)-1 >= 0:
#                 break
#             else:
#                 print('Такого файла нет')
#         else:
#             print('У вас нету файлов для игры')

#     return list_file[int(qwe)-1]


def main():
    while True:
        clear_console(False)
        # print('\033[31mд\033[33mо\033[32mм\033[0m')
        qwe = action_selection((1, 2, 3), 'Что будем делать?:\n1) играть\n2) работа с файлами\n3) выход')
        clear_console(False)
        if qwe == 1:
            print('играть')
            start_game()
        elif qwe == 2:
            print('работа с файлами')
            working_with_files()
        elif qwe == 3:
            print('выход')
            break


if __name__ == '__main__':
    create_file_config()
    main()