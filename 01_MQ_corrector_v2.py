# 01_MQ_corrector_v2
# Replace the answer to correct format that program can understand but in different way.

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


# Main routine
show_instruction = corrector("Have you played this game before?: ")
print(f"You chose {show_instruction}")
print()

