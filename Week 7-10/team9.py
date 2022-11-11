import pandas as pd

def main():

    icard = pd.read_csv("https://byui-cse.github.io/cse111-course/lesson09/students.csv")

    student_list = make_dictionary(icard)

    query = make_query(student_list)

    print(query)

def make_dictionary(icard):

    student_dict = {"I-Card": [], "Name": []}
    y = 0

    for x in icard.iterrows():
        list1 = icard["I-Number"][y]
        list2 = icard["Name"][y]

        student_dict["I-Card"].append(list1)
        student_dict["Name"].append(list2)

        y += 1

    return student_dict
    
def make_query(student_list):
    i_number = int(input("I-Number: "))
    student_number = student_list["I-Card"]

    if i_number in student_number:
        index = student_number.index(i_number)
        i_number_query = student_list["Name"][index]

    else:
        i_number_query = "Student I-Number Not Found"

    return i_number_query

if __name__ == "__main__":
    main()

