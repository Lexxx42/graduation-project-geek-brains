# Написать класс для работы с векторами

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


vector1 = Vector(1, 2, -3)

vector2 = Vector(5, 5, 5)

vector3 = vector2 + vector1

print(vector3.x, vector3.y, vector3.z)
