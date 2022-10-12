input_data = "123"
try:
    number = int(input_data)
    print("end of try")
except ValueError:
    print("Ez nem szám")
print("end")