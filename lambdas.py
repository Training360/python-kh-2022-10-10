# Írjatok egy függvényt, mely paraméterül kap egy listát,
# és minden elemét megszorozza kettővel.

def multiply(numbers):
    result = []
    for number in numbers:
        atomic_result = number * 2
        result.append(atomic_result)
    return result

# Írj egy függvényt, mely a paraméterül kap egy listát,
# és minden eleméhez hozzáad ötöt

def add_five(numbers):
    result = []
    for number in numbers:
        atomic_result = number + 5
        result.append(atomic_result)
    return result

print(multiply([1, 2, 3, 4, 5]))
print(add_five([1, 2, 3, 4, 5]))

def apply(numbers, f):
    result = []
    for number in numbers:
        atomic_result = f(number)
        result.append(atomic_result)
    return result


def multiply(number):
    return number * 2

def add_five(number):
    return number + 5

print(apply([1, 2, 3, 4, 5], multiply))
print(apply([1, 2, 3, 4, 5], add_five))

print(apply([1, 2, 3, 4, 5], lambda n: n * 3))

def xxx_yyy_zzz(n):
    return n * 3


print(apply([1, 2, 3, 4, 5], xxx_yyy_zzz))

# First-class citizen, first-class function: átadható paraméterként, megadható visszatérési
# értékként, változónak értékül adható

def print_name(name):
    print(f"Hello {name}")


print_name("John Doe")

print("***")

f = print_name

f("Jack Doe")


def print_names(transform):
    for i in range(0, 10):
        print(transform("Trainer"))

# def convert_to_uppercase(s):
    # return s.upper()

# convert_to_uppercase = lambda s: s.upper()
# print_names(convert_to_uppercase)


print_names(lambda s: s.upper())

print_names(lambda s: s.lower())

print_names(lambda s: s * 5)

# increment = 5
# def add(number):
    # return number + increment

# Lambda függvény gyártás
def make_incrementor(increment):
    return lambda number: number + increment

increment_with_42 = make_incrementor(42)

i = 10
print(increment_with_42(i))

increment_with_52 = make_incrementor(52)

print(increment_with_52(i))

price = 100_000
vat = 1.25
print(price * vat)

# Változó kiemelése magic numbernél
gas_amount = 123_000
days_of_year = 365
print(gas_amount * days_of_year)