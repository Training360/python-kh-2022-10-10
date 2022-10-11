# Defincíóban használunk: formális paraméterek
def print_name(name, count=2, welcome="Hello"):
    print(welcome)
    for i in range(count):
        print(name)


print_name("John Doe", 5) # Sorrendi kötés: positional argument
# Hívás helyén: aktuális paraméterek
print_name("John Doe", 2, "Grrr")

print_name(name="John Doe", count=5) # Név szerinti kötés: keyword

print_name(count=5, name="John Doe", welcome="xyz") # Név szerinti kötés

print_name("John Doe")

print_name("John Doe", welcome="xxx") # Keverjük a sorrendi és a név szerinti kötést

def sum_numbers(name, *args):
    print(name)
    print(type(args))
    print(args)
    for number in args:
        print(number)


sum_numbers("John Doe", 1, 2, 3, 4, ("a", "b"))


def print_parameters(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['year_of_birth'])


print_parameters(name="John Doe", year_of_birth=1970)

def print_numbers(*args):
    print(args)


print_numbers("John Doe")