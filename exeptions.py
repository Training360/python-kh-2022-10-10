def get_number_data():
    input_data = "abcd"
    number = int(input_data)
    return number

def get_data():
    get_number_data()    
    print("end of get_data")

try:
    get_data()
except ValueError:
    print("Nem szám")
print("end")


