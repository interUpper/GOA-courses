#davaleba 1

answer = input("which coding academy were u studying : ")
if answer == "GOA":
    print("u made great choice!")
else:
    print("u made wrong choice!")

#davaleba 2
buget = float(200)
print("u have ", buget , " to spend")
product1 = float(input("input first product price: "))
product2 = float(input("input second product price: "))

if product1 + product2 <= buget :
    print("money is enough!!!")
else:
    print("u need more money!!")

#davaleba 3
userinput = int(input("if its below 5 it'll multyply by 2. if its bigger number than 5 it'll multyply by 4 :) :"))
if userinput <= int(5):
    print(userinput * 2)
else:
    print(userinput * 4)

#davaleba 4
price = float(10)
discount = float(7)
need = float(input("input how mant tkt u need: "))
if need < 5 :
    print(need * price)
elif need >=5 :
    print("price is : ", need * discount)



#davaleba 5
number1 = float(input("first number : "))

symbol = input("operation: ")

number2 = float(input("second number : ")) 

if symbol == "/":
    print(number1 / number2)
elif symbol == "*":
    print(number1 * number2)
elif symbol == "-":
    print(number1 - number2)
elif symbol == "+":
    print(number1 + number2)
else :
    print("you made mistake somewhere!!!")