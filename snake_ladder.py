import random

def play_game_with_rolls():
    position = 0
    count = 0
    while position != 100:
        count += 1
        dice_roll = random.randint(1, 6)
        option = random.randint(1, 3)

        if option == 1:  
            pass
        elif option == 2:  
            position += dice_roll
        else:  
            position -= dice_roll
        
        if position < 0:
            position = 0
        if position > 100:
            position -= dice_roll
        
        print(f"Dice rolled: {dice_roll}, Position: {position}")
    print(f"Total number of times the dice was played to win : {count}")

play_game_with_rolls()
