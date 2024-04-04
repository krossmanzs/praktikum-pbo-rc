import random


words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

stages = ["""
    ------
    |    |
    |
    |
    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |
    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
------------
""", """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   /|\\
    |
------------
""", """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\ 
    |
------------
"""]

stage = 0
word = words[random.randrange(0,len(words)-1)]
guessed_words = list()
attempts = 5
correct_words = 0

for i in range(len(word)):
    guessed_words.append("_")

while stage < 7 and attempts >= 0:
    print(f"The word is: ", end= '')
    
    for i in range(len(word)):
        print(guessed_words[i], end='')

    guess = input("\nGuess a letter: ")
    
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess and guessed_words[i] != word[i]:
                guessed_words[i] = guess
                correct_words += 1
    else:
        print(f"Incorrect. You have {attempts} attempts left.")
        attempts -= 1
        stage += 1
        
    print(stages[stage])
        
    if correct_words == len(word):
        break;
    
    
    
if attempts > 0:
    print("OMMMMGGGGGG, you winnnnn!!")
else:
    print("OMGG the peeps ded :'(")