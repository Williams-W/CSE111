def main():
    make_list()

def make_list():
    total_rectangles = float(input("How many rectangles?: "))
    rotations = 0
    area = []

    while total_rectangles > 0:

        total_rectangles -= 1
        rotations += 1

        print(f"Rectangle # {rotations}")

        rectangle_x_length = float(input("Length: "))
        rectangle_x_height = float(input("Height: "))

        area.append(float(rectangle_x_height * rectangle_x_length))
    
    print(f'Your total area is: {sum(area)}')
    



        
