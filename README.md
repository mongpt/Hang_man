# Hang_man
Try to guess correct word, otherwise you will be hung
```python
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
```
Output console:
```
C:\Users\ADMIN\AppData\Local\Programs\Python\Python39\python.exe C:\Users\ADMIN\PycharmProjects\Hang_man\hang_man.py 
A new word = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
Guess a letter of this word: s
A new word = ['_', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: u
A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: c

    +---+
    |   |
    O   |
        |
        |            
        |
===========

A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: s
A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: f
 
    +---+
    |   |
    O   |
    |   |
        |
        |
===========

A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: s
A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: g
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========

A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: h
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========

A new word = ['u', '_', '_', '_', '_', '_', 's', '_', '_', '_']
Guess a letter of this word: r
A new word = ['u', '_', '_', '_', '_', 'r', 's', '_', '_', '_']
Guess a letter of this word: i
A new word = ['u', '_', 'i', '_', '_', 'r', 's', 'i', '_', '_']
Guess a letter of this word: s
A new word = ['u', '_', 'i', '_', '_', 'r', 's', 'i', '_', '_']
Guess a letter of this word: g
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========

A new word = ['u', '_', 'i', '_', '_', 'r', 's', 'i', '_', '_']
Guess a letter of this word: h
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========

You lose
>>>>>>> university <<<<<<<
```
