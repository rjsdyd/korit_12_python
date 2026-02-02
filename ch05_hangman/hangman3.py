# 초기 설정
import random
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)
'''
''.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐 str로 만들어주는 method
'''
# temp = ['s', 'q', 'l', 'd']
# test = ''.join(temp)
# print(test)
# test = '/'.join(temp)
# print(test)
# test = ' '.join(temp)
# print(test)

# todo - 1 : 사용자가 추측을 반복할 수 있도록 while 반복문 작성.
# 사용자가 chosen_word의 모든 문자열을 맞추었을 때, 즉 display에 '_'가 없을 때
# 반복문을 중단시킬 겁니다. 반복문 종료 후 '정답입니다!'를 출력하도록 작성

# 풀이 # 1
# while '_' in display:
# 풀이 # 2
while ''.join(display) != chosen_word:
    guess = input('알파벳 하나 추측해서 입력 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(' '.join(display))

print('정답입니다! 🎶')
# todo - 2 : 정답을 보여줄 때 apple 라면 a p p l e 로 출력할 수 있도록 .join() 메서드를 활용
