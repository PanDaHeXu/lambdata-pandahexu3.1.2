import pytest
from helper_functions.functions import ListFunction

@pytest.fixture()
def test_list():
    test_list = [a, b, c, d]
    return test_list

@pytest.fixture()
def test_df():
    data = {
        'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]
    }
    df = pd.DataFrame(data)
