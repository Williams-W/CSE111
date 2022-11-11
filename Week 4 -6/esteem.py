def main():

    print("This program is an implementation of the Rosenberg \n \
Self-Esteem Scale. This program will show you ten \n \
statements that you could possibly apply to yourself.\n \
Please rate how much you agree with each of the\n \
statements by responding with one of these four letters:\n \
\n \
D means you strongly disagree with the statement.\n \
d means you disagree with the statement.\n \
a means you agree with the statement.\n \
A means you strongly agree with the statement.")

    score = questions()

    print(f"Your score is {score}\n \
        A score below 15 may indicate problematic low self-esteem.")



def questions():
    list = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.","I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.","I take a positive attitude toward myself.","On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.","I certainly feel useless at times.", "At times I think I am no good at all."]

    result = 0
    y = 0

    for x in list:

        print()
        print(x)
        answer = input("Enter D, d, a, or A: ")
        y += 1

        if y == 1 or y == 2 or y == 4 or y == 6 or y == 7:
            if answer == "D":
                result += 0
            elif answer == "d":
                result += 1
            elif answer == "a":
                result += 2              
            else:
                result += 3
                
        else:
            if answer == "D":
                result += 3              
            elif answer == "d":
                result += 2              
            elif answer == "a":
                result += 1              
            else:
                result += 0
                
        print(result)    
    return result

main()