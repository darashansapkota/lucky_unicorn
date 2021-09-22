import random

# functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")

def number_check(question,low,high):
    error = "Please enter an whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low <= response <= high:
                return response
            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


    sides = decoration * 3

    statement = "{} {} {}".format(sides, greeting, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""

# Main routine goes here...
welcome = statement_generator("Welcome to the lucky Unicorn Game", "*")

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print("Display instructions")
    print("You have to chosen number,1 to 10")

how_much = number_check("How much would you like to play with?",1,10)
balance = how_much
print("You have chosen to spend ${:.2f}" .format(balance))

play_again = input("To play press <enter> ...")
while play_again == "":
    chosen_num = random.randint(1, 100)
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "U"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 10 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num > 2 == 0:
            chosen ="horse"
            decoration = "H"
        # othervise set it to a zebra
        else:
            if chosen_num >= 4:
             chosen = "zebra"
            decoration = "Z"
        balance -= 0.5

    outcome = statement_generator("You got a {}. Your balance is " "${:.2f}".format(chosen, balance), decoration)

    if balance < 1:
            play_again ="xxx"
            print("Sorry you have run out of money")
    else:
        play_again = input("Press <enter> to play again or xxx to quit")



