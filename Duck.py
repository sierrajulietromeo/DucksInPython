from FlyBehaviour import FlyBehaviour
from QuackBehaviour import QuackBehaviour


class Duck:

  def __init__(self):
    self.flyBehaviour = FlyBehaviour()
    self.quackBehaviour = QuackBehaviour()
    
  def display(self):
    pass
  
  def performFly(self):
    self.flyBehaviour.fly()
  
  def performQuack(self):
    self.quackBehaviour.quack()
  
  def swim(self):
    print("All ducks float")