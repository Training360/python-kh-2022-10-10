print(type(5))

print(type("John Doe"))

name = "John Doe"
print(name.upper())

class Client:

    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def get_name(self):
        return self.name

    
    def get_year_of_birth(self):
        return self.year_of_birth

    def set_name(self, new_name):
        self.name = new_name

    def calculate_age(self, actual_year):
        return actual_year - self.year_of_birth


john = Client("John Doe", 1970) # Példányosítás, itt kerül meghívásra a konstruktor

print(john.get_name())
print(type(john))

jack = Client("Jack Doe", 1980)
print(jack.get_name())
print(jack.get_year_of_birth())

jack.set_name("Jack Smith")
print(jack.get_name())


client = ("John Doe", 1970)
# Tuple: sehol nincs leírva, hogy az első a neve, és 0. indexszel kell rá hivatkozni
print(client[0])
client = {"name": "John Doe", "year_of_birth": 1970} # Csak adatot tárol
print(client["name"])

print(jack.calculate_age(2022))

