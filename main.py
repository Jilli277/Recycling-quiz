#Shivani Rana and Jill Pa'u
#3/11/20
#Recycling Game
import time

easy = ["What is the number 1 sythetic solid that is a big contributor to pollution?","__1__",
    "\nReduce, reuse,","__2__",
    "\nCan you recycle aluminuim foil?","__3__",
   "\nWhat is another name for waste water?", "", "__4__","\n"]
easy_answers = ["Plastic","Recycle","Yes","Sewage"]
medium = [
    "Does one wrong item in a recycling bin mean the whole bag will be sent to landfill?", "__1__",
    "\nDoes recycling really save energy? ",
    "", "__2__",
    "\nHow much energy (in percentage) can you save by recycling paper?",
    "__3__", "\nDoes plastic fully break down and eventually disintergrate?",
    "__4__", "\n"
]
medium_answers = ["YES", "yes", "60%", "No"]
hard = [
    "How many people said that they have at least 5 non-reusable drinks in their dorm? [51%,61%, 71%, 91%]" ,
    "\nOut of the drinks people keep in their room 71% are plastic, [True/False]",
    "\nThe average person generates over _____ of trash every day. [3Kg, 4Kg, 1Kg, 2Kg]",
     "\nPlastic takes _____ years to decompose [350,250,9000,1000]",
    "\n"
]
hard_answers = ["61%", "True", "2Kg", "1000"]

print("\    /\    /  __  |  __  _   _ _   __    ")
print(" \  /  \  /  /__\ | /   / \ | | | /__\   ")
print("  \/    \/   \__  | \__ \_/ |   | \__    ")
print("       _____    _____                    ")
print("         |  _     |  |    __             ")
print("         | / \    |  |_  /__\            ")
print("         | \_/    |  | | \__             ")
print(" | __                                    ")
print(" |/  |                  |                ")
print(" |___|  __   __      __ |     __   __    ")
print(" |  \  /__\ /   |  |/   | | |/  \ /  \|  ")
print(" |   \ \___ \__ \__/\__ | | |   | \__/|  ")
print("                   |                  |  ")
print("           ___ \__/               \__/   ")
print("          /   \  __     _  _   __        ")
print("          |  __ /  \| |/ \/ \ /__\       ")
print("          \___/ \__/| |     | \__        ")
print("      Please select a difficulty         ")
print("        Easy, Medium, or Hard            ")
print("                                         ")
players_choice = input(" Please type in your selection: ")


def dif_selection(players_choice):
    """ Takes the players difficulty selection and then loads the proper conditions for the gameself.
    input; 
    players_choice: STR input from user selecting a difficulty level
    output:
    questions: the questions corresponding to the players difficulty choice.
    answers: the answers to the questions.
    """
    if players_choice.lower() == "easy":
        questions, answers = easy, easy_answers
        print(" Easy mode selected")
        time.sleep(1.1)
        return (questions, answers)
    elif players_choice.lower() == "medium":
        questions, answers = medium, medium_answers
        print("     Medium mode selected")
        time.sleep(.05)
        return (questions, answers)
    elif players_choice.lower() == "hard":
        questions, answers = hard, hard_answers
        print("     Hard mode selected")
        time.sleep(.05)
        return (questions, answers)
    else:
        print(
            " \n     Selection not recognized, easy difficulty selected by default\n\n\n"
        )
        questions, answers = easy, easy_answers
        return (questions, answers)


questions, answers = dif_selection(players_choice)
spaces_5 = """ """
print(spaces_5)


def attempt_check(ques_num, questions, answers):
    """
    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect.
    input:
    ques_num: INT The current blank number.
    questions: STR The questions to be answered
    answers: list of STR The answers for the questions.
    output:
    ques_num: the current question number
    """
    space = " "
    print(space.join(questions))
    blank = "__" + str(ques_num) + "__"
    guess = str(
        input("What word should replace? " + "__" + str(ques_num) + "__"))
    score = 0
    answer = answers[ques_num - 1]
    if guess.lower() == answer.lower():
        questions[questions.index(blank)] = answer
        score += 1
        print("\n\nCORRECT!\n")
        print("Score:", score)
        ques_num += 1
        return ques_num
    else:
        print("Incorrect. Please try again.\n")
        return attempt_check(ques_num, questions, answers)


def play_game(questions, answers, spaces_5):
    """
    This takes in the parameters of the game and runs the game under the set conditions.
    input:
    questions: the questions that pertain to the difficulty level selected
    answers: a list of answers to the given questions
    spaces_5: a variable containing a string meant for visual formating of appearance
    """
    space = " "
    ques_num = 1
    print("     Welcome to the Recycling game, a pollution/global warming awareness themed trivia game!\n\n\n")
    for answer in answers:
        ques_num = attempt_check(ques_num, questions, answers)
        print(spaces_5)
        time.sleep(1.5)
    print(space.join(questions))
    print("Congratulations you have WON!!!!!!!!!!!!!!!!!!!!")


play_game(
    questions,
    answers,
    spaces_5,
)
