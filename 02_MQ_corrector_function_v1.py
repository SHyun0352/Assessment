"""
02_MQ_corrector_function_v1
converts the user's answer (such as yes,no) to proper answer.
01_MQ_corrector_v1.py is converted into function.
changed question part(instruction_show) to answer to simplify the code.
"""


# Function
def corrector(question_text):
    while True:

        # Ask player if they want to see instruction
        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Invalid answer. Please type 'yes' or 'no'. ")


# Main routine
print("Welcome to Maori Language Quiz.")
print()
instruction_show = corrector("Do you want to see instruction?: ")
print(f"You have chosen {instruction_show}")
print()






