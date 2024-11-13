def is_leap(year):return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_in_year(day, month, year):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month == 2 and day == 29 and not is_leap(year):
        return "Error"
    total_days = day
    for m in range(1, month):total_days += days_in_month[m]
    if month > 2 and is_leap(year):total_days += 1

    return total_days

d,m,y = [int(e) for e in input("Input: ").split()]
print(f"Output for date: {day_in_year(d, m, y)}")