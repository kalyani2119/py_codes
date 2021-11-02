#Reverse Floyd's Triangle
" " "
example if n=5 and a=10

15
14 13
12 11 10
9  8  7  6
5  4  3  2  1

" " "
n=int(input("Enter the number of rows"))
a=0
for i in range(n):
  a=a+1
  b=n+a
  for i in range(n):
    for i in range(i+1):
      print(format(b,"<3"),end="")
      b=b-1
  print()
