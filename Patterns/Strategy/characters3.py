'''
  characters3.py
  Paul Talaga
  Jan 18, 2019
  Desc:
    From characters2, we made the display function __str__ so the object can be printed
    Now the different types of Fighting are defined and Characters can specify which one they want.
    By default they don't fight (for the tree).
    Thus all Character's fighing characteristics (Kick or Puch) can easily be changed without changing
    a Character.

'''

# Fighting base class, which does nothing
class Fight:
  def __init__(self, parent):
    self.parent = parent      # Save a reference to the parent so health can be changed

  def doFight(self):
    pass        # do nothing

# Kinds of fighting, which individual characters can use.
class Kick(Fight):
  def __init__(self,parent):
    super().__init__(parent)  # Be sure to call the init of the base class.

  def doFight(self):
    print("You kicked and lost 10 health")
    self.parent.health = self.parent.health - 10

class Punch(Fight):
  def __init__(self,parent):
    super().__init__(parent)

  def doFight(self):
    print("You punched and lost 5 health")
    self.parent.health = self.parent.health - 5



class Character:
  def __init__(self): # Like a constructor, but not base class __init__ not called automatically.
    self.name = "None"  # Instance variables, unique to each instance
    self.color = "None"
    self.health = 100
    self.fight_obj = Fight(self)

  def fight(self):
    self.fight_obj.doFight()
    

  def __str__(self):
    return "Character {} , with color {}, and health {}".format(self.name, self.color, self.health)  


class Gremlin(Character):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.color = "Green"
    self.health = 100
    self.fight_obj = Kick(self)

  def __str__(self):
    return "Gremlin {} , with color {}, and health {}".format(self.name, self.color, self.health)

class Gnome(Character):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.color = "Grey"
    self.health = 50
    self.fight_obj = Kick(self)

  def __str__(self):
    return "Gnome {} , with color {}, and health {}".format(self.name, self.color, self.health)

class Wizard(Character):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.color = "Blue"
    self.health = 150
    self.fight_obj = Punch(self)

  def __str__(self):
    return "Wizard {} , with color {}, and health {}".format(self.name, self.color, self.health)

class Tree(Character):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.color = "Green"
    self.health = 1000

  def __str__(self):
    return "Tree {} , with color {}, and health {}".format(self.name, self.color, self.health)  


characters = []
characters.append(Gremlin("Greg"))
characters.append(Gnome("Bob"))
characters.append(Wizard("Gandolf"))
characters.append(Tree("Fred"))

for c in characters:
  print(c)

print("\n")

print("\nA Fight happened for all\n")
for c in characters:
  c.fight()

print("\n")

for c in characters:
  print(c)


