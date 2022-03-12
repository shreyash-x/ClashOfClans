from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import points as pt
import numpy as np
import datetime
from characters import barbarians, dragons

# 50 - 100 : cyan
# 20 - 50 : yellow
# 0 - 20 : red

now = datetime.datetime.now()

def buildingColor(V,address):
    type = address.split(':')[0]
    a=0
    b=0
    health = 0
    max_health = 0

    if type == pt.TOWNHALL:
        health = V.town_hall_obj.health
        max_health = V.town_hall_obj.max_health
    else:
        a = int(address.split(':')[1])
        b = int(address.split(':')[2])
    if type == pt.HUT:
        health = V.hut_objs[(a,b)].health
        max_health = V.hut_objs[(a,b)].max_health
    elif type == pt.CANNON:
        if V.cannon_objs[(a,b)].isShooting:
            return Back.MAGENTA
        health = V.cannon_objs[(a,b)].health
        max_health = V.cannon_objs[(a,b)].max_health

    health = (health*100)/max_health
    if(health > 50):
        return Back.CYAN
    elif(health > 20):
        return Back.YELLOW
    else:
        return Back.RED

def barbColor(barb):
    health = barb.health
    max_health = barb.max_health
    percentage = (health*100)/max_health
    if(percentage > 50):
        return Back.RED
    elif percentage > 20:
        return Back.YELLOW
    else:
        return Back.WHITE

def drColor(dr):
    health = dr.health
    max_health = dr.max_health
    percentage = (health*100)/max_health
    if(percentage > 50):
        return Back.MAGENTA
    elif percentage > 20:
        return Back.BLUE
    else:
        return Back.WHITE
        


