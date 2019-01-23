'''
  characters.py
  Paul Talaga
  Jan 18, 2019
'''

class Character:

  def __init__(self,name): # constructor
    self.name = name  # Instance variables, unique to each instance
    self.color = "None"
    self.health = 100

  def fight(self):
    print("You faught and lost 10 health")
    self.health = self.health - 10

  def duck(self):
    print("duck")

  def display(self):
    #print("Character %s , with color %s, and damage %i" % (self.name, self.color, self.damage))  # old
    print("Character {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old


gremlin = Character("Gremlin")
gnome = Character("Gnome")

gremlin.display()
gnome.display()

# Fight
gremlin.fight()

gremlin.display()
gnome.display()


