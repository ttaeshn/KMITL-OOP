def add2list(lst1, lst2):
    if len(lst1) != len(lst2): return "Error"
    else: return [x + y for x, y in zip(lst1, lst2)]

input1 = input()
list1 = list(map(int, input1.split()))
input2 = input()
list2 = list(map(int, input2.split()))
print(add2list(list1,list2))
