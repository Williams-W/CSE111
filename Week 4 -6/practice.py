from numpy import append
import random

def main():

    numbers = [5, 10 , 15]
    print(numbers)

    append_random_number(numbers)
    print(numbers)

    append_random_number(numbers, 3)
    print(numbers)

def append_random_number(numbers, quantity = 1):
 
    for z in range(quantity):
        x = round(random.uniform(1,5),2) 
        numbers.append(x)

if __name__ == "__main__":
    main()

