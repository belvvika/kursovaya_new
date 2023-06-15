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

def data(date: list[dict]) -> list[dict]:
    '''
    возвращает дату перевода
    '''
    date_list = []
    for operation in date:
        if operation['date']:
            date_list.append(operation)
    return date_list[:10]

def description(description: list[dict]) -> list[dict]:
    '''
    возвращает описание перевода
    '''
    description_list = []
    for operation in description:
        if operation['description']:
            description_list.append(operation)
    return description_list

def amount(amount: list[dict]) -> list[dict]:
    '''
    возвращает сумму перевода
    '''
    amount_list = []
    for operation in amount:
        if operation['operationAmount']:
            amount_list.append(operation)
    return amount_list

