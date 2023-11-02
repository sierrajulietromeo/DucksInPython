from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack


class MallardDuck(Duck):

  def __init__(self):
    self.quackBehaviour = Quack()
    self.flyBehaviour = FlyWithWings()
  
  def display(self):
    print("I'm a real mallard duck")