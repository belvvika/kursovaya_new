
from package_name.functions import read_json



def test_read_json(path_test_json,expected_result):
    assert read_json(path_test_json) == expected_result
