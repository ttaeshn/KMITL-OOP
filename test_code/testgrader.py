def checking_survivor(num_list):
    print(num_list)
    temp_list = []
    if len(num_list) % 2 == 1:
        for index in range(len(num_list)):
            if (index + 1) % 2 == 1:
                temp_list.append(num_list[index])
        
    print(temp_list)
    
    if len(temp_list) == 2 and len(num_list) % 2 == 1:
        return "HI"
    elif len(temp_list) == 3 and len(num_list) % 2 == 0:
        return temp_list[1]
    else:
        return checking_survivor(temp_list) 

num = int(input("Enter a number: "))
num_list = []

for i in range(num):
    num_list.append(i+1)

print(checking_survivor(num_list))
