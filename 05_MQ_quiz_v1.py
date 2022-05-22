"""
05_MQ_quiz_v1
creating a code that gives the player randomly chosen questions from the list.
"""

import random


# corrector function that converts certain answers to "Yes" or "No"
def corrector(question_text):
    while True:

        # Ask player if they want to see instruction
        answer = input(question_text).lower()

        # if player types "yes" or "y", converts to "Yes"
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if player types "no" or "n", Converts to "No"
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # if player types anything  else, ask again
        else:
            print("Invalid answer. Please type 'yes' or 'no'. ")


# selection function
def selection(question, low, high):
    # error message that shows when the player types invalid answer.
    error = "Invalid input.\n" \
            "Please enter a number between 0 to 6."

    # this while loop makes the code keep running even the player types invalid answer.
    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response

            else:
                print(error)

        # if player types anything else from the number provided, it asks again.
        except ValueError:
            print(error)


# quiz function
def quiz():
    # resets number of correct and wrong every time you play the quiz.
    correct = 0
    wrong = 0

    # lists of english/maori words
    number = [["one", "tahi"], ["two", "rua"], ["three", "toru"], ["four", "wha"], ["five", "rima"], ["six", "ono"],
              ["seven", "whitu"], ["eight", "waru"], ["nine", "iwa"], ["ten", "tekau"]]

    days = [["monday", "rahina"], ["tuesday", "ratu"], ["wednesday", "raapa"], ["thursday", "rapare"],
            ["friday", "ramere"], ["saturday", "rahoroi"], ["sunday", "ratapu"]]

    months = [["january", "kohitatea"], ["february", "hui-tanguru"], ["march", "poutu-te-rangi"],
              ["april", "paenga-whawha"], ["may", "haratua"], ["june", "pipiri"], ["july", "hongongoi"],
              ["august", "here-turi-koka"], ["september", "mahuru"], ["october", "whiringa-a-nuku"],
              ["november", "whiringa-a-rangi"],
              ["december", "hakihea"]]

    # if player chooses a number between 1 and 3, play quiz.
    if 1 <= select <= 3:
        if select == 1:
            print("You've selected number quiz!")
            print()
            choice = number
        elif select == 2:
            print("You've selected days!")
            print()
            choice = days
        else:
            print("You've selected months quiz!")
            print()
            choice = months

        # shuffles the order of the list
        random.shuffle(choice)

        print("**************************************************")
        print("***********get right as much as you can!**********")
        print("**************************************************")
        print("\n"
              "\n")

        # playing quiz
        for i in choice:
            answer = input("What is this number in Maori? '{}': ".format(i[0]))
            # if player types correct answer, correct goes up by 1
            if answer == i[1]:
                print("correct.")
                correct += 1
            # if player types wrong answer, wrong goes up by 1
            else:
                print("wrong.")
                wrong += 1
        # shows summary of finished quiz
        print("*********************************")
        print(f"Correct: {correct},Wrong: {wrong}, quiz ended!")
        print("*********************************")

    # if player types a number between 4 and 6, shows vocabulary lists.
    if 4 <= select <= 6:
        if select == 4:
            print()
            print(number)
        elif select == 5:
            print(days)
        else:
            print(months)


# Main routine
again = ""

print("Welcome to Maori quiz.")
print()

play = "Yes"

while play == "Yes":

    if again == "":
        select = selection("1) [Quiz] Number 1 to 10 in Maori\n"
                           "2) [Quiz] Days of the week in Maori\n"
                           "3) [Quiz] Months of the year in Maori\n"
                           "                                   \n"
                           "***************************************\n"
                           "                                   \n"
                           "4) [Vocabulary] Number 1 to 10 in Maori\n"
                           "5) [Vocabulary] Days of the week in Maori\n"
                           "6) [Vocabulary] Months of the year in Maori\n"
                           "\n"
                           "0) Quit\n"
                           "Choose the number between 0 to 6: ", 0, 6)
        print()
        quiz()

    else:
        print()
        print("Summary showing up")
        break

    print()
    again = input("Press [Enter] to play again, type Any key to quit: ")

print()
print("While loop end test")
