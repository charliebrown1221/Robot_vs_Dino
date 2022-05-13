from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
 def __init__(self):
    self.robot = Robot("Iron Giant")
    self.dinosaur = Dinosaur('Godzilla', 100)
      
 def run_game(self):
    display_welcome(self)
    battle_phase(self)
    display_winner(self)
    


 def display_welcome(self):
    print(f'LETS GET READY TO RUMBLE!! Good evening and welcome to tonights fight which promises to be a classic in every sense of the word. In the red corner, weighing in at 99,000 tons and the undisputed world champion the legend known as {self.name.dinosaur}….. And in the blue corner weighing in at 55,000 tons ……. {self.name.robot} !! And tonights prize? ETERNAL GLORRRYYY!')
    
  

 def battle_phase(self):
   while self.dinosaur.attack(self.robot):
     print(f'{self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power}!')
     print(f'{self.robot.name} has {self.robot.health} remaining!')
   if self.robot.attack(self.dinosaur):
      print(f'{self.robot.name} attacked {self.dinosaur.name} with {self.Weapon.name} for {self.Weapon.attack_power}!')
      print(f'{self.robot.name} has {self.robot.health} remaining!') 
     
    
  

 def display_winner(self):
    if self.dinosaur.health == 0:
      print(f'{self.robot.name} has won the match, what a crazy fight!!')
    elif self.robot.helth == 0:
      print(f'The winner and still undefeted champion {self.dinosaur.name}')  
    
  
  
  
  
 
    