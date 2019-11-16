# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:47:49 2019

@author: lydia
"""
class Adventurer:

#==========================================
# Purpose: 
#   A constructor that initializes an Adventurer object 
# Input Parameter(s): 
#   name is a string that represents the the name of the Adventurer
#   level is an integer that represents the Adventurer's level
#   strength is an integer that represents the Adventurer's strength
#   speed is an integer that represents the Adventurer's speed
#   power is an integer that represents the Adventurer's power   
# Return Value(s): 
#   None    
#==========================================

    def __init__(self, name, level, strength, speed, power):    
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = level * 6
        self.hidden = False
        
#==========================================
# Purpose: 
#   Creates a representation of the Adventurer        
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string representation of the Adventurer        
#==========================================

    def __repr__(self):
        return self.name + ' - HP: ' + str(self.HP) 

#==========================================
# Purpose: 
#   Simulates an Adventurer attacking another Adventurer. If not hidden, the 
#   target loses hit points equal to the strength of the attacker plus four.        
# Input Parameter(s): 
#   target is another Adventurer object        
# Return Value(s): 
#   None        
#==========================================

    def attack(self,target):
        if target.hidden == True:
            print(self.name+" can't see "+target.name)
        else:
            damage = self.strength + 4
            target.HP -= damage
            print(self.name+" attacks "+target.name+" for "+str(damage)+" damage")

#==========================================
# Purpose: 
#   Complares two Adventurers to see if the left operand (self) has a lower
#    number of Hit Points than the right operand (other).          
# Input Parameter(s): 
#   other is an Adventurer        
# Return Value(s): 
#   True if the left operand (self) has a lower number of Hit Points 
#   than the right operand (other). False otherwise.         
#==========================================

    def __lt__(self,other):
        if self.HP < other.HP:
            return True
        else: 
            return False            

class Fighter(Adventurer):

#==========================================
# Purpose: 
#   A constructor that initializes an Fighter object 
# Input Parameter(s): 
#   name is a string that represents the the name of the Fighter
#   level is an integer that represents the Fighter's level
#   strength is an integer that represents the Fighter's strength
#   speed is an integer that represents the Fighter's speed
#   power is an integer that represents the Fighter's power   
# Return Value(s): 
#   None    
#==========================================    
    
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 12             

#==========================================
# Purpose: 
#   Simulates a Fighter attacking another Adventurer. If not hidden, the 
#   target loses hit points equal to the strength of the attacker doubled plus six.        
# Input Parameter(s): 
#   target is another Adventurer object        
# Return Value(s): 
#   None        
#==========================================
        
    def attack(self,target):
        if target.hidden == True:
            print(self.name+" can't see "+target.name)
        else:
            damage = self.strength * 2 + 6 
            target.HP -= damage
            print(self.name+" attacks "+target.name+" for "+str(damage)+" damage")


class Thief(Adventurer):

#==========================================
# Purpose: 
#   A constructor that initializes a Thief object 
# Input Parameter(s): 
#   name is a string that represents the the name of the Thief
#   level is an integer that represents the Thief's level
#   strength is an integer that represents the Thief's strength
#   speed is an integer that represents the Thief's speed
#   power is an integer that represents the Thief's power   
# Return Value(s): 
#   None    
#========================================== 
     
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)  
        self.HP = level * 8
        self.hidden = True

#==========================================
# Purpose: 
#   Simulates a Thief attacking another Adventurer.        
# Input Parameter(s): 
#   target is another Adventurer object        
# Return Value(s): 
#   None        
#==========================================
        
    def attack(self,target):
        if self.hidden == False: 
            Adventurer.attack(self,target)
        elif target.hidden == True and self.speed < target.speed:
            print(self.name+" can't see "+target.name)
        else:
            damage = (self.speed + self.level) * 5
            target.HP -= damage
            self.hidden = False
            target.hidden = False
            print(self.name+" sneak attacks "+target.name+" for "+str(damage)+" damage")
            

class Wizard(Adventurer):

#==========================================
# Purpose: 
#   A constructor that initializes a Wizard object 
# Input Parameter(s): 
#   name is a string that represents the the name of the Wizard
#   level is an integer that represents the Wizard's level
#   strength is an integer that represents the Wizard's strength
#   speed is an integer that represents the Wizard's speed
#   power is an integer that represents the Wizard's power   
# Return Value(s): 
#   None    
#========================================== 
            
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = power

#==========================================
# Purpose: 
#   Simulates a Wizard attacking another Adventurer.        
# Input Parameter(s): 
#   target is another Adventurer object        
# Return Value(s): 
#   None        
#==========================================
        
    def attack(self,target):
        if self.fireballs_left == 0: 
            Adventurer.attack(self,target)
        else:
            target.hidden = False
            damage = self.level * 3
            target.HP -= damage
            self.fireballs_left -= 1
            print(self.name+" casts fireball on "+target.name+" for "+str(damage)+" damage")
 
#==========================================
# Purpose: 
#   Simulates a duel between two Adventurers.        
# Input Parameter(s): 
#   adv1 is an Adventurer object representing the first attacker
#   adv2 is an Adventurer object representing the other player in the duel            
# Return Value(s): 
#   True if adv1, the first attacker wins. False otherwise.        
#==========================================           
            
def duel(adv1, adv2):
    turn = 1
    while adv1.HP > 0 and adv2.HP > 0:
        if turn % 2 != 0:
            print(adv1)
            print(adv2)
            adv1.attack(adv2)
        else:    
            adv2.attack(adv1)
        turn += 1
    print(adv1)
    print(adv2)
    if adv1.HP <= 0 and adv2.HP > 0:
        print(adv2.name+" wins!")
        return False
    elif adv2.HP <= 0 and adv1.HP > 0:
        print(adv1.name+" wins!")
        return True            
    else:
        print("Everyone loses!")
        return False
 
#==========================================
# Purpose: 
#   Simulates a tournament between Adventurers.        
# Input Parameter(s): 
#   adv_list is a list of Adventurer objects.            
# Return Value(s): 
#   The Adventurer who wins the tournament or None if the list is empty.        
#==========================================     

def tournament(adv_list):
    while len(adv_list) > 1:
        adv_list.sort()
        winner2 = duel(adv_list[-2],adv_list[-1])
        if winner2 == True:
            del adv_list[-1]
        else:
            del adv_list[-2]
    if len(adv_list) == 0:
        return None
    if len(adv_list) == 1:
        return adv_list[0]
    