import random

# main Routine goes here
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen += "unicorn"
        balance += 4
    elif 6 <= chosen_num <=36:
        chosen = "donkey"
    else:
        if chosen_num % 2 == 0:
            chosen = "hours"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("you got a {}. your balance is ""$ {:.2f}".format(chosen, balance))

print()
