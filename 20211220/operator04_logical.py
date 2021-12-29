is_tall = False
is_rich = True

is_man = False

height = 183.5

money = 250000

# 키도 크고 (키가 180 이상), 부자이기도 ( money가 100000 이상) 한 사람 OK
result01 = height >= 180 and money >= 100000
print('결과 1 and :', result01)


# 키가 크거나 부자이거나 하나라도 되면 OK
result02 = is_tall or is_rich
print('결과 2 or :', result02)

# 남성만 아니면 OK
result03 = not is_man
print('결과 3 not :', result03)