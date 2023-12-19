import random

NUMBER_LENGTH = 4

class FourJerriesGame:
    def __init__(self):
        self.hidden_number = None
        self.user_guess = None

    #Welcome screen at start of the game & rules.
    def welcome_screen(self):
        print("Welcome to the 4Jerries Game!\n")
        print("Rules.\nEvery number in wrong place you get a Tom.\nEvery right place you get Jerry.\nIf you get 4 Jerries you will win.\n")

    #Generate the hidden number.
    def generate_hidden_number(self):
        digits = [str(i) for i in range(10)]
        self.hidden_number = ''.join(random.sample(digits, NUMBER_LENGTH))

    #Take user input for the check number.
    def get_user_guess(self):
        while True:
            user_input = input(f"Enter a {NUMBER_LENGTH}-digit number: ")
            if self.validate_user_guess(user_input):
                self.user_guess = user_input
                break
            else:
                print("Invalid input. Please enter a valid 4-digit number.")
    #Validate the user input.
    def validate_user_guess(self, user_input):
        if not user_input.isdigit() or len(user_input) != NUMBER_LENGTH:
            return False
        return True

    #Check the user input and hidden number is matching or not.
    def is_correct_guess(self):
        return self.user_guess == self.hidden_number

    #Count the jerry and tom. 
    def count_jerries_toms(self):
        jerrys = sum(1 for i in range(len(self.user_guess)) if self.user_guess[i] == self.hidden_number[i])
        toms = NUMBER_LENGTH - jerrys
        return jerrys, toms

    #Display the result correct or wrong
    def display_result(self, jerrys, toms):
        print(f"{jerrys} Jerry, {toms} Tom")
        print(self.hidden_number)

    def play_game(self):
        self.welcome_screen()
        self.generate_hidden_number()
        while True:
            self.get_user_guess()

            if self.is_correct_guess():
                print("Congratulations! You guessed the correct number.")
                break

            jerrys, toms = self.count_jerries_toms()
            self.display_result(jerrys, toms)


if __name__ == "__main__":
    game = FourJerriesGame()
    game.play_game()
