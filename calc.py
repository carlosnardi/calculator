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
def getting_data():
  num1 = float(input("What's the first number: "))
  operation = input('''
  +
  -
  *
  /
  Pick an operation: ''')
  num2 = float(input("What's the next number: "))
  return num1, num2, operation

def continue_calculating(number):
  operation = input('''
  +
  -
  *
  /
  Pick an operation: ''')
  num2 = float(input("What's the next number: "))
  return num2, operation

def calculating(num1, num2, operation):
  if operation == '+':
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/": 
    return num1 / num2
    

data = getting_data()
num1 = data[0]
num2 = data[1]
operation = data[2]

first_result = calculating(num1, num2, operation)
print(first_result)

#continue_calc = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to start a new calculation:\n")
#if continue_calc == "y":
 # continue_calculating(first_result)