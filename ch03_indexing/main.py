str_example = 'Hello, Python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])

print(len(str_example))     # 결과값 : 14

# 일반 for문으로 Hello, Python!을 한줄로 출력하세요.
for i in range(len(str_example)):
    print(str_example[i], end='')

print()
# 향상 for문으로 한줄로 출력하세요.
for i in str_example:
    print(i, end='')

'''
마이너스 인덱스 : 문자열의 뒤에서부터 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱 : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 추출하는 것이 가능

형식 :
변수명 [ 시작인덱스 : 종료인덱스 : 증감값 ]
시작 인덱스 : 생략하면 처음부터 추출
종료 인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 증가 (인덱스 넘버가 0부터 1씩 증가한다는 의미
'''
print()
print(str_example[:-3:])
print(str_example[-0])
print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])

'''
근데 잘 생각해보면 range(시작값, 종료값, 증감값)이랑 
변수명 [시작인덱스 : 종료인덱스 : 증감값]이랑 같아보임.
실행 예)
네 자리 숫자를 입력하세요
맨 마지막 숫자는 6입니다.
'''

number = input('네 자리 숫자를 입력하세요. >>> ')
print(f'맨 마지막 숫자는 {number[3:4:1]}입니다')
# if number % 2 == 0:
#     print(f'맨 마지막 숫자는 {number[3:4:1]}이며, 짝수입니다.')
# else :
#     print(f'맨 마지막 숫자는 {number[3:4:1]}이며, 홀수입니다.')
if int(number[-1]) % 2 == 0:
    print(f'맨 마지막 숫자는 {number[-1]}이며, 짝수입니다.')
else :
    print(f'맨 마지막 숫자는 {number[-1]}이며, 홀수입니다.')

'''
python 삼항 연산자
if - else 구조를 한줄로 줄여 사용
'''
result = '짝수' if int(number[-1]) % 2 == 0 else '홀수'
print(f'맨 마지막 숫자는 {number[-1]}이며, {result}입니다.')

def multiply(n):
    for i in range(1, 10):
        print(f'{n} X {i} = {n*i}')

dan = int(input('몇단을 출력할것? >>>'))
multiply(dan)

