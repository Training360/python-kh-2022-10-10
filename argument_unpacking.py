def print_employee(name, year_of_birth):
    print("Name: " + name)
    print("Year of birth: " + str(year_of_birth))


print_employee("John Doe", 1980)

employee = ("John Doe", 1980)

print_employee(*employee)

print_employee(employee[0], employee[1])

def sum_numbers(numbers):
    print(type(numbers))


sum_numbers((1, 2, 3, 4))

employee = {"year_of_birth": 1980, "name": "John Doe"}
print_employee(**employee)

