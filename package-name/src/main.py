from functions import read_json, sort_data, sort_data_by_date, mask_from_to_msg, get_date
import os
read_json_list = read_json(os.path.join(os.path.dirname(__file__), 'operations.json'))
sort_data_list = sort_data(read_json_list)
sort_data_by_date_list = sort_data_by_date(sort_data_list)

function_list_all = sort_data_by_date_list[:5]

for operation in function_list_all:
    date = get_date(operation.get('date'))
    desc = operation.get('description')
    from_ = mask_from_to_msg(operation.get('from'))
    if from_:
        from_ = from_ + '->'
    to_ = mask_from_to_msg(operation.get('to'))
    amount = operation.get('operationAmount')['amount']
    currency = operation.get('operationAmount')['currency']['name']

print(f'{date} -> {desc}')
print(f'{from_}{to_}')
print(f'{amount} {currency}')