from random import choice
from string import ascii_lowercase

print("H A N G M A N")
lives = 8
playable_words = ['python', 'java', 'kotlin', 'javascript']
action = ""

while action != "exit":
    action = input('"play" to play the game, "exit" to quit:')
    if action == "play":
        choosen_word = choice(playable_words)
        hidden_word = list(choosen_word)
        for i in range(0, len(hidden_word)):
            hidden_word[i] = "-"
        used = set()
        while lives > 0 and choosen_word != "".join(hidden_word):
            print()
            print("".join(hidden_word))
            players_letter = input("Input a letter:")
            if players_letter in choosen_word and not players_letter in used:
                for n in range(0, len(choosen_word)):
                    if players_letter == choosen_word[n]:
                        hidden_word[n] = players_letter
                        used.add(players_letter)
            elif players_letter in used:
                print("You already typed this letter")
            elif players_letter not in choosen_word and len(players_letter) == 1 and players_letter in ascii_lowercase:
                lives -= 1
                print("No such letter in the word")
                used.add(players_letter)
            elif len(players_letter) != 1:
                print("You should input a single letter")
            elif players_letter not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
        if "".join(hidden_word) == choosen_word:
            print()
            print("".join(hidden_word))
            print("You guessed the word!\nYou survived!")
        else:
            print("You are hanged!")

