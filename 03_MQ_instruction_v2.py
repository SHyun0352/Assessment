"""
03_MQ_instruction_v
Shows instruction without using function. The code works with 'instruction_show'.
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


# Main routine
print("Welcome to Maori Language Quiz.")
print()
instruction_show = corrector("Do you want to see instruction?: ")
print(f"You have chosen {instruction_show}")
if instruction_show == "Yes":
    print("***How to play***")
    print()
    print("There are two types of quiz.\n"
          "type correct spelling of the question in Maori")
    print()
    print("Choose the type of quiz you want to play, and play!")
    print()

elif instruction_show == "No":
    print("Topic selection")
