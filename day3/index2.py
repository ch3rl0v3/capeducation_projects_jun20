age = int(input("Enter your age: "))
if age < 18:
    print("Вы не можете получить права")
else: 
    print("Вы можете получить права")

your_apples = int(input("Сколько у вас яблок? "))
your_friends_apples = int(input("Сколько яблок у вашего друга? "))
if your_apples > your_friends_apples:
    print("У вас больше яблок, чем у вашего друга")
elif your_apples < your_friends_apples:
    print("У вашего друга больше яблок, чем у вас")
else:
    print("У вас и вашего друга одинаковое количество яблок")