def sort_zeros_ones_twos(array):
  a = 0
  b = 0
  c = 0
  n = len(array)
  for i in range(n):
    if array[i] == 0:
      a += 1

  for i in range(n):
    if array[i] == 1:
      b += 1

  for i in range(n):
    if array[i] == 2:
      c += 1

  ib = 0
  for ib in range(a):
    array[ib] = 0
    ib += 1
  for ib in range(b):
    array[ib] = 1
    ib += 1
  for ib in range(c):
    array[ib] = 2
    ib += 1
  

