# *-* coding: UTF-8 *-*

score = float(input('score = '))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('Grade: %s' % grade)
