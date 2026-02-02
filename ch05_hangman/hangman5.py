import random
logo = '''
  _    _                   __  __             
 | |  | |                 |  \/  |            
 | |__| | __ _ _ __   __ _| \  / | __ _ _ __  
 |  __  |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ 
 | |  | | (_| | | | | (_| | |  | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|
                      __/ |                   
                     |___/                    
'''
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
word_list = [
    'apple', 'banana', 'camel', 'actor', 'adult', 'alarm', 'album', 'angel', 'angle', 'angry',
    'animal', 'answer', 'ant', 'area', 'arm', 'army', 'art', 'artist', 'atom', 'aunt',
    'baby', 'back', 'ball', 'bank', 'base', 'basket', 'bath', 'beach', 'bear', 'beat',
    'beer', 'bell', 'belt', 'bench', 'bike', 'bird', 'birth', 'black', 'block', 'blood',
    'blue', 'board', 'boat', 'body', 'bone', 'book', 'boot', 'bottle', 'box', 'boy',
    'brain', 'bread', 'bridge', 'bright', 'brother', 'brush', 'build', 'burn', 'bus', 'bush',
    'butter', 'button', 'cake', 'call', 'camera', 'camp', 'can', 'candle', 'candy', 'cap',
    'car', 'card', 'care', 'carry', 'case', 'cat', 'catch', 'cause', 'cell', 'center',
    'chair', 'chance', 'change', 'chart', 'check', 'cheese', 'cherry', 'chest', 'child', 'chin',
    'church', 'city', 'class', 'clean', 'clear', 'climb', 'clock', 'close', 'cloth', 'cloud',
    'club', 'coach', 'coal', 'coast', 'coat', 'coffee', 'cold', 'color', 'comb', 'cook',
    'cool', 'copy', 'corn', 'corner', 'cost', 'count', 'court', 'cousin', 'cover', 'cow',
    'crack', 'cream', 'cross', 'crowd', 'crown', 'cry', 'cup', 'curve', 'cut', 'cycle',
    'dad', 'dance', 'dark', 'date', 'day', 'dead', 'dear', 'death', 'deep', 'deer',
    'desk', 'dirt', 'dish', 'dog', 'doll', 'door', 'dot', 'down', 'draw', 'dream',
    'dress', 'drink', 'drive', 'drop', 'drum', 'dry', 'duck', 'dust', 'ear', 'earth',
    'east', 'eat', 'edge', 'egg', 'eight', 'elbow', 'end', 'engine', 'error', 'eye',
    'face', 'fact', 'fall', 'family', 'fan', 'farm', 'fast', 'father', 'fear', 'feel',
    'feet', 'field', 'fight', 'film', 'final', 'find', 'fine', 'finger', 'fire', 'fish',
    'five', 'flag', 'flat', 'floor', 'flower', 'fly', 'fog', 'food', 'foot', 'forest',
    'fork', 'form', 'four', 'frame', 'free', 'fresh', 'friend', 'frog', 'front', 'fruit',
    'fuel', 'full', 'fun', 'funny', 'game', 'garden', 'gas', 'gate', 'gear', 'gift',
    'girl', 'glass', 'glove', 'glue', 'goat', 'gold', 'golf', 'good', 'goose', 'grape',
    'grass', 'gray', 'great', 'green', 'ground', 'group', 'grow', 'guard', 'guess', 'guide',
    'guitar', 'gum', 'gun', 'guy', 'habit', 'hair', 'half', 'hall', 'hand', 'happy',
    'hard', 'hat', 'hate', 'head', 'health', 'heart', 'heat', 'heavy', 'hell', 'help',
    'hen', 'hero', 'high', 'hill', 'hip', 'hit', 'hobby', 'hold', 'hole', 'home',
    'honey', 'hook', 'hope', 'horn', 'horse', 'hose', 'host', 'hot', 'hotel', 'hour',
    'house', 'human', 'hunt', 'hurry', 'hurt', 'ice', 'idea', 'image', 'inch', 'ink',
    'iron', 'island', 'item', 'jacket', 'jail', 'jam', 'jar', 'jaw', 'jazz', 'jeans',
    'jelly', 'jet', 'job', 'joke', 'joy', 'judge', 'juice', 'jump', 'junk', 'jury',
    'key', 'kick', 'kid', 'kill', 'kind', 'king', 'kiss', 'kit', 'kite', 'knee',
    'knife', 'knot', 'know', 'lady', 'lake', 'lamp', 'land', 'lane', 'lap', 'last',
    'late', 'laugh', 'law', 'lead', 'leaf', 'learn', 'left', 'leg', 'lemon', 'lens',
    'less', 'let', 'letter', 'level', 'library', 'lid', 'lie', 'life', 'lift', 'light',
    'line', 'lion', 'lip', 'list', 'live', 'load', 'lock', 'log', 'long', 'look',
    'loop', 'lord', 'loss', 'loud', 'love', 'low', 'luck', 'lunch', 'lung', 'mail',
    'main', 'make', 'male', 'mall', 'man', 'map', 'march', 'mark', 'mask', 'mass',
    'match', 'mate', 'math', 'meal', 'mean', 'meat', 'medal', 'media', 'meet', 'melon',
    'menu', 'mess', 'metal', 'mice', 'milk', 'mind', 'mine', 'mirror', 'miss', 'mix',
    'mode', 'model', 'mom', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motor',
    'mount', 'mouse', 'mouth', 'move', 'movie', 'mud', 'muscle', 'music', 'nail', 'name',
    'neck', 'need', 'nerve', 'nest', 'net', 'news', 'next', 'nice', 'night', 'nine',
    'noble', 'noise', 'none', 'noon', 'north', 'nose', 'note', 'notice', 'noun', 'nurse',
    'nut', 'oak', 'ocean', 'oil', 'old', 'olive', 'onion', 'open', 'opera', 'orange',
    'orbit', 'order', 'organ', 'oven', 'owl', 'owner', 'pack', 'page', 'pain', 'paint',
    'pair', 'palace', 'palm', 'pan', 'panel', 'pant', 'paper', 'park', 'part', 'party',
    'pass', 'past', 'path', 'pay', 'peace', 'peak', 'pear', 'pen', 'pencil', 'pepper',
    'person', 'pet', 'phone', 'photo', 'piano', 'pick', 'piece', 'pig', 'pile', 'pill',
    'pilot', 'pin', 'pine', 'pink', 'pipe', 'pitch', 'pizza', 'place', 'plan', 'plane',
    'plant', 'plate', 'play', 'player', 'plum', 'plus', 'pocket', 'poem', 'poet', 'point',
    'poison', 'pole', 'police', 'pond', 'pool', 'poor', 'pop', 'pork', 'port', 'post',
    'pot', 'potato', 'power', 'press', 'price', 'pride', 'print', 'prize', 'profit', 'proof',
    'proud', 'pump', 'punch', 'pure', 'purple', 'purse', 'push', 'queen', 'quest', 'quick',
    'quiet', 'quiz', 'race', 'radio', 'rail', 'rain', 'raise', 'rank', 'rare', 'rat'
]
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