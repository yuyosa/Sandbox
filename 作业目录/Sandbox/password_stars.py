min_length = 8

password = input("Please enter password：")
while len(password) < min_length:
    print("Too short! Enter again!")
    password = input("Please enter password：")

print('*' * len(password))
