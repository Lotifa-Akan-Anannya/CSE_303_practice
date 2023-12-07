def bar_plot(column_name):
 values = df["Sex"]
 values.value_counts().plot.bar()
 plt.show()
