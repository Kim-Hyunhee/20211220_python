num1 = 15
num2 = 20

back_up = num1

num1 = num2
num2 = back_up

print(num1)
print(num2)

grade = int(input('몇 학년인가? :'))
score = int(input('몇 점인가? :'))

if score < 0 or score> 100 :
    print('잘못된 점수 입니다.')
else :
    if grade == 1 :
        if score >= 60:
            print('합격')
        else :
            print('불합격')
    else:
        if score >= 70:
            print('합격')
        else:
            print('불합격')

score1 = int(input('첫 번째 과목 점수 :'))
score2 = int(input('두 번째 과목 점수 :'))
score3 = int(input('세 번째 과목 점수 :'))

average = (score1 + score2 + score3) / 3

if (score1 < 40) or (score2 < 40) or (score3 < 40):
    print('과락으로 불합격입니다.')
else :
    if average >= 60:
        print('합격')
    else:
        print('불합격')

num1 = int(input('숫자입력 :'))
num2 = int(input('숫자입력 :'))
num3 = int(input('숫자입력 :'))

min_num = num1
if min_num > num2:
    min_num = num2
if min_num > num3:
    min_num = num3

print(min_num)

max_num = num1
if max_num < num2 :
    max_num = num2
if max_num < num3:
    max_num = num3

print(max_num)