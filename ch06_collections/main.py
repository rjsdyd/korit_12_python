'''
python 대표 collectin 종류
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능 / 순서 있음
3. set 세트 : 중복된 값이 저장이 불가 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
# list_example = [30, 40, '김이', [100, '김삼']]
# print(list_example)
# tuple_example = (10, 20, 30, 40, '김삼')
# print(tuple_example)
# set_example = {100, 200, 300, 400, '김오'}
# print(set_example)
# dict_example = {'이름' : '김일', '나이' : 20, '학교' : '코리아아이티'}
# print(dict_example)

'''
1. list : 여러 값을 저장할 떄 가장많이 사용. 
          자료형이 서로 다르더라도 하나의 리스트에 저장 가능. 
          Java 기준 하나의 배열에 동일한 자료형만 들어갈 수있는 것과 달리 강점
'''
# list의 선언 및 초기화
# li1 = [1, 2, 3 , '김사']
'''
    1.1 list의 index / slice
        list는 str과 동일한 방식의 index / slicing을 지원
        1) 인덱스 / 마이너스 인덱스
        
'''
# print(li1[0])
# print(li1[1])
# print(li1[-1])
# print(li1[-2])
'''
    1.2 slicing
        str의 slicing과 같이 '시작 인데스 : 종료 인덱스 : 증감값'으로 이루어져 있음.
'''
# li2 = [100, 3.14, 'hello']      # list 선언 및 초기화 방법 # 1
# li3 = list((4, 5, 6, 7, 8))     # list 선언 및 초기화 방법 # 2
# print(li3[0:4:2])               # 시작 인덱스부터 4번지 앞까지, 2씩 증가
'''
    1.3 list의 element 추가와 삭제
        list에 새로운 요소를 추가할 때는 아까 한 것처럼 .append()를 사용할 수 있음.
        그리고 .insert()도 존재
        
        .append() - 항상 마지막 인덱스에 element를 추가
        .insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가
'''
# scores = [30, 40, 50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0, 90)
# print(scores)
'''
        .pop()의 경우 NoArgs라면 맨 마직막 element가 삭제됨.
        .pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 element를 삭제함
'''
# print(scores.pop())
# print(scores)
# print(scores.pop(0))
# print(scores)

'''
        교재에는 없는데 수업하는 삭제 메서드 : .remove(값) - list 내에 해당 값을 찾아내서 삭제 (인덱스가 아님)
'''
# print(scores.remove(30))
# scores.remove(50)
# scores.remove(300)
# print(scores)

'''
li4 리스트를 선언하고, 1부터 10까지 집어넣어보세요.
print(li4) 결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

각 list 내의 element들을 뽑아내서 *2씩
일반 for문 한번
향상 for문 한번
해서 첫 번째 element가 4여야 함.
'''
# 선언
li4 = []
for i in range(1, 11):
    li4.append(i)
print(li4)

# 일반 for문
for i in range(len(li4)):
    li4[i] *= 2
print(li4)

# 향상 for문
print('[', end='')
for num in li4:
    num *= 2
    if num == 40:
        print(num, end='')
    else:
        print(num, end=', ')
print(']', end='')
# 사실상 list 내에서의 element들에 대해 연산을 일괄적으로 적용하는 method가 따로 있음.
# 그리고 우리는 그것을 JS에서 해봄.

print()
modified_li4 = list(map(lambda num : num*2, li4))
# 이상의 경우가 극단적으로 list의 내부 element들에 동일한 함수를 적용한 결과를 적용하는 map() 함수임.
# 그런데 저희는 JS에서 배열의 method로 사용함.
# 이상의 코드가 좀 문제가 있다면 map() 함수의 결과값이 map 객체에 해당하기에 list() 함수를 통한 형병환을 해줘야 함.
print(modified_li4)

'''
    2. tuple(튜플) : 저장된 값을 변경할  수 없는 list라고 생각하시면 됨.
                     순서는 있기에 index 넘버의 사용과 slicing은 사용 가능하나
                     추가 / 삭제 / 수정이 불가능
