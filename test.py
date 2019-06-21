def ThreeItem(item):
  ti = SortItem(item)
  fin = ti[2]
  return fin

def MoreThreeItems(item):
  ti = SortItem(item)
  fin = 0
  col = len(ti) - (len(ti)//3)
  for i in range(len(ti)):
    if i >= col:
      fin = fin + ti[i]
  return fin

def SortItem(item):
  for i in range(0,len(item)-1):
    for j in range(0,len(item)-i-1):
      if item[j] < item[j+1]:
        item[j],item[j + 1] = item[j + 1], item[j]
  return item

def MaximumDiscount(N, price):
  tst = []
  discount = 0
  disc3 = 0
  n = 1
  if len(price) != N:
    return 'Неверно введенные данные!'
  if len(price) < 3:
    return 0
  elif N >= 3 and N < 6 :
    discount = ThreeItem(price)
    return discount
  else:
    discount = MoreThreeItems(price)
    for i in range(N):
      if n % 3 == 0 and i != 0:
        disc3 = disc3 + SortItem(price)[n-1]
      n += 1
    if disc3 > discount:
      return disc3
    else:
      return discount

print(MaximumDiscount(9,[300,350,400,150,200,250,100,250,50]))