from json import dumps
from pprint import pprint


numbers = {n:n**2 for n in range(1, 10) if n % 2 == 0}
print(numbers)

pprint(numbers,depth=1,indent=1)

calls = [
("1111","2222","10:10","start"),
("1112","2223","10:15","start"),
("1113","2224","10:20","start"),
("1111","2222","10:25","end"),
("1113","2224","10:30","end"),
("1112","2223","10:35","end")]

pprint(calls,depth=2,indent=4)

print(dumps(numbers, indent=4))

print(dumps(calls, indent=4))