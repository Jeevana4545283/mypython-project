def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("slect operation:")
print("1.Addition(+)")
print("2.subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

choice=input("enter choice(1/2/3/4):")

if choice in ['1', '2', '3','4']:
    try:
        num1=float(input("enter 1st number:"))
        num2=float(input("enter 2nd number:"))
        if choice=='1':
            print("result:",add(num1,num2))
        elif choice=='2':
            print("result:",subtract(num1,num2))
        elif choice=='3':
            print("result:",multiply(num1,num2))
        elif choice=='4':
            result=divide(num1,num2)
            print("result:",result)
    except ValueError:
                   print("Error: please enter valid numbers.")
else:
   print("invalid input. please choose a valid operation(1-4).")