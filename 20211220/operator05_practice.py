# 연습문제

# 회사의 채용 조건
salary = 3800
minutes = 70  # 1시간 10분 걸리는 거리
over_work = True


# 지원자 1이 회사를 보는 기준 : 연봉이 4천 이상이면 OK

result01 = salary >= 4000
print(result01)

# 지원자 2가 회사를 보는 기준 : 거리가 20분 이내면 OK

result02 = minutes < 20
print(result02)

# 지원자 3 : 야근만 없으면 OK

result03 = not over_work
print(result03)

# 지원자 4 : 연봉 3500 이상 + 거리도 50분 이내

result04 = (salary >= 3500) and (minutes < 50)
print(result04)

# 지원자 5 : 연봉 5000 이상 이거나 거리 80분 이내

result05 = (salary >= 5000) or (minutes < 80)
print(result05)

# 지원자 6 : 연봉 4000 이상이거나 야근이 없거나

result06 = (salary >= 4000) or (not over_work)
print(result06)