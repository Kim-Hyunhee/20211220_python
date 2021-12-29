num1 = int(input('숫자 입력 :'))
num2 = int(input('숫자 입력 :'))
num3 = int(input('숫자 입력 :'))

# if num1 < num2 and num1 < num3 :
#     print(num1,'이 최소값이다.')
# elif num2 <num1 and num2 <num3 :
#     print(num2,'이 최소값이다.')
# else:
#     print(num3,'이 최소값이다.')
    
# if num1 > num2 and num1 > num3 :
#     print(num1,'이 최대값이다.')
# elif num2 > num1 and num2 > num3 :
#     print(num2,'이 최대값이다.')
# else:
#     print(num3,'이 최대값이다.')
    

# num1이 제일 작다고 전제
# 최소값이 몇인지 저장할 변수 => num1을 일단 넣어두자.

min_num = num1
if min_num > num2 :
    # num2가 더 작다! 최소값을 바꾸자
    min_num = num2
if min_num > num3 :
    min_num = num3

print('최소값 :', min_num)


# num1이 제일 크다고 전제
max_num = num1
if max_num < num2 :
    max_num = num2
if max_num < num3 :
    max_num = num3
    
print('최대값 :', max_num)