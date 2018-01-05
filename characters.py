# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:41:03 2017

@author: clawford
"""

class BaseCharacter(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def printName(self):
        print(self.name)
        
class NPC(BaseCharacter):
    pass
class PC(BaseCharacter):
    def __init__(self, name):
        self.weapon = weapon()
        super(PC,self).__init__(name)

class Friendly(NPC):
    pass
class Enemy(NPC):
    def __init__(self):
        self.attackDamage = 5
class Archer(PC):
    pass
class Butcher(PC):
    pass
class GreenLantern(PC):
    pass
class weapon(object):
    def __init__(self):
        self.name = "AXE"
        
if __name__ == '__main__':
	enemy = Enemy()
	print (enemy.attackDamage)
	butcher = Butcher("bob")
	print (butcher.weapon.name)