grade = int(input("몇 학년인가요? : "))
score = int(input("점수가 어떻게 되나요? : "))

if score > 100 or score < 0 :
    print("잘못된 점수입니다.")
else :
    if grade == 1 and score >= 60:
        print("합격입니다.")
    elif grade == 1 and score < 60:
        print("불합격입니다.")
    if grade != 1 and score >= 70:
        print("합격입니다.")
    elif grade != 1 and score < 70:
        print("불합격입니다.")
        

grade = int(input("몇 학년인가요? : "))
score = int(input("점수가 어떻게 되나요? : "))

# 점수가 0 <= 점수 <= 100 이 범위 안에 들어있는가?

if 0 <= score and score <= 100:
    # 그래서 몇 학년인지 보고 -> 점수에 따른 합격/ 불합격 출력
    print('정상 점수 입력')
    
    if grade == 1:
        if score >= 60:
            print('합격 - 1학년')
        else :
            print('불합격 - 1학년')
    else :
        # 2~3gkrsus ruddn
        if score >= 70:
            print('합격 - 2~3학년')
        else :
            print('불합격 - 2~3학년')
else :
    # 점수가 범위를 벗어남 => 잘못된 입력
    print('잘못된 점수가 입력됐습니다.')
