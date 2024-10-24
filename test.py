 """
#### It should work like the example above: ####
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

def test(a,b):
  result1 = a + 1
  result2 = b + 1
  return result1, result2

result_one = test(1,2)[0]
print(test(1,2))
print(result_one)
