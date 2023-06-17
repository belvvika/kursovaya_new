from functions import read_json
import os
read_json_list = read_json(os.path.join(os.path.dirname(__file__), 'operations.json'))
for key in read_json_list:
    key_sort_data = key.get('state')
    key_hide_card = key.get('from')
    key_hide_amount = key.get('to')
    key_data = key.get('date')
    key_description = key.get('description')
    key_amount = key.get('operationAmount')
    key_code = key.get('operationAmount')
    if key_sort_data == 'EXECUTED':
        executed_operation_list = []
        executed_operation_list.append(key_data[0:10])
        executed_operation_list.append(key_description)
        executed_operation_list.append(key_hide_card)
        executed_operation_list.append(key_hide_amount)
        executed_operation_list.append(key_amount['amount'])
        executed_operation_list.append(key_code['currency'])
for keys in executed_operation_list:
    print(keys)