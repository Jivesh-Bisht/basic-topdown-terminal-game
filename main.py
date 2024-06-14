import keyboard
import time
from os import system, name
from termcolor import cprint
from random import randint,choice


obstacles = ["#","@","|"]
player = "*"
world = [[".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".","*",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."]]

def print_world(world):
    for levels in world:
        for element in levels:
            if element == player:
                cprint(element,"green",end=" ")
            elif element in obstacles:
                cprint(element,"red",end=" ")
            else:
                cprint(element,"magenta",end=" ")
        print("\n")


def add_obstacles(world,obs=5):
    for i in range(obs):
        level = randint(0,(len(world)-1))
        pos = randint(0,9)
        if (level,pos) == get_player(world):
            pass
        else:
            world[level][pos] = choice(obstacles)
    



def get_player(world) -> (int,int):
    for level,levels in enumerate(world):
        try:
            current_pos = levels.index(player)
            return level,current_pos
        except ValueError:
            level+=1

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()
add_obstacles(world)
print_world(world)
run = True
while run:

    if keyboard.is_pressed('q'):
        clear()
        print("Quitting")
        run = False


    if keyboard.is_pressed('a'):
        level,current_pos = get_player(world)
        if current_pos == 0:
            clear()
            print_world(world)
        else:
            clear()
            if world[level][current_pos-1] in obstacles:
                print_world(world)
            else:
                world[level][current_pos] = "."
                world[level][current_pos-1] = player
                print_world(world)
            time.sleep(0.1)


    if keyboard.is_pressed('d'):
        level,current_pos = get_player(world)
        if current_pos == len(world[0]):
            clear()
            print_world(world)
        else:
            clear()
            if world[level][current_pos+1] in obstacles:
                print_world(world)
            else:
                world[level][current_pos] = "."
                world[level][current_pos+1] = player
                print_world(world)
            time.sleep(0.1)

    if keyboard.is_pressed('w'):
        level,current_pos = get_player(world)
        if level == 0:
            clear()
            print_world(world)
        else:
            clear()
            if world[level-1][current_pos] in obstacles:
                print_world(world)
            else:
                world[level][current_pos] = "."
                world[level-1][current_pos] = player
                print_world(world)
            time.sleep(0.1)


    if keyboard.is_pressed('s'):
        level,current_pos = get_player(world)
        if level == (len(world)-1):
            clear()
            print_world(world)
        else:
            clear()
            if world[level+1][current_pos] in obstacles:
                print_world(world)
            
            else:
                world[level][current_pos] = "."
                world[level+1][current_pos] = player
                print_world(world)
            time.sleep(0.1)
