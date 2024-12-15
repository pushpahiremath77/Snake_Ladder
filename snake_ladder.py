import random

def roll_die():
    return random.randint(1, 6)

def check_option(die_value):
    options = ["No Play", "Ladder", "Snake"]
    option = random.choice(options)
    
    if option == "Ladder":
        print(f"Ladder : Player moves forward by {die_value} steps.")
    elif option == "Snake":
        print(f"Snake : Player moves backward by {die_value} steps.")
    else:
        print("No Play : Player stays in the same position.")
    return option

def play_two_players():
    player1_position = 0
    player2_position = 0
    rolls1 = rolls2 = 0
    turn = 1
    
    while player1_position < 100 and player2_position < 100:
        if turn == 1:
            die_value = roll_die()
            rolls1 += 1
            option = check_option(die_value)
            
            if option == "Ladder" and player1_position + die_value <= 100:
                player1_position += die_value
            elif option == "Snake":
                player1_position -= die_value
                if player1_position < 0:
                    player1_position = 0
            
            print(f"Player 1's position: {player1_position}")
            if player1_position == 100:
                print(f"Player 1 wins after {rolls1} rolls!")
                break
            turn = 2 
        else:
            die_value = roll_die()
            rolls2 += 1
            option = check_option(die_value)
            
            if option == "Ladder" and player2_position + die_value <= 100:
                player2_position += die_value
            elif option == "Snake":
                player2_position -= die_value
                if player2_position < 0:
                    player2_position = 0
            
            print(f"Player 2's position: {player2_position}")
            if player2_position == 100:
                print(f"Player 2 wins after {rolls2} rolls!")
                break
            turn = 1

play_two_players()
