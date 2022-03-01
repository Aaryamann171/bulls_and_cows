import random

def welcome_messages():
    print("# Welcome to the Bulls and Cow game!")
    print("Too lazy to type out rules, you can refer to the link below")
    print("https://en.wikipedia.org/wiki/Bulls_and_Cows")
    print("Let's Begin", end="\n\n")

def secret_code_generator():
    secret_code = []
    num_list = [x for x in range(1,9)]
    for i in range(4):
        rand_indx = random.randint(1, len(num_list)-1)
        x = num_list.pop(rand_indx)
        secret_code.append(x)
    original_num = int("".join([str(x) for x in secret_code]))
    return secret_code, original_num

def user_input():
    # quit if user types one of these commands
    quit_messages = ["quit", "exit", "q", "ex"]
    guess = input("Enter you guess: ")
    if guess in quit_messages:
        print("Quiting game, thanks for playing!")
        exit()
    if len(guess) != 4:
        print("Guess must be 4 digits")
        return None
    # convert user guess into a list of ints
    guess_list = list(map(lambda i: int(i), [c for c in guess]))
    # check if there are any duplicates in the list
    if len(set(guess_list)) < 4:
        print("NOTE: all numbers are unique")
    return guess_list

def bulls(l1, l2): # correct guess in the correct position
    bulls = 0
    for i in range(4):
        if l1[i] == l2[i]:
            bulls += 1
    return bulls

def common_nums(l1, l2): # correct guess but not in the correct position
    return len(set(l1).intersection(set(l2)))

def main():
    welcome_messages()
    game_on_flag = 1
    secret_code, original_num = secret_code_generator()
    while(game_on_flag): 
        user_guess = user_input()
        while (user_guess is None):
            user_guess = user_input()
        n_bulls = bulls(secret_code, user_guess)
        commons = common_nums(secret_code, user_guess)
        n_cows = commons - n_bulls
        print(f"Bulls: {n_bulls}")
        print(f"Cows: {n_cows}")
        if(user_guess == secret_code):
            print(f"Congratulations! Your guess is correct. Secret code was in fact {original_num}.")
            game_on_flag = 0
        
if __name__=="__main__":
    main()
