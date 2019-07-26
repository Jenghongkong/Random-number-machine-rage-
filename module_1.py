import random

def lottery():
    return_number = input("How many you want to returns: ")
    range_1 = input("Type in the range 1: ")
    range_2 = input("Type in the range 2: ")
    return_number = int(return_number)
    range_1 = int(range_1)
    range_2 = int(range_2)

    for i in range(return_number):
        yield random.randint(range_1,range_2)
        
for random_number in lottery():
       print("The number is... %d!" %(random_number))
    
        
