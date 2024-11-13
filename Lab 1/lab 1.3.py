import math
hr_in,min_in,hr_out,min_out = [int(e) for e in input("Input: ").split()]

all_min_in = hr_in*60 + min_in
all_min_out = hr_out*60 + min_out

sum_min = all_min_out - all_min_in

time = 0
ans = 0

if (hr_in < 7 or hr_out > 23 or min_in > 60 or min_in < 0 or min_out > 60 or min_out < 0 or sum_min < 0):
    print("Error")
else:
    if sum_min <= 15:
        print("0")
    elif 15 < sum_min <= 180:
        if all_min_out > 1380:
            print("Overtime")
        else:
            time = math.ceil(sum_min / 60)
            ans += (10*time)
            print(ans)
    elif 180 < sum_min <= 360:
        if all_min_out > 1380:
            print("Overtime")
        else:
            time = math.ceil(sum_min / 60)
            repeat_money = (20*time) - 30
            ans += repeat_money
            print(ans)
    elif 360 < sum_min <= 960:
        if all_min_out > 1380:
            print("Overtime")
        else:
            print("200")
    else:
        print("Overtime")
