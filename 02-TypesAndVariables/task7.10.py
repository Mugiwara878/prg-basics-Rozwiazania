import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("type number: "))
game = you == computer
print(f'You won: {game}')