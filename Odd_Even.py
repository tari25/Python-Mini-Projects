#checking if a given number is odd or even

print("Enter numbers below. Use 'end' to indicate the end of the list.")
num = input()
while num != "end": 

    if int(num)%2 == 0: #mod function used to find remainder
        print(num, "is even")
    else:
        print(num, "is odd")
    num = input()
