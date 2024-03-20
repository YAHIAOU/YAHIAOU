from pathlib import Path

pwd = Path('.')

print(pwd.absolute())

cible = pwd / 'cible'
print(cible.absolute())

##########

class Vecteur2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vecteur2):
        x = self.x + vecteur2.x
        y = self.y + vecteur2.y
        return vecteur2(x,y)
    
    def __repr__(self):
        return str(self.__dict__)
    
v1 = Vecteur2D(3, 4)
v2 = Vecteur2D(-1, 5)
print(v1)
print(v2)

