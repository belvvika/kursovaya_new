from src.functions import read_json, sort_data, hide_card, hide_amount, data, description, amount



def test_read_json(path_test_json, expected_result):
    assert read_json(path_test_json) == expected_result



def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort


def test_hide_card(expected_result_for_hide_card):
    assert hide_card(expected_result_for_hide_card)


def test_hide_amount(expexted_result_for_hide_amount):
    assert hide_amount(expexted_result_for_hide_amount)

def test_data(expexted_result_data):
    assert data(expexted_result_data)

def test_description(expexted_result_description):
    assert description(expexted_result_description)

def test_amount(expexted_result_amount):
    assert amount(expexted_result_amount)