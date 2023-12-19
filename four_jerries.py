import random

hidden_number = None
user_guess = None

def welcome_screen():
    print("Welcome to the 4Jerries Game!")

def generate_hidden_number():
    global hidden_number
    hidden_number = str(random.randint(1000, 9999))

def validate_hidden_number():
    # Add validation logic if needed
    pass

def player_guess():
    global user_guess
    user_guess = input("Enter a 4-digit number: ")

def validate_user_guess():
    # Add validation logic if needed
    pass

def count_jerries_toms():
    jerrys = 0
    toms = 0
    for i in range(4):
        if user_guess[i] == hidden_number[i]:
            jerrys += 1
        elif user_guess[i] in hidden_number:
            toms += 1
    return jerrys, toms

def display_result(jerrys, toms):
    print(f"{jerrys} Jerry, {toms} Tom")

def main():
    welcome_screen()
    generate_hidden_number()

    attempts = 0
    while True:
        player_guess()
        validate_user_guess()

        if user_guess == hidden_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

        jerrys, toms = count_jerries_toms()
        display_result(jerrys, toms)

        attempts += 1

#Main function.
if __name__ == "__main__":
    main()
