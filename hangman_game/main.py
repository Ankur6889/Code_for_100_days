import random 
import ascii_art
import game_words
import os 
import numpy
def display_function(dashed_word,lives,message):
    
    os.system('clear')
    print("\n",ascii_art.logo,"\n","_____________________________________________________________________","\n")
    how_to_print =""
    for i in dashed_word:
        how_to_print = how_to_print+ i + " "
    print(how_to_print,"\n")
    if lives == 6 :
        print("")
    else :
        print(ascii_art.stages[lives])
    return input(f"{message}")


# Selecting a random word from the word list for the game 
selected_word = random.choice(game_words.word_list)

# Game Variables
len_of_word = len(selected_word)
lives_remaining = 6
game_end = False
already_guessed_letters = []
dashed_word = []
message = "Guess a letter :"
global_game_restart = False 

# generating an array called display_word with dashed letters for the word 

for i in range(len_of_word):
    dashed_word.append("_")


while not game_end:
    
    guessed_letter = display_function(dashed_word,lives_remaining,message)
    if guessed_letter in already_guessed_letters:
        message = f"you have already tried '{guessed_letter}' try something else :"

    else :
        
        if guessed_letter in selected_word:
            already_guessed_letters.append(guessed_letter)
            for letter_index in range(len_of_word):
                if guessed_letter == selected_word[letter_index]:
                    dashed_word[letter_index] = guessed_letter
                    guessed_word = ""
                    for i in dashed_word:
                        guessed_word = guessed_word + i
                    if guessed_word == selected_word :
                        message = "Great Job !! you guessed the correct word."
                    else : 
                        message = "Good , now guess another letter :"
            
            
        else : 
            print("That's Wrong")
            already_guessed_letters.append(guessed_letter)
            lives_remaining-=1
            message = "Oh! that was a wrong answer!!! Try Again :"
            if lives_remaining < 1 :
                game_end = True 
                display_function(dashed_word,lives_remaining,f"GAME OVER !!! the correct answer was : {selected_word}")
        