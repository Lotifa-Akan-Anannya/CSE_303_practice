new_dataframe =df.fillna(method='bfill')
new_dataframe.isnull().sum()
