num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
str = """
Press 1 for Addition
Press 2 for Subtraction
Press 2 for Multiplication
Press 4 for Division
Press 5 for Power                   
"""
print(str)
def addition():
     print(num1+num2)
def Substraction():
     print(num1-num2)
def Mul():
     print(num1*num2)
def Div():
    print(num1 / num2)
def power():
    print(num1**num2)

choice = int(input("Enter your choice: "))
if(choice == 1):
    addition()
elif(choice == 2):
    Substraction()
elif(choice == 3):
    Mul()
elif(choice == 4):
    Div()
elif(choice == 5):
    power()
