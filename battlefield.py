from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
 def __init__(self):
    self.robot = Robot("Iron Giant")
    self.dinosaur = Dinosaur('Godzilla', 100)
      
 def run_game(self):
    self.display_welcome()
    self.battle_phase()
    
    


 def display_welcome(self):
    print(f'LETS GET READY TO RUMBLE!! Good evening and welcome to tonights fight which promises to be a classic in every sense of the word. In the red corner, weighing in at 99,000 tons and the undisputed world champion the legend known as {self.dinosaur.name}….. And in the blue corner weighing in at 55,000 tons ……. {self.robot.name} !! And tonights prize? ETERNAL GLORRRYYY!')
    
  

 def battle_phase(self):
   while self.dinosaur.health > 0 or self.robot.health > 0:
     if self.dinosaur.health >= 0 and self.robot.health >= 0:
      self.dinosaur.attack(self.robot)
      print(f'{self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power}!')
      print(f'{self.robot.name} has {self.robot.health} remaining!')
      self.robot.attack(self.dinosaur)
      print(f'{self.robot.name} attacked {self.dinosaur.name} with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power}!')
      print(f'{self.dinosaur.name} has {self.dinosaur.health} remaining!') 
     if self.robot.health <= 0 or self.dinosaur.health <= 0:
       self.display_winner()
     
    
  

 def display_winner(self):
   if self.dinosaur.health <= 0:
      print(f'{self.robot.name} has won the match, i did not think he would find a battery to get in the last hit what a crazy fight!!')
   elif self.robot.health <= 0:
      print(f'The winner and still undefeted champion {self.dinosaur.name}')  
    
  
  
  
  
 
    