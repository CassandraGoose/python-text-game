from sys import exit

def start():
    print("It's Monday today. You aren't thrilled to go to work today...")
    print("\nDo you want to stop for coffe before work? (Yes or No)")

    to_do_next = input("> ")

    if to_do_next == "Yes":
        get_a_latte()
    elif to_do_next == "No":
        go_to_work()
    else:
        game_over("You didn't go to work or get a coffee and you got fired.")

def get_a_latte():
    print("Something seems off as you drive to Dunkin Doughnuts.")
    print("\n You saw a man walking down the street but he just disappeared in a flash of blue light.")
    print("\n You shrug if off for now and you order your latte.")
    print("\n The barista hands you your latte but their words are all jumbled when they speak to you")
    print("\n Do you just drive to work or do you ask them if they are having a stroke? (Work or Ask)")

    to_do_next = input("> ")

    if to_do_next == "Work":
        go_to_work()
    elif to_do_next == "Ask":
        ask_question()
    else:
        game_over("Error. Error. Error.")

def ask_question():
    print("They start yelling at you.")
    print("Do you start a fight or go to work? (Fight or Work)")

    to_do_next = input("> ")

    if to_do_next == "Fight":
        game_over("The barista ate you.")
    elif to_do_next == "Work":
        go_to_work()
    else:
        game_over("dedd")

def go_to_work():
    print("When you walk into work, your coworker looks concerned.")
    print("\n Do you ask him why? (Yes or No)")

    to_do_next = input("> ")

    if to_do_next == "Yes":
        ask_coworker()
    elif to_do_next == "No":
        game_over("He murdered you.")
    else:
        game_over("dedd")
        
def ask_coworker():
    print("He tells you aliens are taking over today and proceeds to dance away.")
    exit(0)

def game_over(why):
    print(f"\n{why}. Game over.")
    exit(0)

start()
