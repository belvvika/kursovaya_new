from functions import read_json, sort_data, hide_card, sort_data_by_date, hide_amount, amount, description
import os
read_json_list = read_json(os.path.join(os.path.dirname(__file__), 'operations.json'))
sort_data_list = sort_data(read_json_list)
sort_data_by_date_list = sort_data_by_date(sort_data_list)
hide_card_list = hide_card(sort_data_by_date_list)
hide_amount_list = hide_amount(hide_card_list)
amount_list = amount(hide_amount_list)
description_list = description(amount_list)
function_list_all = description_list[:5]

for key in function_list_all:
    print(f'{key.get("date")[:10]} -> {key.get("description")}')
    print(f'{key.get("from")} -> {key.get("to")}')
    print(f'{key.get("operationAmount")["amount"]} {key.get("operationAmount")["currency"]["name"]}')
