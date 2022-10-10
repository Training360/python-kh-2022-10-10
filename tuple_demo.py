numbers = (1, 2, 3, 4, 5)
print(numbers[1])

# Módosíthatatlan
#numbers[1] = 66 # 'tuple' object does not support item assignment
#numbers.append(6) # 'tuple' object has no attribute 'append'

# Tuple unpacking
names = ("John Doe", "Jack Doe")
name1, name2 = names
print(name1)
print(name2)

name, year_of_birth, color = ("John Doe", 1970, "blue")
print(name)
print(year_of_birth)
print(color)

names = ("John", "Jack", "Bob", "Otto", "Bob")
i = 0
for name in names:
    print(f"{i} - {name}")
    i += 1

for i in range(len(names)):
    print(f"{i} - {names[i]}")

for i, name in enumerate(names):
    print(f"{i} - {name}")

# A John Doe nevezetű felhasználó 1970-ben született, azaz 52 éves.

name = "John Doe"
year_of_birth = 1970
year = 2022

print("A " + name + " nevezetű felhasználó " + str(year_of_birth) + "-ben született, azaz " + str(year - year_of_birth) + " éves.")

age = year - year_of_birth
print(f"A {name} nevezetű felhasználó {year_of_birth}-ben született, azaz {age} éves.")

employees = [("John Doe", 1970), ("Jane Doe", 1980), ("Jack Doe", 1990)]
for name, year_of_birth in employees:
    print(f"{name}: {year_of_birth}")

#30e m3 - 500e m3

orders = [("Vértes", 20), ("Mátra", 30), ("Gerecse", 15)]
# Írjátok ki, hogy összesen hány m3-t rendeltek!
result = 0
for name, amount in orders:
    result += amount
print(result)

# Bónusz feladat: melyik tájegységen rendeltek a legtöbbet 
# - módosított szélsőérték keresés
max_name = ""
max_amount = 0
for name, amount in orders:
    if amount > max_amount:
        max_amount = amount
        max_name = name
print(f"A legtöbbet a {max_name} területen rendelték, {max_amount} m3-t.")

