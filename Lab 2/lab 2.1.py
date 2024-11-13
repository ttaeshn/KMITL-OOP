input_list = [int(e) for e in input().split()]
sorted_list = sorted(input_list)
swap_number = 0

if sorted_list[0] == 0:
    swap_number = sorted_list[0]
    sorted_list[0] = sorted_list[1]
    sorted_list[1] = swap_number

for i in range(len(sorted_list)):
    print(sorted_list[i],end='')