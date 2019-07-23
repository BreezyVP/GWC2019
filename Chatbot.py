# --- Define your functions below! ---
def intro():
    print("Hi, my name is Eve.")

def process_input(answer):
    if answer == "hi":
        say_greeting()
    elif answer == "I'm bored":
        say_what_to_do(reply)
        if reply == "yes":
            print("What about Hangman?")
            if reply == "yes":
                print()
            else reply == "no":
                print("What game would you like to play then?")
        else reply == "no"
            print("")
    else:
        say_default()

def say_greeting():
    print("I'm a chatbot. It's very nice to meet you.")
def say_default():
    print("Me too.")
def get_name(reponse):
    print("That's a great name! I wish I had a name like yours.")
def say_what_to_do(reply):


# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)
        response = input("What's your name?")
        get_name(response)
        say_what_to_do(reply)
        reply = input("That sucks. Do you wanna play a game?")
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
