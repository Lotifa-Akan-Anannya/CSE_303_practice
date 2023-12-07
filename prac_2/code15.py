df[ ["Sex","Pclass","Survived"] ].groupby(["Sex","Survived","Pclass"]).value_counts()
