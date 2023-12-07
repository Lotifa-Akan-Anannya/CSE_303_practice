df[ ["Sex","Survived"] ].groupby(["Sex"]).sum().plot.bar()
