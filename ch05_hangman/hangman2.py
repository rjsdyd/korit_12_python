import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

# todo -1 : 비어있는 list인 display를 만드시오.
display = []
# list에 element를 추가하는 메서드 : .append()
# display.append('김')
# display.append('영')
# print(display)
# display[1] = 1      # 얘는 인덱스가 생겼기에 가능
# print(display)
# display[4] = 4      # 얘는 인덱스가 없기에 불가능
# print(display)

# todo - 2 : 이상의 코드 라인을 참조하여 chosen_word의 각 문자 개수마다 '_'를 추가하시오.
# 예를 들어 chosen_word == 'apple' 라면 display = ['_', '_', '_', '_', '_']로 만들어져야 함.
for _ in range(len(chosen_word)):       # '_' 이것은 인덱스 넘버를 쓰지 않는다는 뜻, 반복횟수만 컨트롤 한다는 뜻.
    display.append('_')
print(display)
# todo - 3 : chosen_word의 각 문자들을 반복시켰을 때 그 위치가 guess와 일치한다면 해당 위치의 display에 문자를 공개
# 예를 들어 chosen_word가 apple이고 guess == 'p' 라면 display = ['_', 'p', 'p', '_', '_']로 바꿔야 함.

# 특정 인덱스에 있는 '_'를 guess로 대입해줘야 함.
# chosen_word[i]가 guess와 일치한다면 display[i]를 guess로 재대입
guess = input('알파벳 하나 추측해서 입력 >>> ').lower()
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:         # 일치한다면 ==
        display[i] = guess              # 재대입 =
print(display)