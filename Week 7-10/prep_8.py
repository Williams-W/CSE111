'''def main():
    Canada = read_file()
    Canada.pop(0)
    Canada.pop()
    Alberta_Count = 0

    for x in Canada:
        if x == "Alberta" or x == "AB":
            Alberta_Count += 1
        else:
            Alberta_Count = Alberta_Count

    print(Alberta_Count)
    
def read_file():
    Canada = []
    with open("provinces.txt", "rt") as Canada_file:
        for x in Canada_file:
            clean_line = x.strip()
            Canada.append(clean_line)
    return Canada
        

main()

        '''

students = {
    "10-450-1203": "Jorge Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Michelle Davis"
}

students["81-298-9238"] = ["Sama Patel", "Cabbage", "Cats"]

print(students)