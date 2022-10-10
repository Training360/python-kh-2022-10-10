# Lista származtatás

numbers = [i for i in range(0, 5)]
print(numbers)

numbers = []
for i in range(0, 5):
    numbers.append(i)

print(numbers)

numbers = [i ** 2 for i in range(0, 5)]
print(numbers)

names = ["John Doe", "Jack Doe"]
uppers = [n.upper() for n in names]
print(uppers)

numbers = [1, 2, 4, 7, 8]
result = [i - 1 for i in numbers] # Transzformáció
print(result)

names = ["John Doe", "Jack Doe", "Bob"]
result = [len(n) for n in names]
print(result)

names = ["John Doe", "Jack Doe", "Bob"]
result = [n for n in names if "J" in n]
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = [n for n in numbers if n % 2 == 0] # Szűrés, filter
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = [n * 2 for n in numbers if n % 2 == 0]
print(result)

# Írj egy get_all_positive_numbers(numbers) függvényt,
    # egy új listába visszaadja az összes pozitív számot

# Írj egy függvényt, ami double_values(numbers), ami visszaad
    # egy új listát az eredeti listában lévő számok kétszeresével
    # [1, 2, 3] -> [2, 4, 6]

def get_all_positive_numbers(numbers):
    return [n for n in numbers if n > 0]

def double_values(numbers):
    return [n * 2 for n in numbers]