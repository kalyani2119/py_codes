num=int(input("Enter the number"))
print("You have entered:",num)
for i in range(2,num):
  if num%i==0:
    print("NOT PRIME NUMBER")
 else:
   print("PRIME NUMBER")
