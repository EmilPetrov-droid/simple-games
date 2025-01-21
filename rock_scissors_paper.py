import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
computer_move = ''

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

# make user's choice case insensitive

if player_move.lower() == 'r':
    player_move = rock
elif player_move.lower() == 'p':
    player_move = paper
elif player_move.lower() == 's':
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")
print(f"Your choice is {player_move}")
print("Now it is computer's turn.")

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or\
    ((player_move == paper and computer_move==rock) or
     (player_move == scissors and computer_move == paper )):
    print("You win!")

elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")


