def count_minus(str):
    return sum(1 for i in str if int(i) < 0)

x = input("Input: ").split()
print(count_minus(x))
