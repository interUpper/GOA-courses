#დავალება 1

num1 = float(input("გთხოვთ შეიყვანოთ ტემპერატურა ცელსიუსში ფარენჰეიტში გადაყვანისთვის: "))
num1 = num1 * 1.8 + 32

print(num1)

#დავალება 2

user_age = int(input("თქვენი ასაკი: "))
print(user_age < 20 and user_age > 12)

#დავალება 3

rec1 = float(input("გთხოვთ შემოიტანოთ პირველი გვერდის სიგრძე: "))

rec2 = float(input("გთხოვთ შემოიტანოთ მეორე გვერდის სიგრძე: "))

s = rec1 * rec2

print(s)

#დავალება 4

user_num = int(input("გთხოვთ შემოიტანეთ 100_ზე მეტი რიცხვი რომელიც იყოფა 9 ზე: "))

print(user_num > 100 and user_num % 9)

