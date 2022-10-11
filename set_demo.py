# Halmaz = set
# Nem enged duplikátumokat

numbers = {1, 2, 3}
print(numbers)

for number in numbers:
    print(number)

numbers = {1, 2, 3, 1, 2, 3}
print(numbers)

numbers = {1, 2}
numbers.add(3)
print(numbers)
numbers.add(3)
print(numbers)

numbers = {9, 8, 7}
print(numbers)

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}

print(set1 | set2) # unió
print(set1 & set2) # metszetét
print(set1 - set2)

set1 = {4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.issubset(set2))
print(set2.issuperset(set1))

print(type(set1))
set3 = frozenset(set1)
print(type(set3))
# set3.add(3) # Hiba, ugyanis a frozenset nem módosítható

numbers = [1, 2, 3, 4, 1, 2, 3, 4]
set1 = set(numbers)
print(set1)

# Írj egy `different_letters(letters)` függvényt, ami megszámolja, 
# hogy egy listában hány különböző betű szerepel

letters = ["a", "b", "a", "a", "b", "c"] # -> 3

def different_letters(letters):
    return len(set(letters))

print(different_letters(letters))

# Írd ki, hogy egy stringben hány különböző betű található

sentence = "Egy aprócska kalapocska, benne csacska macska mocska."
print(len(set(sentence) - {" ", ".", ","}))

print("a".isalpha())
print(".".isalpha())

for c in sentence:
    print(c)

print({c.lower() for c in sentence if c.isalpha()})
print(len({c.lower() for c in sentence if c.isalpha()}))
