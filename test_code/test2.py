num_list = []
nums = [int(e) for e in input().split()]
num_list.extend(nums)

for start in range(len(num_list) - 1):
    for count in range(start + 1, len(num_list)):
        if num_list[start] + num_list[count] == num_list[-1]:
            print([start, count])
        else:
            count = count + 1
    start = start + 1
