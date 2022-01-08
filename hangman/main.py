import hangman_pics
import random_words
import random

# ask user for his name
def ask_username():
	user_name = input("Enter your name to begin the game: ")
	return user_name

# generate a random word
def generate_random_word():
	random_word = random.choice(random_words.words)
	return random_word


# run the game 
def run_game():
	user_name = ask_username()
	user_score = 0
	user_life = 7
	game_over = False
	random_word = generate_random_word()
	blank_list = ["_" for x in range(0,len(random_word))]

	while game_over == False or user_score == len(random_word):
		guessed_letter = input("Enter your guess: ")

		if user_life == 1:
			print("You have used all your lives. GAME OVER")
			game_over = True

		elif len(guessed_letter) == 1:
			guessed_letter_idx = random_word.find(guessed_letter)
			if guessed_letter_idx != -1:
				user_score += 1
				blank_list[guessed_letter_idx] = guessed_letter
				print(blank_list)

			elif guessed_letter_idx == -1:
				if user_life == 1:
					game_over = True
				else: 
					user_life -= 1
					print(f" {user_name}! You guessed incorrectly. You have {user_life} life remaining.")
					print(hangman_pics.HANGMANPICS[-user_life])
				
			else:
				print("Invalid Error")
			
		else:
			print(f"{user_name}! Your guess should be a single letter!")
			





