import numpy as np
import points as pt
from characters import barbarians, dragons


class Building:        
    def destroy(self):
        self.destroyed = True
        if self.type == 'wall':
            self.V.remove_wall(self)
        elif self.type == 'hut':
            self.V.remove_hut(self)
        elif self.type == 'cannon':
            self.V.remove_cannon(self)
        elif self.type == 'townhall':
            self.V.remove_town_hall(self)


class Hut(Building):
    def __init__(self, position,V):
        self.position = position
        self.dimensions = (2,2)
        self.V = V
        self.destroyed = False
        self.health = 40
        self.max_health = 40
        self.type = 'hut'

class Cannon(Building):
    def __init__(self, position,V):
        self.position = position
        self.dimensions = (2,2)
        self.V = V
        self.destroyed = False
        self.health = 60
        self.max_health = 60
        self.type = 'cannon'
        self.attack = 5
        self.attack_radius = 5
        self.isShooting = False

    def scan_for_targets(self,King):
        self.isShooting = False
        for barb in barbarians:
            if (barb.position[0] - self.position[0])**2 + (barb.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(barb)
                return
        for dragon in dragons:
            if (dragon.position[0] - self.position[0])**2 + (dragon.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(dragon)
                return
        
        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King)

    def attack_target(self, target):
        if(self.destroyed == True):
            return
        target.deal_damage(self.attack)

class Wall(Building):
    def __init__(self, position,V):
        self.position = position
        self.dimensions = (1,1)
        self.V = V
        self.destroyed = False
        self.health = 20
        self.max_health = 20
        self.type = 'wall'

class TownHall(Building):
    def __init__(self, position,V):
        self.position = position
        self.dimensions = (4,3)
        self.V = V
        self.destroyed = False
        self.health = 100
        self.max_health = 100
        self.type = 'townhall'



def shoot_cannons(King,V):
    for cannon in V.cannon_objs:
        V.cannon_objs[cannon].scan_for_targets(King)