def printMap(V):
    map = np.copy(V.map)
    map_matrix = np.empty((pt.config['dimensions'][0]*2,pt.config['dimensions'][1]*2), dtype=object)
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if(map[i][j].split(':')[0] == pt.BLANK):
                for a in range(2):
                    for b in range(2):
                        map_matrix[2*i+a][2*j+b] = Back.GREEN + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_TOP):
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_BOTTOM):
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_LEFT):
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_RIGHT):
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_TOPLEFT):
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_TOPRIGHT):
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_BOTTOMLEFT):
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.WALL_BOTTOMRIGHT):
                map_matrix[2*i+1][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i][2*j] = Back.BLACK + '  '
            elif(map[i][j].split(':')[0] == pt.SPAWN):
                map_matrix[2*i][2*j] = Back.WHITE + '  '
                map_matrix[2*i][2*j+1] = Back.WHITE + '  '
                map_matrix[2*i+1][2*j] = Back.WHITE + '  '
                map_matrix[2*i+1][2*j+1] = Back.WHITE + '  '
            elif(map[i][j].split(':')[0] == pt.CANNON):
                map_matrix[2*i][2*j] = Back.GREEN + '  '
                map_matrix[2*i][2*j+1] = Back.GREEN + '  '
                map_matrix[2*i][2*j+2] = Back.GREEN + '  '
                map_matrix[2*i][2*j+3] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+1][2*j] = Back.GREEN + '  '
                map_matrix[2*i+1][2*j+1] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+1][2*j+2] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+1][2*j+3] = Back.GREEN + '  '
                map_matrix[2*i+2][2*j] = buildingColor(V,map[i][j]) + 'CA'
                map_matrix[2*i+2][2*j+1] = buildingColor(V,map[i][j]) + 'NN'
                map_matrix[2*i+2][2*j+2] = buildingColor(V,map[i][j]) + 'ON' 
                map_matrix[2*i+2][2*j+3] = Back.GREEN + '  '
                map_matrix[2*i+3][2*j] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j+1] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j+2] = Back.GREEN + '  '
                map_matrix[2*i+3][2*j+3] = Back.GREEN + '  '
                map[i][j+1] = -1
                map[i+1][j] = -1
                map[i+1][j+1] = -1
            elif(map[i][j].split(':')[0] == pt.HUT):
                map_matrix[2*i][2*j] = Back.GREEN + '  '
                map_matrix[2*i][2*j+1] = Back.BLACK + '  '
                map_matrix[2*i][2*j+2] = Back.BLACK + '  '
                map_matrix[2*i][2*j+3] = Back.GREEN + '  '
                map_matrix[2*i+1][2*j] = Back.BLACK + '  '
                map_matrix[2*i+1][2*j+1] = Back.BLACK + 'HU'
                map_matrix[2*i+1][2*j+2] = Back.BLACK + 'T '
                map_matrix[2*i+1][2*j+3] = Back.BLACK + '  '
                map_matrix[2*i+2][2*j] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+2][2*j+1] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+2][2*j+2] = Back.BLUE + '  '
                map_matrix[2*i+2][2*j+3] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j+1] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j+2] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+3][2*j+3] = buildingColor(V,map[i][j]) + '  '
                map[i][j+1] = -1
                map[i+1][j] = -1
                map[i+1][j+1] = -1
            elif(map[i][j].split(':')[0] == pt.TOWNHALL):  
                for a in range(2*i,2*i+8):
                    for b in range(2*j,2*j+6):
                        map_matrix[a][b] = Back.GREEN + '  '
                map_matrix[2*i][2*j+2] = Back.MAGENTA + '  '
                map_matrix[2*i][2*j+3] = Back.MAGENTA + '  '
                map_matrix[2*i+1][2*j+1] = Back.MAGENTA + '  '
                map_matrix[2*i+1][2*j+2] = Back.BLUE + '  '
                map_matrix[2*i+1][2*j+3] = Back.BLUE + '  '
                map_matrix[2*i+1][2*j+4] = Back.MAGENTA + '  '
                map_matrix[2*i+2][2*j] = Back.MAGENTA + '  '
                map_matrix[2*i+2][2*j+1] = Back.MAGENTA + '  '
                map_matrix[2*i+2][2*j+2] = Back.BLUE + '  '
                map_matrix[2*i+2][2*j+3] = Back.BLUE + '  '
                map_matrix[2*i+2][2*j+4] = Back.MAGENTA + '  '
                map_matrix[2*i+2][2*j+5] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j+1] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j+2] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j+3] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j+4] = Back.MAGENTA + '  '
                map_matrix[2*i+3][2*j+5] = Back.MAGENTA + '  '
                for a in range(2*i+4,2*i+8):
                    for b in range(2*j,2*j+6):
                        map_matrix[a][b] = buildingColor(V,map[i][j]) + '  '
                map_matrix[2*i+4][2*j+1] = buildingColor(V,map[i][j]) + Fore.BLACK + 'TO'
                map_matrix[2*i+4][2*j+2] = buildingColor(V,map[i][j]) + Fore.BLACK + 'WN'
                map_matrix[2*i+4][2*j+3] = buildingColor(V,map[i][j]) + Fore.BLACK + 'HA'
                map_matrix[2*i+4][2*j+4] = buildingColor(V,map[i][j]) + Fore.BLACK + 'LL'
                map_matrix[2*i+6][2*j+2] = Back.BLACK + '  '
                map_matrix[2*i+6][2*j+3] = Back.BLACK + '  '
                map_matrix[2*i+7][2*j+2] = Back.BLACK + '  '
                map_matrix[2*i+7][2*j+3] = Back.BLACK + '  '

                map[i][j+1] = -1
                map[i][j+2] = -1
                for k in range (i+1,i+4):
                    map[k][j] = -1
                    map[k][j+1] = -1
                    map[k][j+2] = -1
    pos = pt.KING_POS

    if(pos != -1):
        a= 2*pos[0]
        b = 2*pos[1]
        map_matrix[a][b] = Back.YELLOW + Fore.BLACK + '  '
        map_matrix[a+1][b] = Back.YELLOW + Fore.BLACK + 'KI'
        map_matrix[a][b+1] = Back.YELLOW + Fore.BLACK + '  '
        map_matrix[a+1][b+1] = Back.YELLOW + Fore.BLACK + 'NG'

    for barb in barbarians:
        a= 2*barb.position[0]
        b = 2*barb.position[1]
        map_matrix[a][b] = barbColor(barb) + Fore.BLACK + 'BA'
        map_matrix[a+1][b] = barbColor(barb) + Fore.BLACK + '  '
        map_matrix[a][b+1] = barbColor(barb) + Fore.BLACK + 'RB'
        map_matrix[a+1][b+1] = barbColor(barb) + Fore.BLACK + '  '

    for dr in dragons:
        a= 2*dr.position[0]
        b = 2*dr.position[1]
        map_matrix[a][b] = drColor(dr) + Fore.BLACK + 'DR'
        map_matrix[a+1][b] = drColor(dr) + Fore.BLACK + 'ON'
        map_matrix[a][b+1] = drColor(dr) + Fore.BLACK + 'AG'
        map_matrix[a+1][b+1] = drColor(dr) + Fore.BLACK + '  '



    store_replay(map_matrix)

    
    for i in range(map_matrix.shape[0]):
        for j in range(map_matrix.shape[1]):
            print(map_matrix[i][j], end='')
        print('')


    

def showKingHealth(health):
    health_bar = []
    health_scaled = int(health/10)
    for i in range(10):
        if(i<health_scaled):
            health_bar.append(Back.RED + '  ')
        else:
            health_bar.append(Back.BLACK + '  ')
    store_healthbar(health_bar)        
    return health_bar

def update_map(map):
    map_mat = printMap(map)
    return map_mat



def store_replay(map_matrix):
    # create a file name
    file_name = 'replay_' + now.strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
    # open the file
    file = open('./replays/' + file_name, 'a')
    for i in range(map_matrix.shape[0]):
        for j in range(map_matrix.shape[1]):
            file.write(map_matrix[i][j])
        file.write('\n')
    file.close()
    

def store_healthbar(health_bar):
    # create a file name
    file_name = 'replay_' + now.strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
    # open the file
    file = open('./replays/' + file_name, 'a')
    file.write(Back.BLACK + Fore.WHITE +'King Health: ')
    for i in range(len(health_bar)):
        file.write(health_bar[i])
    file.write('\n')
    file.write("=====")
    file.close()