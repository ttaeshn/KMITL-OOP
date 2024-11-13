def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): return True
    else: return False

def isnt_valid_date(day, month, year):
    if day < 1 or day > 31 or month < 1 or month > 12: return True
    elif month in [4, 6, 9, 11] and day > 30: return True
    elif month == 2:
        if (is_leap(year) and day > 29) or (not is_leap(year) and day > 28): return True
    return False

def day_of_year(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year): days_in_month[2] = 29

    if month == 2 and day > days_in_month[2]: return -1

    day_count = sum(days_in_month[0:month]) + day
    return day_count

def days_in_year(year):
    if is_leap(year): return 366
    else: return 365

def date_diff(date1, date2):
    day1, month1, year1 = map(int, date1.split('-'))
    day2, month2, year2 = map(int, date2.split('-'))

    if isnt_valid_date(day1, month1, year1) or isnt_valid_date(day2, month2, year2):
        return -1
    else:
        days_count1 = day_of_year(day1, month1, year1)
        days_count2 = day_of_year(day2, month2, year2)

        if year1 == year2: return abs(days_count1 - days_count2) + 1
        else:
            days_between_years = 0
            days_between_years += days_in_year(year1) - days_count1
            for year in range(year1 + 1, year2):
                days_between_years += days_in_year(year)
            days_between_years += days_count2
            return days_between_years + 1

date = input("Input: ").split()
print(date_diff(date[0], date[1]))