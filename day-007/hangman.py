print(r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer', 'algorithm', 'function', 'variable']
hang_status=[r'''  +---+
  |   |
      |
      |
      |
      |
=========''', r'''  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

word=random.choice(word_list)

hang_status_index=0
lives=6
blanks='-'*len(word)
while lives>0 and word!=blanks:
    print("Word to guess: ",blanks)
    # print("Guess a letter: ",input())
    guess=input("Guess a letter: ")

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        hang_status_index+=1
        print(hang_status[hang_status_index])
        lives-=1
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        # guessed_word_index=word.index(guess)
        # blanks=blanks[:guessed_word_index]+guess+blanks[guessed_word_index+1:]
        # # blanks[guessed_word_index]=guess
        

        indices=[i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            blanks=blanks[:index]+guess+blanks[index+1:]
        print(hang_status[hang_status_index])






if word==blanks:
    print("You win!")
else:
    print(f"***********************IT WAS {word}! YOU LOSE***********************")