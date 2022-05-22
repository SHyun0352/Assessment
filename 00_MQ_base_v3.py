"""
00_MQ_base_v1
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


# Instruction function
def instruction():
    print("***How to play***")
    print()
    print("--Maori spelling Quiz--\n"
          "In the selection menu, You can open Vocabulary, or Quiz.\n"
          "You can learn how to spell maori words in the Vocabulary.\n"
          "Then ")
    print()
    print("Choose the type of quiz you want to play, and play!")
    print()


# selection function
def selection(question, low, high):
    # error message that shows when the player types invalid answer.
    error = "\n" \
            "Invalid input.\n" \
            "Please enter a number between 0 to 6.\n" \
            "\n"

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

        print(formatter("*", "Get spelling correct as many as you can!"))
        print()

        # playing quiz
        for i in choice:
            answer = input("What is this number in Maori? '{}': ".format(i[0]))
            # if player types correct answer, correct goes up by 1
            if answer == i[1]:
                print()
                print(formatter("!", "correct"))
                correct += 1
                print()
            # if player types wrong answer, wrong goes up by 1
            else:
                print()
                print(formatter("?", "wrong"))
                wrong += 1
                print()
        # shows summary of finished quiz
        print(formatter("*", f"Correct: {correct},Wrong: {wrong}, quiz ended!"))

    # if player types a number between 4 and 6, shows vocabulary lists.
    if 4 <= select <= 6:
        if select == 4:
            print()
            print(number)
        elif select == 5:
            print(days)
        else:
            print(months)


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
again = ""

print("Welcome to Maori Language Quiz.")
print()

# asks whether the player wants to see the instruction.
instruction_show = corrector("Do you want to see instruction?: ")
print(f"You have chosen {instruction_show}")
print()

# after showing instruction, ask again to the player whether they want to play the quiz
if instruction_show == "Yes":
    instruction()
    play = corrector("Do you want to play quiz now? (type 'no' to quit): ")

# if the player types no, automatically saying 'yes' to play the quiz.
else:
    play = "Yes"

# this while loop makes the code run over and over again until player says they do not want to play the game.
while play == "Yes":
    # if the player did not type anything when the program asked to play again.
    if again == "":
        select = selection("Choose the number you want to play.\n"
                           "\n"
                           "1) Plays quiz about 'Number 1 to 10' in Maori\n"
                           "2) Plays quiz about 'Days of the week' in Maori\n"
                           "3) Plays quiz about 'Months of the year' in Maori\n"
                           "\n"
                           "********************************************\n"
                           "\n"
                           "4) Shows vocabulary of 'Number 1 to 10' in Maori\n"
                           "5) Shows vocabulary of 'Days of the week' in Maori\n"
                           "6) Shows vocabulary of 'Months of the year' in Maori\n"
                           "\n"
                           "0) Close the program.\n"
                           "\n"
                           "Choose the number between 1 to 6: ", 0, 6)
        print()
        quiz()
        print()

        # if player selects 0, go to main routine and quit.
        if select == 0:
            break

    # if the player types any key, the while loop ends.
    else:
        break

    # ask the player whether they want to play again or not.
    again = input("Do you want to go back to the menu? Press [Enter] to go menu, type any key to quit.")

# end of main routine
print("Thank you for playing our Maori quiz!")
