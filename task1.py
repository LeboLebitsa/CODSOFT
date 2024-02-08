operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter another one: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
     result = num1 / num2
     print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")