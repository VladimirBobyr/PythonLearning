def is_leap(year):
    leap = False

    # Write your logic here
    if ((year%4) or (year%400)) and (not (year%100)):
        leap = True

    return leap

year = int(input())
print(is_leap(year))
