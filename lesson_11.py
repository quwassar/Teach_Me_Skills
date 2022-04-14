start_number = 2

def list_nuber_generation(start_number):
    while start_number < 10000:
        start_number = start_number*start_number
        yield start_number
list_numbers_generate = [number for number in list_nuber_generation(start_number)]
print(list_numbers_generate)