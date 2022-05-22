# 01_MQ_Instruction_v1
# Replace the answer to correct format that program can understand.


instruction_show = ""

while instruction_show != "x":
    instruction_show = input("Do you want to see the instruction? (yes/no): ").lower()

    # If user types yes/y, convert the user's answer to Yes
    if instruction_show == "yes" or instruction_show == "y":
        answer = "Yes"
        print("Process to the game")

    # If user types no/n, convert the user's answer to no
    elif instruction_show == "no" or instruction_show == "n":
        answer = "Yes"
        print("Process to the game")

    # If user types different answer than expected, ask again.
    else:
        print("Type valid answer. (yes/no)")

    # Shows what the user have chosen.
    print(f"You have chosen {instruction_show}")





