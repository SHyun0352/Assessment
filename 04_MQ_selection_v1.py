"""
04_MQ_selection_v1
Let user choose what they want to view or play.
"""

# Asks to choose what data they want to view or play
select = int(input("Choose the number between 1 to 6.\n"
                   "                                   \n"
                   "1) [Quiz] Number 1 to 10 in Maori\n"
                   "2) [Quiz] Days of the week in Maori\n"
                   "3) [Quiz] Months of the year in Maori\n"
                   "                                   \n"
                   "***************************************\n"
                   "                                   \n"  
                   "4) [Vocabulary] Number 1 to 10 in Maori\n"
                   "5) [Vocabulary] Days of the week in Maori\n"
                   "6) [Vocabulary] Months of the year in Maori"))

# If the user select certain number, goes on.
if select == 1:
    print("Maori quiz starts")

elif select == 2:
    print("Maori quiz starts")

elif select == 3:
    print("Maori quiz starts")

elif select == 4:
    print("Show vocab list")

elif select == 5:
    print("Show vocab list")

else:
    print("Show vocab list")

