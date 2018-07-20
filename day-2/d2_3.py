year = int(input('year = '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

if is_leap:
    print("%d is leap year" % year)
else:
    print("%d is not leap year" % year)
