# Oliver

# This document defines all the base information of a game and will
# be used if pickle is impossible


class Game:
    def __init__(self):
        # Hero
        #self.Hlevel = 1
        #self.Hmsircle = 0
        #self.Hhealth = 50
        #self.Hattack = 20
        #self.Hdefence = 0
        #self.Hagility = 5
        #self.Hmana = 0

        #self.Hequiped = 0
        #self.Hitems = []

        hero = Entity()
        hero.name = "Hero"
        hero.level = 1
        hero.exp = 0
        hero.attack = 10
        hero.health = 50

        dragon = Entity()
        dragon.name = "Dragon"
        dragon.level = 3
        dragon.exp = 2
        dragon.attack = 20
        dragon.health = 100
        
        goblin = Entity()
        goblin.name = "Goblin"
        goblin.level = 1
        goblin.exp = 2
        goblin.attack = 2
        goblin.health = 10

        self.Hero = hero
        self.Enemies = [goblin, dragon]
        
        self.slayn = []

class Entity:
    level: int
    exp: int
    health: int
    attack: int
    name: str
    def __init__(self):
        pass