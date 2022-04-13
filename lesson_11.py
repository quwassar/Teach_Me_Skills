start_number = 2

def get_generator(start_number):
    while start_number < 10000:
        start_number = start_number*start_number
        yield start_number
        print(start_number)
list_numbers_generation = [number for number in get_generator(start_number)]
print(list_numbers_generation)