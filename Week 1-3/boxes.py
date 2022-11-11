import math

number_of_items = int(input("Enter the number of items: "))
number_in_box =  int(input("Enter the number of items per box: "))

print(f'For {number_of_items} items, packing {number_in_box} items in each box, you will need',
 math.ceil(number_of_items/number_in_box),'boxes.')
