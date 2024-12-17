import random

def roll_die():
    return random.randint(1, 6)

def check_option(position):
    die_value = roll_die()
    option = random.choice(["No Play", "Ladder", "Snake"])

    if option == "Ladder":
        position += die_value
        if position > 100:
            position -= die_value
    elif option == "Snake":
        position -= die_value
        if position < 0:
            position = 0
    return position, die_value, option


def play_two_players():
    position1 = 0
    position2 = 0
    rolls1 = 0
    rolls2 = 0
    turn = 1
    game=True

    #while True:
    while game:
        if turn == 1: 
            position1, _, option = check_option(position1)
            rolls1 += 1
            print(f"Player 1: {option}, Rolls:{rolls1}, Position:{position1}")

            if position1 == 100:
                print(f"Player 1 wins the game in {rolls2} rolls")
                #break
                game=False
            turn = 2  

        else:
            position2,_, option = check_option(position2)
            rolls2 += 1
            print(f"Player 2: {option}, Rolls:{rolls2}, Position:{position2}")

            if position2 == 100:
                print(f"Player 2 wins the game in {rolls2} rolls")
                #break
                game=False
            turn = 1  

play_two_players()
    



    
