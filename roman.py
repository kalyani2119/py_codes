# integer number to roman number conversion
def roman_numbers(number):
  if number>3999:
    print("Please enter the number less than 3999")
    return
  value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
  symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
  roman=""
  i=0
  while number>0:
    div=number//value[i]
    number=number%value[i]
    while div:
      roman=roman+symbol[i]
      div=div-1
  i=i+1
  return roman
number=int(input("Please enter an integer number"))
print("roman number of ",number,"is",roman_numbers(number))
