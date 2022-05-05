"""
03_MQ_instruction_v1
Coded a function which shows instruction works with corrector function and instruction_show.
"""


# Corrector function
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


# Main routine
print("Welcome to Maori Language Quiz.")
print()
instruction_show = corrector("Do you want to see instruction?: ")
print(f"You have chosen {instruction_show}")
if instruction_show == "Yes":
    instruction()
elif instruction_show == "No":
    print("Topic selection")

