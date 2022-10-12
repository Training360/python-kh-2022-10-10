from json import dumps


temperatures = [
    ["Budapest", "2022-10-12", 12, 22],
    ["Debrecen", "2022-10-12", 10, 22],
    ["Pécs", "2022-10-12", 11, 25],
    ["Győr", "2022-10-12", 8, 16],
]

def apply(data, calculate):
    for row in data:
        row.append(calculate(row))


apply(temperatures, lambda row: row[3] - row[2])
apply(temperatures, lambda row: row[3] * 2)

print(temperatures)
#print(dumps(temperatures, indent=4))