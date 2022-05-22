import random

games_won = 0
games_lost = 0
options = ["play", "results", "exit"]
keep_playing = True
used_letters = []

def scoreBoard():
    print(f"You won: {games_won} times")
    print(f"You lost: {games_lost} times")
            
print('H A N G M A N')

while keep_playing == True:
    
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    
    if choice not in options:
        continue
    elif choice == "exit":
        keep_playing = False 
    elif choice == "results":
        scoreBoard()
    else:
        attempts = 8
        languages = ['python', 'java', 'swift', 'javascript']
        word = random.choice(languages)
        clue = list('-' * len(word))
        
        while attempts > 0:
            
            print()
            print("".join(clue))
 
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("Please, input a single letter.")
                used_letters.append(letter)
            elif letter != letter.lower():
                print("Please, enter a lowercase letter from the English alphabet.")
                used_letters.append(letter)       
            elif letter.isalpha() == False:
                print("Please, enter a lowercase letter from the English alphabet.")
                used_letters.append(letter)
            elif letter in used_letters:
                print("You've already guessed this letter.")  
            else:
                if letter in word:
                    
                    for i in range(len(word)):
                        if word[i] == letter:
                            clue[i] = letter
                            used_letters.append(letter)
                            if "".join(clue) == word:
                                print(f"You guessed the word {word}!")
                                print("You survived!")
                                attempts = 0
                                used_letters = []
                                games_won += 1
                            else:
                                continue

                else:
                    print("That letter doesn't appear in the word.")
                    used_letters.append(letter)
                    attempts -= 1     

        if attempts == 0 and "".join(clue) != word:
            games_lost += 1
            print("You lost!")
            continue