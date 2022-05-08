"""
00_MQ_base_v1
"""


# Corrector function
def corrector(question_text):
    while True:

        # Ask player if they want to see instruction
        answer = input(question_text).lower()

        # Converts 'yes' or 'y' to 'Yes'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # Converts 'no' or 'n' to 'No'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If the player types different answer than expected answer, asks to type again.
        else:
            print("Invalid answer. Please type 'yes' or 'no'. ")


# Instruction function
def instruction():
    print("***How to play***")
    print()
    print("There are two types of quiz.\n"
          "First choice is choosing number between 1 to 4 in the list\n"
          "Second choice is type the answer to the question.\n")
    print()
    print("Choose the type of quiz you want to play, and play!")
    print()


# Selection function which allows the player choose what they want to open.
def selection():

    response = ""

    # Lists of quizzes/vocabulary
    print()
    print("1) [Quiz] Number 1 to 10 in Maori\n"
          "2) [Quiz] Days of the week in Maori\n"
          "3) [Quiz] Months of the year in Maori\n"
          "                                   \n"
          "***************************************\n"
          "                                   \n"
          "4) [Vocabulary] Number 1 to 10 in Maori\n"
          "5) [Vocabulary] Days of the week in Maori\n"
          "6) [Vocabulary] Months of the year in Maori\n"
          "\n"
          "0) Quit")

    print()

    # Asks whether the player wants to see/play quiz or vocabulary.
    select = int(input("Choose the number between 1 to 6: "))

    print()

    # Used while  loop that continues to ask if the player typed different than it shown.
    while response == "":

        if 0 <= select <= 6:
            if select == 0:
                print("Thank you for playing the Quiz!")
                quit()

            elif select == 1:
                response = "number"
                return response

            elif select == 2:
                response = "days"
                return response

            elif select == 3:
                response = "months"
                return response

            elif select == 4:
                response = "vocabnum"
                return response

            elif select == 5:
                response = "vocabdays"
                return response

            else:
                response = "vocabmonths"
                return response

        else:
            print("Invalid answer. Please answer between 1 to 6."
                  "1) [Quiz] Number 1 to 10 in Maori\n"
                  "2) [Quiz] Days of the week in Maori\n"
                  "3) [Quiz] Months of the year in Maori\n"
                  "                                   \n"
                  "***************************************\n"
                  "                                   \n"
                  "4) [Vocabulary] Number 1 to 10 in Maori\n"
                  "5) [Vocabulary] Days of the week in Maori\n"
                  "6) [Vocabulary] Months of the year in Maori\n"
                  "\n"
                  "0) Quit")

            print()

            select = int(input("Choose the number between 1 to 6: "))


# Main routine
print("Welcome to Maori Language Quiz.")
print()
instruction_show = corrector("Do you want to see instruction?: ")
print(f"You have chosen {instruction_show}")
if instruction_show == "Yes":
    instruction()
    play = corrector("Do you want to play quiz now? (type 'no' to quit): ")

else:
    play = "Yes"

if play == "Yes":
    selection()
