import random
def snakes_and_ladders(pos):
    if pos==61:
        pos=47
        print("Snake!")
    if pos==44:
        pos=26
        print("Snake!")
    if pos==25:
        pos=10
        print("Snake!")
    if pos==18:
        pos=1
        print("Snake!")
    if pos == 3:
        pos = 13
        print("Ladder!")
    if pos==11:
        pos=28
        print("Ladder!")
    if pos==30:
        pos=45
        print("Ladder!")
    if pos==42:
        pos=59
        print("Ladder!")
    return pos

def take_turn(pos):

    global roll
    roll = random.randint(1,6)
    print(roll)
    x = pos +roll
    x = snakes_and_ladders(pos= x)
    if x <= 64:
        pos = x

    return pos

positions  = [1,1]
current_idx = 0

while positions[0]<64 and positions[1]<64:

    print(f"Player 1 is on space {positions[0]}")
    print(f"Player 2 is on space {positions[1]}")
    print(f"Player {current_idx+1} rolls the die: ", end=" ")

    positions[current_idx] = take_turn(positions[current_idx])

    if current_idx == 0:
        current_idx = 1

    else:
        current_idx = 0

if positions[0] == 64:
    print("Player 1 wins!!!")
elif positions[1] == 64:
    print("Player 2 wins!!!")
















