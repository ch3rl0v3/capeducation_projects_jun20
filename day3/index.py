email = input("Enter your email: ")
place = email.find("@")
length = len(email)
domen = email[place+1:length]
print("Domen of your email is: " + domen)