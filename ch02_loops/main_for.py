'''
for 반복문 :
    원래 python에서의 default for문의 경우 enhanced for가 기본
    근데 저희 index를 다루는 것부터 시작했기에 걔를 기준으로 먼저 강의

    이때, 중요한 것은 range() 함수
'''
# 1 ~ 10 까지 출력하는 for문
for i in range(10) :
    print(i + 1)
'''
이상에서 중요한 것은 i가 0부터 시작한다는 점
range() : 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 연계되어 함께 쓰이는 편

range() 함수의 응용
range((시작값), 한계값, (증감값))

시작값 : 생략 가능, 생략하면 0부터 시작
한계값 : 명시하지 않으면 끝까지 진행
증감값 : 생략 가능, 생략할 시에 1씩 증가
'''
for i in range(1, 11, 1) :
    print(i, end=' / ')

print()
print(i)        # 결과값 : 10
'''
Java에서는 for(int = 0; ...) 어쩌고 한 부분 있을 때
System.out.println(i); 하면 오류
while에서와 마찬가지로 지역변수의 범위가 다르다는 점을 알 수 있음.

이상까지 학습했을 때 시작값 / 한계값 / 증감값을 정의하게 되는 range() 함수가 필수적

하지만 default 형태의 python
'''

nums = [1, 2, 3, 4, 5]
for i in nums:
    print(i, end=' , ')

print()

if 5 in nums:
    print('5가 리스트 내에 있음.')
else :
    print('5가 리스트 내에 없음.')
'''
그러면 자바를 배우는 저희는 익숙치 않지만 in 이라는 애가 생각보다 엄청 중요
in이 적용된 무언가의 결과값의 자료형은?
-> true / false가 나오는 '연산자'
A in B라고 했을 때 A라는 요소가 B라는 반복 가능 객체 내에 존재하는지를 
True / False로 뽑아줌
'''
print(5 in nums)    # 결과값 : True