import pytest
from helper_functions.functions import ListFunction

def test_df_length(list_to_add, df):
    list_to_add = test_list
    df = test_df
    assert(len(list_to_add) == df.shape[0])
