import random

caracters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

cantidad = int(input("cuantos caracters hay?"))

password = ""

for i in range(cantidad):
    password += random.choice(caracters)

print(password)
