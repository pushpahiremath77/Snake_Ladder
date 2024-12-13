#use case 1
# def play_uc1():
#     position = 0
#     print(f"Player starts at position {position}")   
# play_uc1()

#use case 2
# import random
# def roll_die():
#     print(f"Player rolled: {random.randint(1, 6)}")
# roll_die()

#use case 3
import random
def roll_die():
    return random.randint(1, 6)

def get_option():
    option = ['NO_PLAY', 'LADDER', 'SNAKE']
    return random.choice(option)
    
def uc3():
    position=0
    die=roll_die()
    choice=get_option()
    
    print(f"Die rolled: {die}")
    if choice=='LADDER':
        position+=die
        print(f"{choice}! The player move ahead to position {position}")
    elif choice=='SNAKE':
        position-=die
        if position<0:
            position=0
        print(f"{choice}! The player move behind to the position {position}")
    else:
        print(f"{choice}! The player stays in the same position")

uc3()



