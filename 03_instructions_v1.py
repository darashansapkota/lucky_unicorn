

# functions go here...
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


# Main routine goes here...
show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))

if show_instructions == "yes" :
    print("Display instructions")
else:
    print("Programs Continues")
