import random
from hangman_art import *
# hangman_arts 파일의 전체 데이터를 가지고 옴
from hangman_word_list import word_list
# hangman_word_list 파일 내에서 word_list 변수만 가지고 오겠다는 의미

# 이상과 같이 작성한 것을 기준으로 hangman을 완성

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6

print(logo)
end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input('알파벳 하나 추측해서 입력 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
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