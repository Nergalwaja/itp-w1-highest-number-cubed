"""This is the entry point of the program."""


def highest_number_cubed(limit):
    number = 0
    while True :
        number += 1
        if number ** 3 > limit:
            return number - 1
highest_number_cubed(30)
highest_number_cubed(12)
highest_number_cubed(3)
highest_number_cubed(12000)

#1 ** 3 = 1
#2 ** 3 = 8
#3 ** 3 = 27
#4 ** 3 = 64