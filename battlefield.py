from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
  def __init__(self):
    self.robot = Robot("Iron Giant")
    self.dinosaur = Dinosaur('godzilla', 100)
      
  def test(self):
    self.dinosaur.attack(self.robot)
    print(self.robot.health)
    