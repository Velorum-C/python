result = input("Expression: ")
expression = result.split()
x, y, z = float(expression[0]), expression[1], float(expression[2])
if y == "+":
    ans = x + z
if y == "-":
    ans = x - z
if y == "*":
    ans = x * z
if y == "/":
    ans = x / z
print(f"{result} is {ans}")
