num1 = 12
num2 = 15

# num1에 들어있는 값을 미리 복사 (백업)
back_up = num1

num1 = num2

# 미리 백업해둔 back_up에 잇는 값을 대신 num2에 대입
num2 = back_up


print(num1)
print(num2)