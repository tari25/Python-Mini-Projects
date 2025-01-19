num1 = int(input("Enter first numebr: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation symbol. +(add), -(subtract), *(multiply), /(divide): ")
ans = float 

#calculations based on chsen operation
if operation == "+":
    ans = num1 + num2
elif operation == "-":
    ans = num1 - num2
elif operation == "*":
    ans = num1 * num2
elif operation == "/":
    if num2 != 0:
        ans = num1 / num2
    else:
        print("Error! Division by zero is not allowed.")

print("The answer is: ", ans)
