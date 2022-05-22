"""
04_MQ_selection_v2
Slightly improved version of 04_MQ_selection_v1.
The program asks again if the user types wrong number.
"""


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

        # if player answers with invalid int, ask again.
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


# Temporary Main routine to test the code
print("Welcome to Maori Language Quiz.")
chosen = selection()
print(f"You've chose {chosen}")
