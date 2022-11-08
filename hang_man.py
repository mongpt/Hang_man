
import random
graphic = ['''
    +---+
    |   |
    O   |
        |
        |            
        |
===========
''',''' 
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
''',''' 
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========
''',''' 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========
''',''' 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========
''',''' 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
'''
]

wordList = ["comfortable", "banana", "castle", "university", "library", "method", "school", "capital"]
randomWord = random.choice(wordList)
resultList = []
for i in randomWord:
    resultList.append("_")
print("A new word =",resultList)
x = 0
while "_" in resultList:
    guess = input("Guess a letter of this word: ")
    if guess in randomWord:
        for i in range(len(randomWord)):
            if guess == randomWord[i]:
                resultList[i] = guess
    else:
        print(graphic[x])
        x += 1
        if x == 6:
            print("You lose")
            break
    print("A new word =",resultList)
print(">>>>>>>",randomWord,"<<<<<<<")