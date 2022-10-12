# Hozzatok létre egy olyan Circle nevezetű osztályt,
# melynek konstruktorban át kell adni egy sugarat!
# Írjatok egy metódust, ami lekéri a sugár méretét (get)!
# Írjatok egy másik metódust, ami visszaadja a területét!
# t = r ** 2 * pi

from math import pi


class Circle:


    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def get_area(self) -> float:
        return self.radius ** 2 * pi

    def __str__(self):
        return f"Kor {self.radius} sugaru."

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius == other.radius


    def __hash__(self) -> int:
        return hash(self.radius)


circle = Circle(10)
print(circle.get_radius())
print(circle.get_area())

print(circle)

another_circle = Circle(10)

print(circle == another_circle)
print(hash(circle))
print(hash(another_circle))

# i = 10
# print(i)
# i = "hello"
# print(i)

# circle2 = Circle("grrr")
# print(circle2.get_radius())
# print(circle2.get_area())

