# Még két nagyon elterjedt algoritmus
# Szűrés
# Írj egy get_all_positive_numbers(numbers) függvényt,
    # egy új listába visszaadja az összes pozitív számot
def get_all_positive_numbers(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result

# Transzformáció
# Írj egy függvényt, ami double_values(numbers), ami visszaad
    # egy új listát az eredeti listában lévő számok kétszeresével
    # [1, 2, 3] -> [2, 4, 6]
def double_values(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


numbers = [-1, 1, -1, 1, -1, 2]

positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)

is_positive = lambda n: n > 0
positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)

double_values = [n * 2 for n in numbers]
print(double_values)

multiply_with_two = lambda n: n * 2
double_values = list(map(multiply_with_two, numbers))
print(double_values)

numbers = [1, 2, 3, 4]
print(list(map(lambda x: 2 * x, numbers)))

