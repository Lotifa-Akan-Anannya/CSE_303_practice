
plt.pie(df["Survived"].value_counts().values)
plt.legend( df["Survived"].value_counts().index)
