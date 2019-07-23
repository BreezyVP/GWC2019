import random

# A list of words that
potential_words = ["code", "hack", "build", "design", "think", "learn", "brave", "try"]

word = random.choice(potential_words)
letters = len(word)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_"] * letters# TIP: the number of letters should match the word
print(current_word)
# Some useful variables
guesses = []
maxfails = 7
fails = 0
fails = fails+1
letter = "_"
while fails < maxfails:
	iter = 0
	guess = input("Guess a letter or word: ")
	if guess in word:
		for letter in word:
			if letter == guess:
				current_word[iter] = guess
				print(current_word)
			elif guess == word:
				print("Congrats! You got it!")
				break
			iter += 1
	if ("_") not in current_word:
		print("You win! Yay!")
		break
	if guess not in word:
		print("I'm sorry, that's not right. You have " + str(maxfails - fails) + " tries left!")
		fails = fails+1
if fails == maxfails:
	print(current_word)
	print("I'm sorry, but you loose this round. Want to play again?")

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
