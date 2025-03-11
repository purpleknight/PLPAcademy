# PLPAcademy
Kelvin Gitaka PLP Academy Assignment Repo
# Create a Simple Python Program that asks the users to input two numbers and a mathematical operation(addition, subtraction, multiplication or division)
Num1 = int(input('Enter the first number: '))
Num2 = int(input('Enter the second number: '))

def add(Num1, Num2): 
    return Num1 + Num2

def subtract(Num1, Num2):
    return Num1 - Num2

def multiply(Num1, Num2):
    return Num1 * Num2

def divide(Num1, Num2):
    return Num1 / Num2

print(f'The addition of your numbers is: ', add(Num1, Num2))
print(f'The subtraction of your numbers is: ', subtract(Num1, Num2))    
print(f'The multiplication of your numbers is: ', multiply(Num1, Num2))
print(f'The division of your numbers is: ', divide(Num1, Num2))
