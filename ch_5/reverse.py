message = "Why do we fall Bruce? so we can learn to pick ourselves up."

encrypted = ""

i = len(message) - 1


while i >= 0:
    encrypted += message[i]
    i -= 1


print(encrypted)
