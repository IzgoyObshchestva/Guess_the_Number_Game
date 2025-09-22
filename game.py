from func import action_selection, clear_console
from file_zxc_manager import decode_file_config, get_all_file_words, read_words_from_file, save_statistics


def www(word: str):
    word = word.split('/')
    if len(word) == 1:
        return (word[0].lower(), 7)
    else:
        return (word[0].lower(), int(word[1]))


def start_of_the_round(file_name: str):
    list_words = read_words_from_file(file_name)
    qqq = False
    total_words = len(list_words)
    victory = 0
    for word in list_words:
        asd = www(word)
        print(f'Угадай слово из {len(asd[0])} букв')
        print(f'У тебя {asd[1]} попыток')
        print('Введите 000 чтобы сдаться и 111 чтобы полностью выйти')
        i = 1
        while i <= asd[1]:
            qwe = input(f'Попытка {i}: ').lower()
            
            if len(qwe) != len(asd[0]):
                print(f'⚠️  Ваше слово должно быть из {len(asd[0])} букв')
                continue
            else:
                i+=1

            if qwe == asd[0]:
                print('🎰 Ты угадал')
                victory += 1
                clear_console()
                break
            elif qwe == '000':
                print('💀 Вы сдались')
                clear_console()
                break
            elif qwe == '111':
                print('💀 Выйти')
                clear_console()
                qqq = True
                break
            else:
                print(word_check(qwe, asd[0]))
                
            
        else:
            print(f'💀 Сори ты просрал, слово было: {asd[0]}')
            clear_console()
        if qqq:
            break
    else:
        defeat = total_words - victory
        print(f'Статистика:\nВсего слов: {total_words}\nПобеды: {victory}\nПоражения: {defeat}')
        save_statistics(total_words, defeat, victory)
        clear_console()

# print('\033[31mд\033[33mо\033[32mм\033[0m')
def word_check(word: str, answer: str):
    res = ''
    for i in range(len(word)):
        # print(i, end=' ')
        if word[i] == answer[i]:
            # print('1', word[i], answer[i])
            res += f'\033[32m{word[i]}'
        elif word[i] in answer:
            # print('2', word[i], answer)
            res += f'\033[33m{word[i]}'
        else:
            # print('3', word[i], answer, word[i] in answer)
            res += f'\033[31m{word[i]}'
    else:
        res += f'\033[0m'
    return res



def w():
    print(decode_file_config())
    clear_console()


def ww(qwe):
    while True:
        all_file_name = get_all_file_words()
        if all_file_name:
            zxc = f'выберите файл:\n1) назад\n{'\n'.join([f'{index+2}) {name}' for index, name in enumerate(all_file_name)])}'
            qwe = action_selection(tuple(range(1, len(all_file_name)+2)), zxc)
            if qwe == 1:
                clear_console()
                break
            else:
                clear_console()
                start_of_the_round(all_file_name[qwe-2])
        else:
            print('У вас нету файлов для игры')
            clear_console()
            break


def start_game():
    while True:
        zxc = 'Выберите действие:\n1) назад\n2) показать статистику\n3) начать игру'
        qwe = action_selection(tuple(range(1, 4)), zxc)
        match qwe:
            case 1:
                break
            case 2:
                clear_console(False)
                w()
            case 3:
                clear_console(False)
                ww(True)