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

# Main routine goes here...

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print("Display instructions")

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
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen ="horse"
        # othervise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is " "${:.2f}".format(chosen, balance))

    if balance > 1:
            play_again ="xxx"
            print("Sorry you have run out of money")
    else:
        play_again = input("Press <enter> to play again or xxx to quit")



