import random

characters = {
    'lisa': ["Female", "15","5'10", 'Red'],
    'bill': ["Male", "20", "5'5", 'Brown'],
    'linda': ["Female", "25","5'7", 'Brown'],
    'mike': ["Male", "15", "6'1", 'Blonde'],
    'liv': ["Female", "25", "5'11", 'Blonde']
}

def check_guess(guess, character):
    character_info = characters[character]
    if guess == "gender":
        print(character_info[0])
    elif guess == "age":
        print(character_info[1])
    elif guess == "height":
        print(character_info[2])
    elif guess == "hair":
        print(character_info[3])
    else:
        print("not a valid guess")
        return False
    return True

def game_start():
    character = list(characters.keys())[random.randint(0, len(characters.keys())-1)]
    guesses = 0
    guess_max = 2
    game_over = False
    game_won = False
    while not game_over and not game_won:
        user_input = input("What would you like to do? ")
        if user_input == "list":
            for item in characters:
                print(item)
        elif user_input == "help":
            print("list: prints all the characters names")
            print("gender: prints the gender of the chosen character")
            print("age: prints the age of the chosen character")
            print("height: prints the height of the chosen character")
            print("guess <name>: guess a character")
            print("help: lists all the commands")
            print("quit: quits the game")
        elif user_input == "quit":
            game_over = True
        elif user_input.split(' ')[0] == 'guess':
            if user_input.split(" ")[1].lower() == character.lower():
                game_won = True
            else:
                game_over = True
        else:
            has_guessed = check_guess(user_input, character)
            if has_guessed:
                guesses += 1
        if guesses > guess_max:
            game_over = True
    if game_won:
        print("You won!")
    else:
        print("You lost...")

game_start()