'''
tu1 = (1, 2, 3)             # 튜플 생성 방법 # 1
tu2 = tuple((4, 5, 6))      # 튜플 생성 방법 # 2
tu3 = 7, 8, 9               # 튜플 생성 방법 # 3

print(tu3)
print(type(tu3))            # 결과값 : <class 'tuple'>
a, b, c = 7, 8, 9
# 복수의 변수 선언 및 초기화 방법 -> 변수 개수와 데이터 개수가 같으면 알아서 '순서대로' 대입

tu4 = 0
print(type(tu4))            # 결과값 : <class 'int'>

tu5 = 'Hello. ', 'good morning. ', 'my name is ', 'kim-il ', 'i am ', '20 ', 'years old'
for word in tu5:
    print(word.title(), end='')
    # 결과값 : Hello. Good Morning. My Name Is Kim-Il I Am 20 Years Old

print()
'''
이상의 예시를 남겨두는 이유는 우리가 배우는 collection의 개념과 내부 element의 자료형이 서로 다르다는 점.
tuple 자체는 추가 / 수정 / 삭제가 불가능했음.
그런데 내부 element 자체는 str이니까 데이터의 가공이 가능
'''

'''
    3. set 세트
        : 수학의 집합 개념 , Java와 동일
'''
set1 = {1, 2, 3}        # 세트 생성 방법 # 1
set2 = set({4, 5, 6})   # 세트 생성 방법 # 2

# 비어있는 list / tuple / set 생성 방법
li = []
tu = ()
se = {}
print(type(li))     # 결과값 : <class 'list'>
print(type(tu))     # 결과값 : <class 'tuple'>
print(type(se))     # 결과값 : <class 'dict'>

# 그래서 set 비어있는 것은
se1 = set({})
print(type(se1))    # 결과값 : <class 'set'>

'''
    set 관련 메서드
    1. .add() - set에 새로운 element 추가
    2. .remove() - 기존 element 삭제 -> index가 없으니 .pop()이 없음.
    3. .discard() - 기존 element 삭제
'''

se3 = {10, 20, 30}
se3.add(50)
print(se3)      # 결과값 : {10, 20, 50, 30}
se3.remove(30)  # 순서가 없기에 '값'을 정확히 입력해야 함.
print(se3)      # 결과값 : {10, 20, 50}

# remove() vs discard()
# se3.remove(70)        # 얘는 오류 발생
# print(se3)
se3.discard(70)         # 얘는 오류 발생 안함.
print(se3)

'''
.remove()의 경우 argument로 set 내에 있는 값을 정확하게 입력하지 않으면 KeyError 예외가 발생
반면 .discard()의 경우에는 set내에 없는 값을 입력했을 경우 해당 값이 애초에 존재하지 않기에 
변함 없는 상태로 메서드가 종료
'''
# 인덱스 넘버는 없지만 향상된 for문으로 내부 element를 출력할 수 있음.
for num in se3:
    print(num)          # 순서는 담보 못함.
'''
    4. dict(ionary) - 자바에서의 Map / Js에서의 Object / JSON과 비슷한 형식
'''

dict1 = {
    '이름' : '김일',
    '나이' : 20,
    '주소' : ['서울특별시', '마포구', '목동'],
}
'''
나중에 확장성을 위해서 미리 ,를 쳐두는 편입니다. 그러면 그냥 추가 property를 넣으면 되니....

정말 * 3 중요하게 제가 반복적으로 언급하는 부분 dictionary에서 반복문 돌리면 key가 나옴.
'''
for key in dict1:
    print(key)

# 그렇다면 value를 확인하기 위해서는
for key in dict1:
    print(dict1[key])       # *** 매우 *** 중요

# key들만 추출하는 메서드
print(dict1.keys())
print(type(dict1.keys()))       # <class 'dict_keys'>
print(list(dict1.keys()))       # ['이름', '나이', '주소']
print(dict1.values())
print(type(dict1.values()))     # <class 'dict_values'>

# key들 혹은 value들만 뽑아서 list를 만들고 싶다면 list() 형변환 함수를 사용해야 함.

'''
그래서 collections 수업을 할 때 ***매우*** 중요한 점은 list를 배웠을 때 list만 고려할 것이 아니라
set / tuple / dictionary로 자료형을 변경하는 것이 가능한가임.

    1) dictionary에서 property 추가 / 삭제
