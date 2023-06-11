import random
import re


class Character:
    def __init__(self ,name , health ,defense ,damage ):
        self.name = name
        self.health = health
        self.defense = defense
        self.damage = damage
        self.xp = 0
        self.level= 1
    
    def attack(self,target):
        
        damage_dealt = random.randint(1,self.damage)
        target.health = target.health - damage_dealt
        print(f"{self.name} attacked {target.name} and dealt {damage_dealt} damage")
        if damage_dealt <= 0:
           damage_dealt = 0

        if target.health <= 0:
            print(f"{target.name} has been defeated")
        else:
            print(f"{target.name} has {target.health} hp remain")
    
    
    def gain_xp(self , target):
        self.xp += random.randint(10,20)
        print (f"{self.name} gained {self.xp}XP")

        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level +=1
        self.health += 10
        self.damage += 5
        self.xp = 0
        print(f"{self.name}leveled up!level {self.level}reached.")
        print(f"{self.name}'s health increased to {self.health} and damage increased to {self.damage}")        
    
    
class monster:
     
    def __init__(self , name , health , damage ,evade_attack):
        super().__init__(name,health,damage)
        self.evade_attack = evade_attack
    def evade_attack(self):
        if random.random() < self.evade_attack:
            print(f"{self.name} evaded the attack!")
            return True
        else:
            return False

    def attack(self,target):
        if self.evade_attack:
            return
        super().attack(target)
    
#valid player name

def validate_name(name):
    pattern = r'^[a-zA-Z0-9]+$'
    return re.match(pattern, name)

# Ask for the player's character name
player_name = ""
while not validate_name(player_name):
    player_name = input("Enter your character's name:").strip()
    if not player_name:
        print("Invalid name. Please enter a valid name.")

#create characters

player = Character("Player",100,20,30)
monster = Character("Monster",100,20,20)

#main code

print(f"enemy health = {monster.health}")
print(f"Your health = {player.health}")

while player.health > 0 and monster.health > 0:
    #the user choose to attack
    input("Press Enter to attack...!")
    monster.attack(player)
    player.attack(monster)
    
    
    if player.health > 0 and monster.health > 0:
        print(f"enemy health = {monster.health}")
        print(f"Your health = {player.health}")

    elif player.health > 0 and monster.health <=0:
        player.gain_xp(monster)             
