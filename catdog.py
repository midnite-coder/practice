def cat_dog(str):
  c1=0
  c2=0
  for i in range(len(str)-1):
    if str[i]=='c':
      if str[i]=='a':
        if str[i]=='t':
          c1=c1+1
          i=i+3
          continue
    elif str[i]=='d':
      if str[i]=='o':
        if str[i]=='g':
          c2=c2+1
          i=i+3
          continue
  if c1==c2:
    return True
  else:
    return False