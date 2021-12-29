score = int(input('점수 : '))

if score >= 90:
    rank = int(input('등수 :'))
    
    if rank <= 5:
        print('A+ 입니다.')
    else :
        print('A0 입니다.')
elif score >= 80:
    print('B 입니다.')
elif score >= 70:
    print('C 입니다.')
else:
    print('F 입니다.')