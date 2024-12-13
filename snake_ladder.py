import random
def repeat_roll():
    position=0
    while(position!=100):
        dice=random.randint(1,6)
        choice=random.randint(1,3)

        if choice==1:
            if position + dice <= 100:
                position+=dice
                print(f"Ladder:Rolled {dice}, moved forward. Position: {position}")
            else:
                print(f"Rolled {dice}, but move exceeds 100. Staying at position: {position}")
        
        elif choice==2:
            position-=dice

            if position<0:
                position=0
            print(f"Snake:Rolled {dice}, moved backward. Position: {position}")

        else:
            print(f"No Play:Staying in same position: {position}")
    print(f"Player reached the winning position: {position}")

repeat_roll()
