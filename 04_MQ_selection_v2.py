"""
04_MQ_selection_v2
Slightly improved version of 04_MQ_selection_v1.
The program asks again if the user types wrong number.
"""

# shows what choices are available
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

# asks the player what they want to play
select = int(input("Choose the number between 1 to 6: "))
print()

# respond for each choices
if 0 <= select <= 6:
    if select == 0:
        print("Thank you for playing the Quiz!")
        quit()
    elif select == 1:
        print()
        print("Maori quiz starts")

    elif select == 2:
        print()
        print("Maori quiz starts")

    elif select == 3:
        print()
        print("Maori quiz starts")

    elif select == 4:
        print()
        print("Show vocab list")

    elif select == 5:
        print()
        print("Show vocab list")

    else:
        print()
        print("Show vocab list")

# if the player types other int from 0 to 6, program asks again.
else:
    print("Invalid input. Please try again.")
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

    select = int(input("Choose the number between 1 to 6: "))
