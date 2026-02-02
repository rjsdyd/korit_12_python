import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')

# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화
lives = 6
# todo - 2 : while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 조건을 작성

end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input('알파벳 하나 추측해서 입력 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
        # else:
        #     lives -= 1
        #     print(stages[lives])
        #     print(f'기회가 {lives}번 남았습니다')
        #     if lives == 0:
        #         end_of_game = True
        # 라고 작성하면 문자 하나 당 일치 여부를 확인하기에 예상했던 것과 다르게
        # 맞추더라도 나머지 문자에 대해 lives -= 1이 누적적으로 적용됨
        # 그런데 각 element에 대한 반복 때문에 누적적으로 값이 빠진다면, 반복문 바깥에 따로 작성
    if guess not in chosen_word:
        lives -= 1
        # print(stages[lives])  # 틀렸을 때만 그림이 나온다는 점이 문제
        print(f'기회가 {lives}번 남았습니다')
        if lives == 0:
            print('게임 종료')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다')
    if '_' not in display:
        print('정답입니다.')
        end_of_game = True

    print(' '.join(display))
# lives == 0 일 때 게임 종료를 표시해주셔야 함.
# 정답을 맞추면 정답입니다.를 출력
# 맞추거나 틀린 경우에 안내를 출력 _ p p _ _ 와 같은 식으로