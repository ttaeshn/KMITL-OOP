def delete_minus(lst):
    return [[num for num in sub_lst if num >= 0] for sub_lst in lst]

x = []
num_lists = int(input("Enter the number of sublists: "))
for i in range(num_lists):
    sublist_input = input(f"Enter sublist {i+1} elements: ")
    sublist = eval(sublist_input)
    x.append(sublist)

output = delete_minus(x)
print("Output:", output)
