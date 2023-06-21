from src.functions import read_json, sort_data, description, amount, sort_data_by_date, mask_card_number, mask_from_to_msg, mask_account_number, get_date


def test_read_json(path_test_json, expected_result):
    assert read_json(path_test_json) == expected_result

def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort

def test_description(expexted_result_description):
    assert description(expexted_result_description)

def test_amount(expexted_result_amount):
    assert amount(expexted_result_amount)

def test_sort_data_by_date(expexted_result_sort_data_by_date):
    assert sort_data_by_date(expexted_result_sort_data_by_date)

def test_mask_from_to_msg(expexted_result_mask_from_to_msg):
    assert mask_from_to_msg(expexted_result_mask_from_to_msg)

def test_mask_card_number(expexted_result_mask_card_number):
    assert mask_card_number(expexted_result_mask_card_number)

def test_mask_account_number(expexted_result_mask_account_number):
    assert mask_account_number(expexted_result_mask_account_number)

def test_get_date(expexted_result_get_date):
    assert get_date(expexted_result_get_date)