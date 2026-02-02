import random
import hangman_art
import hangman_word_list

# import 다음에 파일명을 썼다는 것에 주목.
# 이 파일 하나를 파이썬에서는 module(모듈)이라고 함.

# 외부의 hangman_word_list에 있는 word_list 변수를 참조해서 chosen_word를 만들 필요

print(hangman_art.logo)
# 위에가 힌트. 그러면 chosen_word를 불러올 수 있도록 코드를 작성

chosen_word = random.choice(hangman_word_list.word_list)
print(f'테스트 단어 : {chosen_word}')
display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6

end_of_game = False
while not end_of_game:
    print(hangman_art.stages[lives])
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
            print(hangman_art.stages[lives])
            print(f'정답은 {chosen_word}입니다')
    if '_' not in display:
        print('정답입니다.')
        end_of_game = True

    print(' '.join(display))