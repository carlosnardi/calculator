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

def continue_calculating():
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

while True:
  data = getting_data()
  num1 = data[0]
  num2 = data[1]
  operation = data[2]
  first_result = calculating(num1, num2, operation)
  print(first_result)
  
  continue_calc = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to start a new calculation:\n")
  while continue_calc == "y":
    data_to_continue = continue_calculating()
    num2 = data_to_continue[0]
    operation = data_to_continue[1]
    second_result = calculating(first_result, num2, operation)
    print(second_result)
    continue_calc = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to start a new calculation:\n")