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
        if operation.get('state') == 'EXECUTED':
            sorted_data.append(operation)
    return sorted_data

def hide_card(number: list[dict]) -> list[dict]:
    '''
    скрывает исходный номер карты
    '''
    hiden_number = []
    for operation in number:
        if operation.get('from'):
            hiden_number.append(operation)
    return hiden_number

def hide_amount(amount:list[dict]) -> list[dict]:
    '''
    скрывает исходный номер счета
    '''
    hiden_amount = []
    for operation in amount:
        if operation.get('to'):
            hiden_amount.append(operation)
    return hiden_amount

def description(description: list[dict]) -> list[dict]:
    '''
    возвращает описание перевода
    '''
    description_list = []
    for operation in description:
        if operation.get('description'):
            description_list.append(operation)
    return description_list

def amount(amount: list[dict]) -> list[dict]:
    '''
    возвращает сумму перевода
    '''
    amount_list = []
    for operation in amount:
        if operation.get('operationAmount'):
            amount_list.append(operation)
    return amount_list

def sort_data_by_date(data: list[dict]) -> list[dict]:
    '''
    возвращает отсортированную дату перевода
    '''
    sort_data_by_date_list = []
    for operation in data:
        if operation.get('date'):
            sort_data_by_date_list.sort(key=lambda x: x['date'], reverse=True)
            sort_data_by_date_list.append(operation)
    return sort_data_by_date_list