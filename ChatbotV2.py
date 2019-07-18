# --- Define your functions below! ---
def intro():
    print("Hi there. My name is Eve 2.0.")
def process_input(answer):
    if valid_response(answer):
        greet()
    else:
        default()

def greet():
    thing = input("It's very nice to meet you. What would you like to do? ")
    valid_choice(thing)

def default():
    print("Me too.")

def valid_response(answer):
    valid_response = ["hi", "hey", "hello", "sup", ]
    if answer in valid_response:
        return True
    else:
        return False
def valid_choice(word):
    valid_choice = ["play a game", "tell me a joke", "tell me a riddle", "talk"]
    if word in valid_choice:
        if word == "play a game":
            hangman = input("What about Hangman? ")
            if hangman == "yes":
                print("Okay, let's play! I have to warn you- I'm very competitive!")
                import random
                potential_words = ["code", "hack", "build", "design", "think", "learn", "brave", "try"]
                word = random.choice(potential_words)
                letters = len(word)
                word = word.lower()
                current_word = ["_"] * letters# TIP: the number of letters should match the word
                print(current_word)
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
            if hangman == "no":
                different_game = input("Okay, what would you like to play? ")
                valid_game(different_game)
        if word == "tell me a joke":
            print("Why did the computer sneeze? Because it had a virus!")
        if word == "tell me a riddle":
            print("I am the beginning of the end, the end of every place. I am the beginning of eternity, the end of time and space. What am I? You have three guesses.")
        if word == "talk":
            print("Okay. Do you like to play sports? ")
        return True
    else:
        return False

def valid_game(different_game):
    different_game = ["rock, paper, scissors", "guess the number"]

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        answer.lower()
        process_input(answer)





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
