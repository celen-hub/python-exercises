wordlist = open("wordlist.txt").read().split()
import random
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
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
=========''', '''
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
chosen_word = random.choice(wordlist)
guess_list = []
for x in range(len(chosen_word)):
	guess_list.append("_")
print(guess_list)

lives = 6

while ''.join(guess_list) != chosen_word:
	guess = input("Guess a letter: ").lower()
	guessed_letters = []
	guessed_letters.append(guess)
	print(f"Guessed Letters : {guessed_letters}")

	for position in range(len(chosen_word)):
		letter = chosen_word[position]
		if letter == guess:
			guess_list[position] = letter
			print(guess_list)
		
	if guess not in chosen_word:
		lives -= 1
		print(stages[lives])
		if lives == 0:
			print("Game Over!")
			break		

guessed_letters = []


	
