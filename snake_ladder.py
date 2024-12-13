import random
def uc5():
    position = 0
    while position != 100:
        dice_roll = random.randint(1, 6)
        option = random.randint(1, 3)

        if option == 1: 
            print(f"No Play : Dice rolled: {dice_roll}, Position: {position}")            
            pass
        elif option == 2:  
            position += dice_roll
            print(f"Ladder : Dice rolled: {dice_roll}, Position: {position}")
        else:  
            position -= dice_roll
            print(f"Snake : Dice rolled: {dice_roll}, Position: {position}")
        
        if position < 0:
            position = 0
        if position > 100:
            position -= dice_roll
        
    print(f"Player reached position {position}!!!")

uc5()
