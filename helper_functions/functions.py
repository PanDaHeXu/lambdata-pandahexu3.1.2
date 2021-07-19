class DFfunction:
    def __init__(self, df):
        self.df = df

    def null_count(df):
        '''Function to auto-count null values for an entire dataframe'''
        return df.isnull().sum().sum()


class ListFunction:
    def __inti__(self, df, list_to_add):
        self.df = df
        self.list_to_add = list_to_add

    def list2col(list_to_add, df):
        '''Function to add a list to a dataframe as a new column,
        if the number of list items and observations in the df are equal'''
        df['Added List'] = list_to_add
        return df
