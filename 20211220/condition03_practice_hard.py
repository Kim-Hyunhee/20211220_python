birth_year = int(input('출생년도 입력 : '))
age = 2021 - birth_year + 1

if age >= 20:
    print('성인입니다.')
elif age >= 8:
    print('학생입니다.')
else :
    print('미취학 아동입니다.')