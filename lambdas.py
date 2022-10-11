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