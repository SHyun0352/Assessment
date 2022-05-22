"""
04_MQ_selection_v4
made selection function in other way which functioning much better
"""


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

        except ValueError:
            print(error)


# Main routine
print("Welcome to Maori quiz.")
print()
# usage of selection function
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

print(f"You've selected number {select}")
