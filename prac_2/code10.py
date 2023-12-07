new_dataframe  = df[ df["Age"] < 10 ]
new_dataframe["Survived"].value_counts().plot.bar()
