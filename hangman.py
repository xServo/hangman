# hangman
# by xServo
# https://github.com/xServo/hangman

import random
import os

# decides phrase 
f_words = open("words.txt", "r")
phrase_list = []
line = f_words.readline()
while line:
   phrase_list.append(line.strip())
   line = f_words.readline()
f_words.close()
 
phrase_str = phrase_list[random.randint(0, len(phrase_list) - 1)]

# turns phrase_str into a list
phrase = []
cnt = 0
for i in phrase_str:
    phrase.append(phrase_str[cnt])
    cnt += 1

# prep board
board = []
cnt = 1
for i in range(len(phrase)):
    board.append("#")
    cnt += 1
guesses = 6

# game loop
while 1:
    # graphics
    os.system('clear')
    #print(*phrase) # testing
    print(*board)
    print("guesses: " + str(guesses))

    # guess
    guess = input("Make a guess: ")
    cnt = 0
    can_gain = True
    for letter in phrase:
        if letter == guess:
            board[cnt] = letter
            if can_gain == True:
                guesses += 1
                can_gain = False
        cnt += 1
    guesses += -1
    
    # lose con
    if guesses < 1:
        os.system('clear')
        input("You ran out of guesses.\nThe word was: " + phrase_str + "\nPress enter to exit.")
        break

    # win con
    won = True
    for letter in board:
        if letter == '#':
            won = False
    if won == True:
        os.system('clear')
        input("You won!\nThe word was: " + phrase_str + "\nPress enter to exit.")
        break
