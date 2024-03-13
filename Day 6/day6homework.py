#მომხმარებელს შემოაქვს მთელი რიცხვი *ცვლადი*
input1 = int(input("write first number: "))

input2 = int(input("write second number: "))

#გადავამუშავოთ მომხმარებლის შემოტანილი ცვლადი(input1)

converted = float(input1)

print(converted == input2)

# მეტობის ოპერაციები

print("< ოპერაციები: ")

print(input1 > input2)
print(51 > 21)
print(12 > 11)
print(74 > 70)
print(715 > 914)

#ტოლია ან მეტიას ოპერაციები

print(">= ოპერაციები: ")

print(converted >= input2)
print(31 >= 31)
print(95 >= 60)
print(1 >= 11)
print(14 >= 54)

#ნაკლებობის ოპერაციები

print("< ოპერაციები: ")

print(converted < input2)
print(91 < 41)
print(14<17)
print(86<154)
print(11 < 11)

#ტოლიობის ან ნაკლებობის ოპერაციები

print("<= ოპეაციები: ")

print(converted <= input2)
print(51 <= 61)
print(73 <=21)
print(15 <=15)
print(1 <= 0)

#შედარების ოპერაციები

print("== ოპერაციები ")

print(converted == input2)
print(51 == 123)
print(761 == 657)
print(14 == 14)
print(91 == 91)

#შედარების(!=) ოპერაციები

print(converted != input2)
print(41 != 541)
print(51 != 51)
print(83 != 72)
print(624 != 624)

#მომხმარებლის მიერ შემოტანილ რიცხვზე ოპერაციების გაკეთება

new_input = float(input("please write number again: "))

new_input2 = float(input("please write number that you want to compare: "))

print(new_input > new_input2)
print(new_input >= new_input2)
print(new_input < new_input2)
print(new_input <= new_input2)
print(new_input == new_input2)
print(new_input != new_input2)

#მომხმარებლის რიცხვის შედარება მასზე 10 ჯერ უფრო დიდ რიცხვზე

number = float(input("please write number that will multiply on 10: "))
number10 = number * 10

print(number > number10)
print(number >= number10)
print(number < number10)
print(number <= number10)
print(number == number10)
print(number != number10)

# str და float ინფუთი

intn = int(input("write number(integer): "))
floatn = float(input("write number(float): "))

print("int type: ",  type(intn), "float type: ", type(floatn))

print(intn == floatn)
print(intn != floatn)