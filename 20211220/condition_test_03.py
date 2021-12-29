score1 = int(input('첫 번째 과목 점수 :'))
score2 = int(input('두 번째 과목 점수 :'))
score3 = int(input('세 번째 과목 점수 :'))

average = (score1 + score2 + score3) / 3

# if score1 >= 40 and score2 >= 40 and score1 >= 40:
#     print("과락은 되지 않았습니다.")
#     if average >= 60:
#         print('합격입니다.')
#     else :
#         print('불합격입니다.')
# else : 
#     print("40점 미만인 점수가 있으므로 불합격입니다.")
    
    
# if score1 < 40 or score2 < 40 or score1 < 40:
#     print("40점 미만인 점수가 있으므로 불합격입니다.")
    
# else:
#     if average >= 60:
#         print('합격입니다.')
#     else :
#         print('불합격입니다.')


if average >= 60:
    if (score1 >= 40) and (score2 >= 40) and (score3 >= 40) :
        print('합격')
    else :
        print('과락으로 불합격')
else:
    print('불합격')    
    
    