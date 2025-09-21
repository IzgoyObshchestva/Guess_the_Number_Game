from func import action_selection, clear_console
from file_zxc_manager import get_all_file_words, ecode_file, decode_file

def w():
    text = '''>Чтобы сделать свой файл со словами, создайте заранее файл <название>.zxc
>замем поместите его в папку "data"
>затем зайдите сюда снова и закодируйте его
>записывайте каждое слово в отдельной строчке и если хотите ограничить количество попыток напишите их по примеру: "дом/3", а иначе по умолчанию их будет 7'''
    print(text)
    clear_console()


def ww(code: bool):
    while True:
        all_file_name = get_all_file_words()
        if all_file_name:
            zxc = f"выберите файл:\n1) назад\n{'\n'.join([f'{index+2}) {name}' for index, name in enumerate(all_file_name)])}"
            qwe = action_selection(tuple(range(1, len(all_file_name)+2)), zxc)
            if qwe == 1:
                clear_console()
                break
            else:
                if code:
                    asd = ecode_file(all_file_name[qwe-2])
                    print(asd)
                    clear_console()
                else:
                    asd = decode_file(all_file_name[qwe-2])
                    print(asd)
                    clear_console()
        else:
            print('У вас нету файлов для игры')
            clear_console()
            break


def working_with_files():
    while True:
        zxc = 'Выберите действие:\n1) назад\n2) как создать свой файл\n3) закодировать\n4) раскодировать'
        qwe = action_selection(tuple(range(1, 5)), zxc)
        match qwe:
            case 1:
                break
            case 2:
                clear_console(False)
                w()
            case 3:
                clear_console(False)
                ww(True)
            case 4:
                clear_console(False)
                ww(False)