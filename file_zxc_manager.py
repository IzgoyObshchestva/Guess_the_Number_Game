import os
import base64
folder = 'data'
file_path = os.path.join(folder, 'config.zxc')

def create_file_config():
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'Папка "{folder}" создана')

    
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            data = f"Угаданных слов: 0\nНе угаданных слов: 0\nВсего слов: 0"
            encoded = base64.b64encode(data.encode("utf-8"))
            f.write(encoded)
            print(f'Файл конфигурации создан')




def decode_file_config():
    with open(file_path, "rb") as f:
        encoded = f.read()
        decoded = base64.b64decode(encoded).decode("utf-8")
    return decoded


def get_all_file_words():
    all_items = os.listdir(folder)
    all_items.remove('config.zxc')
    return all_items


def is_base64_file(path: str) -> bool:
    try:
        with open(path, "rb") as f:
            data = f.read()
        base64.b64decode(data, validate=True)  # validate=True проверяет, что символы допустимые
        return True
    except Exception:
        return False


def ecode_file(name_file: str) -> str:
    if not is_base64_file(f'data/{name_file}'):
        with open(f'data/{name_file}', 'rb') as f_in:
            data = f_in.read()
            encoded = base64.b64encode(data)
        with open(f'data/{name_file}', 'wb') as f_out:
            f_out.write(encoded)
        return 'Файл успешно закодирован'
    return "Файл уже закодирован"


def decode_file(name_file: str) -> str:
    if is_base64_file(f'data/{name_file}'):
        with open(f'data/{name_file}', 'rb') as f_in:
            encoded = f_in.read()
            data = base64.b64decode(encoded)
        with open(f'data/{name_file}', 'wb') as f_out:
            f_out.write(data)
        return 'Файл успешно раскодирован'
    return "Файл уже раскодирован"


def read_words_from_file(file_name: str):
    if is_base64_file(f'data/{file_name}'):
        with open(f'data/{file_name}', "rb") as f:
            encoded = f.read()
            qwe = base64.b64decode(encoded).decode("utf-8").split('\n')
        return tuple(map(lambda x: x.replace('\r', ''), qwe))
    else:
        with open(f'data/{file_name}', 'r', encoding='utf-8') as f:
            qwe = f.readlines()
        return tuple(map(lambda x: x.replace('\n', ''), qwe))
    

def save_statistics(total_words: int, defeat: int, victory: int):
    text = list(map(lambda x: x.rsplit(' ', 1), decode_file_config().split('\n')))
    text[0][1] = int(text[0][1])+victory
    text[1][1] = int(text[1][1])+defeat
    text[2][1] = int(text[2][1])+total_words

    data = '\n'.join([f'{i[0]} {i[1]}' for i in text])

    with open(file_path, 'wb') as f:
        encoded = base64.b64encode(data.encode("utf-8"))  # строку → байты
        f.write(encoded)