'''
dict1['직업'] = '웹 퍼블리셔'       # 기존에 없는 key를 입력하고 = value 하면 됨
print(dict1)
dict1['직업'] = '웹 개발자'         # key 하나 당 value는 동일하기에 재대입이 이루어집니다.
print(dict1)

print(dict1.pop('직업'))            # key를 알아야지 삭제가 가능
# .pop()의 return 특성이 중요
# 그러면 최종 value가 뽑혀져 나올테니 결과값 : 웹 개발자

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그
list에서 2 번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40
'''
li_ex = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sub_list = li_ex[2:7]
second_element = sub_list[1]
print(sub_list)
print(second_element)

'''
사용자로부터 1에서 12까지의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성
(윤년은 고려X)

실행 예)
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지 입니다.
# 1 : dictionary를 이용하는 방법
# 2 : list를 이용하는데 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]을 이용하는 방법
# 3 : list를 이용하는데 [28, 30, 31]을 이용하는 방법 
'''
# 1 : dictionary를 이용하는 방법
month_days_dict = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))
if month in month_days_dict:
    print(f"{month}월은 {month_days_dict[month]}일까지 입니다.")
else:
    print("잘못된 입력입니다.")

# 2 : list를 이용하는데 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]을 이용하는 방법
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))

if 1 <= month <= 12:
    print(f"{month}월은 {days_list[month - 1]}일까지 입니다.")
else:
    print("잘못된 입력입니다.")

# 3 : list를 이용하는데 [28, 30, 31]을 이용하는 방법
days_28 = [2]
days_30 = [4, 6, 9, 11]
days_31 = [1, 3, 5, 7, 8, 10, 12]

month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))

if month in days_28:
    res = 28
elif month in days_30:
    res = 30
elif month in days_31:
    res = 31
else:
    res = None

if res:
    print(f"{month}월은 {res}일까지 입니다.")
else:
    print("잘못된 입력입니다.")

'''
이상의 코드 라인에서 중요한 것은 in 개념입니다.
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체(iterable)이 올 수 있다는 점입니다.
그래서 
elif month_int in [ 1, 3, 5, 7, 8, 10, 12 ]:
    last_date = last_date_list2[2]
의 해석 부분이 중요한데, in 다음에 임의의 list를 초기화하여 month_int가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토했다고 해석할 수 있겠습니다.

( 1, 3, 5, 7, 8, 10, 12 ) 이렇게 초기화하더라도 전혀 문제가 없겠네요. tuple로 집어넣은 사례가 되겠습니다.

응용 예제
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.

짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장하세요.
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20, 25, 30]입니다.
입력 받은 숫자들 중 짝수는 [10, 20, 30]입니다.
'''
# 1. 수학여행지 조사
destinations = set()

for i in range(3):
    place = input("희망하는 수학여행지를 입력하세요 >>> ")
    destinations.add(place)

print()
print(f"조사된 수학여행지는 {destinations}입니다.")
print(f"조사된 수학여행지는 {list(destinations)}입니다.")

# 2. 짝수만 추출하기
li_original = []
li_even = []
for i in range(int(input('몇 개의 숫자를 입력할까? >>> '))):
    num = int(input(f'{i+1}번째 숫자를 입력하세요 >>> '))
    li_original.append(num)
for num in li_original:
    if num % 2 == 0:
        li_even.append(num)
print(f"전체 리스트: {li_original}")
print(f"짝수 리스트: {li_even}")
'''
딕셔너리 기반의 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름의 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름의 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름의 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.


collections + function

숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)          # call2() 유형
print(add_numbers2(last_num))   # call4() 유형

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]

예를 들어 hello = ['안', '녕', '하', '세', '요']라는 list가 있다고 가정했을 때,
add_numbers3(10, hello)를 호출하면
[1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
라는 결과값을 만드는 함수를 정의한다면 어떻게 할 수 있을지 고민해보세요.
'''