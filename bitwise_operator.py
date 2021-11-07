number = int(input("Please enter the integer number:")
             i=0
             result=0
             while result<num:
             result = 1<<i
             if result == number:
               print("The entered number is power of two",i)
               break
             i=i+1;
             else:
              print("The number is not the power of 2")
             
