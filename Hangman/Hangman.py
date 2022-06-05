from multiprocessing import managers
import os
import sys
import random
import time
from traceback import print_tb
from numpy import append

def got_letter(word, letter, blanks_string):
    blanks_new= blanks_string
    index = 0
    for let in word:  
        if let == letter:
            blanks_new = blanks_new[:index] + letter + blanks_new[index+1:]
        index+=1
    return blanks_new


def choose_word(file_name: str):
    with open(f"files\{file_name}.txt") as file_list: 
        selected = random.choice(file_list.readlines())
        return(selected)

def hang_man_picture(fails: int):
    if fails == 0:
        return ("  +---+\n      |\n      |\n      |\n      |\n      |\n=========")
    elif fails == 1:
        return ("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
    elif fails == 2:
        return ("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
    elif fails == 3:
        return ("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
    elif fails == 4:
        return ("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
    elif fails == 5:
        return ("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
    elif fails == 6:
        return ("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
    elif fails == 7:
        return ("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
    else:
        return "Error"


def guess(word):
    guess_list=[]
    fails=0
    word= word.rstrip("\n")
    blanks= ("_"*len(word))
    print(blanks)
    solved = False
    while(solved != True or fails < 7): 
        print("\nGuess a letter")
        letter = input().lower()

        if letter in guess_list:
            print(f"You already guessed that silly. Here is what you have already guesses: {guess_list} \nTry another letter")
        else:
            if letter in word:
                print("That letter is in the word!")
                blanks = got_letter(word, letter, blanks)
                print(blanks)
                if "_" not in blanks:
                    solved = True
                    print("Congratulations! You did it!( ͡❛ ‿‿ ͡❛) \n Would you like to play again? type yes or no ")
                    if input().lower() == "yes":
                        hangman()
                    else:
                        print("Okay! Hope you had fun!")
            else:
                fails+=1
                print("That's wrong TT^TT")
                time.sleep(.1)
                print(hang_man_picture(fails))
                print(blanks)
            
            guess_list.append(letter)

    print(f"\nYou lost :(\n The answer was {word}\n Would you like to play again?")
    if input().lower() == "yes":
                    hangman()
    else:
        print("Okay! Hope you had fun!")


            
def hangman():
    print("Hello! Are you ready to play Hangman?")

    if input().lower() == "yes" :
        print("Which category would you like to choose? Movies, Books, or Songs? ")
        game_type = input().lower()
        time.sleep(.2)
        print("Great Choice! Let's start")
        time.sleep(.1)
        chosen_word = choose_word(game_type).lower()
        #print(chosen_word)
        print (hang_man_picture(0))
        time.sleep(.1)
        guess(chosen_word)


    else:
        print("Aw, maybe next time")



hangman()

