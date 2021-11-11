print("FACTORIAL PROGRAM")
a=int(input("Please enter a number"))
fact=1
for i in range(1,a+1):
  fact=fact*i
  print("factorial of {0} is {1}".format(a,fact))
