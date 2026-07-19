number = 90
guess = int(input("Угадайте число от 1 до 100: "))
while guess != number:
    print("Неправильно")
    if guess < number:
        print("Загаданное число больше")
    elif guess > number:
        print("Загаданное число меньше")
    guess = int(input("Попробуйте снова: "))
print("Вы угадали число!")

height = int(input("Введите высоту вашей пирамиды: "))
num = 1
for i in range(1, height + 1):
    for j in range(i):
        print(num, end=" ")
    print() 
    num += 1