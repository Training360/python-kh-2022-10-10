numbers = [2, 6, 8, 12, 6]
print(numbers)

empty = []
print(empty)

for number in numbers:
    print(number)

print(numbers[3])
# print(numbers[15]) # Érvénytelen indexre hivatkozás

numbers[1] = 3
print(numbers)

# Szeletelés, slicing
print(numbers[1:4]) # Balról zár, jobbról nyílt, hiszen a 
# 4-es indexű elem, már nincs benne

print(numbers[3:])
print(numbers[:3])
print(numbers[1:4:2])
print(numbers[::-1])

print(numbers)
numbers[1:3] = [66, 77]
print(numbers)

print(len(numbers)) # built in function

another_numbers = [2, 66, 77, 12, 6]
print(numbers == another_numbers)

# Nem javasolt használni
# Egymásba ágyazhatóság
employee = ["John Doe", 1970, ["blue", "yellow"]]
print(employee[0])
print(employee[2])

print(employee[2][1])

print([1, 2, 3] + [3, 4, 5])
#print([1, 2, 3] + 4) # can only concatenate list (not "int") to list
print([1, 2, 3] + [4])

print([1, 2] * 3)

print(12 in numbers)
print([8, 12] in numbers)

numbers.append(4) 
# elképzelni: append(numbers, 4)
# objektum függvénye, azaz más néven ez egy metódus
print(numbers)
print(type(numbers))
print(type(3))

del(numbers[3])
print(numbers)

# lista módosítható: elem módosítható, elem hozzáadható, elem törölhető

names = ["John Doe", "Jane Doe", "Jack Doe"]
names.reverse() # ez módosítja a listát
print(names)

names = ["John Doe", "Jane Doe", "Jack Doe"]
print(names[::-1]) # ez nem módosítja a listát
names = names[::-1]
print(names)

names = ["John Doe", "Jane Doe", "Jack Doe"]
print(names.index("Jane Doe"))

names.sort()
print(names)

names = ["Cecil", "Béla", "Ábel", "Aladár"]
names.sort()
print(names)

names = ["John Doe", "Jane Doe", "Jack Doe"]
names.insert(1, "Bob")
print(names)

names = ["John Doe", "Jane Doe", "Jack Doe", "Jack Doe"]

print(names.count("Jack Doe"))

names.remove("Jack Doe")
print(names)

# Keresd ki a legkisebb számot! (Használd a min beépített függvényt)

print(type(5) is int)
print(type("abc") is int)
print(isinstance(5, int))
print(isinstance("abc", int))

numbers = [1, 2, 3, 4, 5]
print(min(numbers))
print(max(numbers))
print(sum(numbers))