"2y, 1m" # két év és egy hónap
"3y, 4m" # három év és négy hónap
"12y, 11m"

# Írj egy olyan függvényt, ami visszaadja, hogy a paraméterként
# megadott intervallum nagyobb-e, mint két év?

from calendar import month
import re


s = "2y, 1m"
parts = s.split(",")
print(parts)
year = parts[0]
month = parts[1]
print(year)
print(month)
year = year.strip()
month = month.strip()
print(year)
print(month)
year = year[:-1]
month = month[:-1]
print(year)
print(month)
year = int(year)
month = int(month)
print(year)
print(month)

greater = (year == 2 and month >= 1) or (year > 2)


s = "2y, 1m"
year, month = [int(i.strip()[:-1]) for i in s.split(",")]
greater = (year == 2 and month >= 1) or (year > 2)

year, month = re.search("(\d+)y,\s(\d+)m", s).groups()
print(year)
print(month)