year = int(input('윤년인지 확인하고 싶은 연도를 입력하세요 >>> '))
if year % 4 == 0 :
    print('윤년입니다.')
elif year % 100 == 0:
    print('윤년이 아닙니다.')
elif year % 400 == 0:
    print('윤년입니다')
else :
    print('윤년이 아닙니다')
print(year)

# 논리 연산자 사용
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f'{year}은 윤년입니다')
else :
    print(f'{year}은 윤년이 아닙니다.')