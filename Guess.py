import random

def guess(x):
    menu = 'Y'
    while(menu == 'y' or menu == 'Y'):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 - {x}:'))
            if (guess < random_number):
                print("Sorry, your guess is too low. Try again!")
            elif (guess > random_number) :
                print("Sorry, your guess is too high. Try again!")
            elif (guess == random_number) :
                print(f"Congratulations! You've guessed the number {random_number}!")
        
        menu = input("Would you like to play again? (Y/N)")
        
guess(100)
print("Thanks for playing!")