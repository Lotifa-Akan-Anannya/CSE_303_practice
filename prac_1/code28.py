for i in range (0,5):
  for j in range (0,5):
    if(i==0 or i==5-1 or j==0 or j==5-1):
      print('*',end  = " ")
    else:
      print(' ',end =" ")
  print()
