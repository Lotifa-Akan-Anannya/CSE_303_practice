def bar_plot(column_name):
  values =  df[column_name]
  values_count  = values.value_counts().plot.bar()
  plt.show()

category_column  = ["Sex","Pclass","Embarked","Parch"]
for c in category_column:
  print
