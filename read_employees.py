import email


count = 0
employees = []
with open("MOCK_DATA.csv") as f:
    for line in f:
        employee = line.strip().split(",") # Fluent
        id, first_name, last_name, email, gender, ip_address = employee
        print(first_name)
        employees.append(employee)
        if "Female" in line:
            count += 1
        # print(line.strip())

print(count)
print(employees)
