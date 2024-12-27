message = input("enter the string:")
index = 0
while index < len(message) :
    letter = message[index]
    print(chr(ord(letter)+ 3),end=' ')
    index += 1
