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

def mask_card_number(number: str) -> str:
    '''
    скрывает номер карты
    '''
    return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
def mask_account_number(number: str) -> str:
    '''
    скрывает номер счета
    '''
    return  '**' + number[-4:]
def mask_from_to_msg(msg: [str, None]) -> str:
    if msg is None:
        return ''
    msg_split = msg.split(sep=' ')
    if msg_split[0] == 'Счет':
        number_hidden = mask_account_number(msg_split[-1])
    else:
        number_hidden = mask_card_number(msg_split[-1])
    return ''.join(msg_split[:-1]) + ' ' + number_hidden

def get_date(dt:str) -> str:
    '''
    возвращает преобразованную дату
    '''
    sep = '.'
    d = dt[0:10].split(sep='-')
    return d[2] + sep + d[1] + sep + d[0]