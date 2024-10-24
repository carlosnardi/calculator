# It should work like the example above: 
"""
What's the first number: 5
+
-
*
/
Pick an operation: /
What's the next number: 2
5 / 2 = 2.5
Type 'y' to continue calculating with 2.5, or type 'n' to start a new calculation: y
Pick an operation: /
What's the next number: 2

"""
def sum(num1, num2):
  return num1 + num2

def subs(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

def getting_data():
  num1 = float(input("What's the first number: ")
  operation = input('''
  +
  -
  *
  /
  Pick an operation: ''')
  num2 = float(input("What's the next number: "))

def continue_calculating(number):
  operation = input('''
  +
  -
  *
  /
  Pick an operation: ''')
  num2 = float(input("What's the next number: "))