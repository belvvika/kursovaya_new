import json


def read_json(file_path):
    '''
    читает файл json
    '''
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    return data



def sort_data():
    '''
    сортирует данные по дате
    '''
    pass



def hide_card():
    '''
    скрывает исходный номер карты
    '''
    pass


def hide_amount():
    '''
    скрывает исходный номер счета
    '''
    pass



