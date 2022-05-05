# 01_MQ_Instruction_v1
# Replace the answer to correct format that program can understand.


instruction_show = ""

while instruction_show != "X":
    instruction_show = input("Do you want to see the instruction? (yes/no): ").lower()

    # If user types yes/y, convert the user's answer to Yes
    if instruction_show == "yes" or "y":
        answer = "Yes"
        print("!!")

    # If user types no/n, convert the user's answer to no
    elif instruction_show == "no" or "n":
        answer = "No"
        print("???")

    # If user types different answer than expected, ask again.
    else:
        print("Type valid answer. (yes/no)")

    # Shows what the user have chosen.
    print(f"You have chosen {answer}")





