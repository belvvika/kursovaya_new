import json


def read_json(file_path):
    '''
    читает файл json
    '''
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)

    return data



def sort_data(data: list[dict]) -> list[dict]:
    '''
    сортирует данные по дате
    '''
    sorted_data = []
    for operation in data:
        if operation['state'] == 'EXECUTED':
            sorted_data.append(operation)
    return sorted_data



def hide_card(number: list[dict]) -> list[dict]:
    '''
    скрывает исходный номер карты
    '''
    hiden_number = []
    for operation in number:
        if operation['from']:
            hiden_number.append(operation)
            hiden_number[14:-4] = '*'
    return hiden_number


def hide_amount(amount:list[dict]) -> list[dict]:
    '''
    скрывает исходный номер счета
    '''
    hiden_amount = []
    for operation in amount:
        if operation['to']:
            hiden_amount.append(operation)
            hiden_amount[:-4] = '*'
    return hiden_amount



