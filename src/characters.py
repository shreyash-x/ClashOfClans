import points as pt
import collections

barbarians = []
dragons = []


class Barbarian:
    def __init__(self, position):
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.position = position
        self.alive = True

    def move(self, pos, V):
        if(self.alive == False):
            return
        vmap = V.map
        r = abs(pos[0] - self.position[0])
        c = abs(pos[1] - self.position[1])
        if(r + c == 1):
            info = vmap[pos[0]][pos[1]]
            if(info == pt.TOWNHALL):
                self.break_building(pos[0], pos[1], V)
                return
            x = int(info.split(':')[1])            
            y = int(info.split(':')[2])
            self.break_building(x,y,V)
            return
        elif(r==0):
            if(pos[1] > self.position[1]):
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] + 1
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[1] += 1
                    if(abs(pos[1] - self.position[1]) == 1):
                        break
            else:
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] - 1
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[1] -= 1
                    if(abs(pos[1] - self.position[1]) == 1):
                        break
        elif(r > 1):
            if(pos[0] > self.position[0]):
                for i in range(self.speed):
                    r = self.position[0] + 1
                    c = self.position[1]
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[0] += 1
                    if(self.position[0] == pos[0]):
                        return
            else:
                for i in range(self.speed):
                    r = self.position[0] - 1
                    c = self.position[1]
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[0] -= 1
                    if(self.position[0] == pos[0]):
                        return
        elif(c > 1):
            if(pos[1] > self.position[1]):
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] + 1
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[1] += 1
                    if(self.position[1] == pos[1]):
                        return
            else:
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] - 1
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[1] -= 1
                    if(self.position[1] == pos[1]):
                        return
        elif(r+c == 2):
            if(pos[0] > self.position[0]):
                for i in range(self.speed):
                    r = self.position[0] + 1
                    c = self.position[1]
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[0] += 1
            else:
                for i in range(self.speed):
                    r = self.position[0] - 1
                    c = self.position[1]
                    if(self.check_for_walls(r,c,vmap)):
                        self.break_wall(r,c,V)
                        return
                    self.position[0] -= 1

    def check_for_walls(self, x, y, vmap):
        if(vmap[x][y] == pt.WALL):
            return True
        return False

    def break_wall(self, x, y, V):
        target = V.wall_objs[(x,y)]
        self.attack_target(target)

    def break_building(self, x, y, V):
        target=None
        if(V.map[x][y] == pt.TOWNHALL):
            target = V.town_hall_obj
        else:
            all_buildings = collections.ChainMap(V.hut_objs, V.cannon_objs)
            target = all_buildings[(x,y)]
        self.attack_target(target)

    def attack_target(self, target):
        if(self.alive == False):
            return
        target.health -= self.attack
        if target.health <= 0:
            target.health = 0
            target.destroy()

    def kill(self):
        self.alive = False
        barbarians.remove(self)

    def deal_damage(self,hit):
        if(self.alive == False):
            return
        self.health -= hit
        if self.health <= 0:
            self.health = 0
            self.kill()

    def rage_effect(self):
        self.speed = self.speed*2
        self.attack = self.attack*2

    def heal_effect(self):
        self.health = self.health*1.5
        if self.health > self.max_health:
            self.health = self.max_health

class Dragon:
    def __init__(self, position):
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.position = position
        self.alive = True

    def move(self, pos, V):
        if(self.alive == False):
            return
        vmap = V.map
        r = abs(pos[0] - self.position[0])
        c = abs(pos[1] - self.position[1])
        if(r + c == 1):
            info = vmap[pos[0]][pos[1]]
            if(info == pt.TOWNHALL):
                self.break_building(pos[0], pos[1], V)
                return
            x = int(info.split(':')[1])            
            y = int(info.split(':')[2])
            self.break_building(x,y,V)
            return
        elif(r==0):
            if(pos[1] > self.position[1]):
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] + 1
                    self.position[1] += 1
                    if(abs(pos[1] - self.position[1]) == 1):
                        break
            else:
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] - 1
                    self.position[1] -= 1
                    if(abs(pos[1] - self.position[1]) == 1):
                        break
        elif(r > 1):
            if(pos[0] > self.position[0]):
                for i in range(self.speed):
                    r = self.position[0] + 1
                    c = self.position[1]
                    self.position[0] += 1
                    if(self.position[0] == pos[0]):
                        return
            else:
                for i in range(self.speed):
                    r = self.position[0] - 1
                    c = self.position[1]
                    self.position[0] -= 1
                    if(self.position[0] == pos[0]):
                        return
        elif(c > 1):
            if(pos[1] > self.position[1]):
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] + 1
                    self.position[1] += 1
                    if(self.position[1] == pos[1]):
                        return
            else:
                for i in range(self.speed):
                    r = self.position[0]
                    c = self.position[1] - 1
                    self.position[1] -= 1
                    if(self.position[1] == pos[1]):
                        return
        elif(r+c == 2):
            if(pos[0] > self.position[0]):
                for i in range(self.speed):
                    r = self.position[0] + 1
                    c = self.position[1]
                    self.position[0] += 1
            else:
                for i in range(self.speed):
                    r = self.position[0] - 1
                    c = self.position[1]
                    self.position[0] -= 1

    def break_building(self, x, y, V):
        target=None
        if(V.map[x][y] == pt.TOWNHALL):
            target = V.town_hall_obj
        else:
            all_buildings = collections.ChainMap(V.hut_objs, V.cannon_objs)
            target = all_buildings[(x,y)]
        self.attack_target(target)

    def attack_target(self, target):
        if(self.alive == False):
            return
        target.health -= self.attack
        if target.health <= 0:
            target.health = 0
            target.destroy()

    def kill(self):
        self.alive = False
        dragons.remove(self)

    def deal_damage(self,hit):
        if(self.alive == False):
            return
        self.health -= hit
        if self.health <= 0:
            self.health = 0
            self.kill()

    def rage_effect(self):
        self.speed = self.speed*2
        self.attack = self.attack*2

    def heal_effect(self):
        self.health = self.health*1.5
        if self.health > self.max_health:
            self.health = self.max_health


def spawnBarbarian(pos):
    #convert tuple to list
    pos = list(pos)
    barb = Barbarian(pos)
    barbarians.append(barb)

def spawnDragon(pos):
    #convert tuple to list
    pos = list(pos)
    dr = Dragon(pos)
    dragons.append(dr)


def move_barbarians(V):
    for barb in barbarians:
        if(barb.alive == False):
            continue
        closest_building = search_for_closest_building(barb.position, V.map)
        if(closest_building == None):
            continue
        barb.move(closest_building, V)

def move_dragons(V):
    for dr in dragons:
        if(dr.alive == False):
            continue
        closest_building = search_for_closest_building(dr.position, V.map)
        if(closest_building == None):
            continue
        dr.move(closest_building, V)

def search_for_closest_building(pos, vmap):
    closest_building = None
    closest_dist = 10000
    for i in range(len(vmap)):
        for j in range(len(vmap[i])):
            item = vmap[i][j].split(':')[0]
            if (item == pt.HUT or item == pt.CANNON or item == pt.TOWNHALL):
                dist = abs(i - pos[0]) + abs(j - pos[1])
                if(dist < closest_dist):
                    closest_dist = dist
                    closest_building = (i,j)
    return closest_building


