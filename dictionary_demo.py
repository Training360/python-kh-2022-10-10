from random import choice, randint


employees = {"John Doe": 1970, "Jack Doe": 1980, "Jane Doe": 1990}
print(employees)
print(len(employees))

# Nincs sorrend: nem lehet elérni index alapján

print(employees["John Doe"])
employees["Bob"] = 1960
print(employees)

employees["Bob"] = 1966
print(employees)

del(employees["Bob"])
print(employees)

print(employees.keys())
print(employees.values())
print(type(employees.values()))
print(list(employees.values()).index(1980))

for k in employees.keys():
    print(k)

# Szeretném kiírni a kulcs és érték párokat egymás alá
# NEM HATÉKONY!
for k in employees.keys():
    print(f"{k} - {employees[k]}")

print(employees.items())

for k, v in employees.items():
    print(f"{k} - {v}")

another_employees = employees.copy()
print(another_employees)

print("Cathrine" in employees)

employees["Cathrine"] = 1980

if "Cathrine" in employees:
    print("Benne van")

employees["Cathrine"] += 1
print(employees)

# Hisztogram
# Csoportosítás, grouping

sentence = "Egy aprócska kalapocska, benne csacska macska mocska."
# Írjuk ki, hogy melyik betű karakter hányszor szerepel a mondatban!

histogram = {}
for c in sentence:
    c = c.lower()
    if c.isalpha():
        if c not in histogram:
            histogram[c] = 1
        else:
            histogram[c] += 1

print(histogram)

# Írd ki egy stringben leggyakrabban szereplő szót!

words = "apple banana apple raspberry banana apple"
histogram = {}
fruits = words.split()
print(fruits)
for fruit in fruits:
    if fruit not in histogram:
        histogram[fruit] = 1
    else:
        histogram[fruit] += 1
print(histogram)

# Szélsőérték keresés tétel
max_fruit = ""
max_number = 0

for k, v in histogram.items():
    if max_number < v:
        max_number = v
        max_fruit = k

print(max_fruit)

#for i in histogram:
#    print(i)

john = {"name": "John Doe", "year_of_birth": 1970, "favourite_color": "green", "salary": 200}
print(john)
print(john['favourite_color'])
john['skills'] = ['Python', 'Java', 'Bash', 'JavaScript']

print(john)
john["address"] = {"city": "Budapest", "zip": 1115}
print(john)

# Írj egy `generate_test_data()` függvényt, ami visszaad employee listát, 100 db elemmel!
# Egy employee az egy dictionary. Következőképp generálni az adatokat:
# Név: legyen két lista, vezeték és keresztnevekkel, ebből véletlenszerűen válasszon
# Fizetés: random szám 100 és 500 között!

numbers = [1, 3, 5, 7, 9]
# randint
print(choice(numbers))




fornames = ["Doe", "Smith"]
firstnames = ["John", "Jack", "Jane"]
employees = []
for i in range(0, 100):
    forname = choice(fornames)
    firstname = choice(firstnames)
    name = firstname + " " + forname
    salary = randint(100, 500)
    employee = {"name": name, "salary": salary}
    employees.append(employee)

print(employees)
print(employees[50]["name"])
print(employees[50]["salary"])