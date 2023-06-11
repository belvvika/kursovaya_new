from package_name.functions import read_json, sort_data



def test_read_json(path_test_json,expected_result):
    assert read_json(path_test_json) == expected_result



def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort
