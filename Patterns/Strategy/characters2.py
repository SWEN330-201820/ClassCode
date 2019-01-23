'''
  characters2.py
  Paul Talaga
  Jan 18, 2019
'''

class Character:

  def __init__(self): # constructor
    self.name = "None"  # Instance variables, unique to each instance
    self.color = "None"
    self.health = 100

  def fight(self):
    print("You faught and lost 10 health")
    self.health = self.health - 10

  def display(self):
    #print("Character %s , with color %s, and damage %i" % (self.name, self.color, self.damage))  # old
    print("Character {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old


class Gremlin(Character):
  def __init__(self, name):
    self.name = name
    self.color = "Green"
    self.health = 100

  def display(self):
    print("Gremlin {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old

class Gnome(Character):
  def __init__(self, name):
    self.name = name
    self.color = "Grey"
    self.health = 50

  def display(self):
    print("Gnome {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old

class Wizard(Character):
  def __init__(self, name):
    self.name = name
    self.color = "Blue"
    self.health = 150

  def display(self):
    print("Wizard {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old

class Tree(Character):
  def __init__(self, name):
    self.name = name
    self.color = "Green"
    self.health = 1000

  def display(self):
    print("Tree {} , with color {}, and health {}".format(self.name, self.color, self.health))  # old

  def fight(self):
    print("Trees can't fight!")

characters = []
characters.append(Gremlin("Greg"))
characters.append(Gnome("Bob"))
characters.append(Wizard("Gandolf"))
characters.append(Tree("Fred"))

for c in characters:
  c.display()

print("\n")

print("\nA Fight happened for all\n")
for c in characters:
  c.fight()

for c in characters:
  c.display()


