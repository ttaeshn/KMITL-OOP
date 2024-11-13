string = input()
length = len(string)
upper_letter = 0
lower_letter = 0
count = 0

while count < length:
    if string[count].isupper():
        upper_letter += 1
    elif string[count].islower():
        lower_letter += 1
    count += 1
else:
    print(lower_letter)
    print(upper_letter)