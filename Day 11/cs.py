symbol = input("operation: ")

number1 = float(input("first number : "))

number2 = float(input("second number : ")) 

number3 = float(input("input third number: "))

if symbol == "/":
    print(number1 / number2 / number3)
elif symbol == "*":
    print(number1 * number2 * number3)
elif symbol == "-":
    print(number1 - number2 - number3)
elif symbol == "+":
    print(number1 + number2 + number3)
else :
    print("you made mistake somewhere!!!")