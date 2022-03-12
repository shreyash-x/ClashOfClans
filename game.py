import sys
import os

sys.path.append('./src')

import get_input
import village
import king
from map import printMap, showKingHealth, update_map
from characters import spawnBarbarian, move_barbarians, spawnDragon, move_dragons
from buildings import shoot_cannons
from spells import rage_spell, heal_spell
import points as pt

getch = get_input.Get()

V = village.createVillage()



def Phealth(health_bar):
    if(King.health > 0):
        print()
        print('King Health: ', end='')
        for i in range(len(health_bar)):
            print(health_bar[i], end='')
        print('')

King = king.spawnKing(pt.config['king_pos'])
os.system('clear')
printMap(V)
Phealth(showKingHealth(King.health))

# clear terminal




while(True):
    ch = get_input.input_to(getch)
    if ch == 'w':
        King.move('up', V)
    elif ch == 's':
        King.move('down', V)
    elif ch == 'a':
        King.move('left', V)
    elif ch == 'd':
        King.move('right', V)
    elif ch == '1':
        King.axe(V)
    elif ch == '2':
        King.dhaiKiloKaHaath(V)
    elif ch == 'r':
        rage_spell(King)
    elif ch == 'h':
        heal_spell(King)
    elif ch == 'z':
        spawnBarbarian(V.spawn_points[0])
    elif ch == 'x':
        spawnBarbarian(V.spawn_points[1])
    elif ch == 'c':
        spawnBarbarian(V.spawn_points[2])
    elif ch == 'v':
        spawnDragon(V.spawn_points[0])
    elif ch == 'b':
        spawnDragon(V.spawn_points[1])
    elif ch == 'n':
        spawnDragon(V.spawn_points[2])
    elif ch == 'q':
        print('quit')
        break
    os.system('clear')
    move_barbarians(V)
    move_dragons(V)
    shoot_cannons(King, V)
    printMap(V)
    Phealth(showKingHealth(King.health))
    if(V.check_if_game_over(King) == 1):
        print('Victory')
        break
    elif(V.check_if_game_over(King) == 2):
        print('Defeat')
        break

