def only_english(string1):
    return [i for i in string1 if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)]

x = str(input("Input: "))
for i in only_english(x): print(i,end="")