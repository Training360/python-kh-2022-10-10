# Adjuk össze az első egymillió számot
# sum() függvényt

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

def multiply_two(limit):
    num = 1
    while num < limit:
        yield num
        num *= 2


def fibonacci(limit):
    yield 1
    yield 1
    first = 1
    second = 1
    while first < limit:
        result = first + second
        yield result
        first = second
        second = result

numbers = []
i = 0
while i < 1_000_000:
    numbers.append(i)
    i += 1

# print(numbers)

print(sum(numbers))

print(firstn(10))

print(range(10))

print(sum(firstn(10)))

print([i for i in firstn(10)])

for j in range(10):
    print(j)

print([i for i in multiply_two(100)])

print([i for i in fibonacci(100)])

def get_number(n):
    return n * 2
    print("Hello World")


print(get_number(4))