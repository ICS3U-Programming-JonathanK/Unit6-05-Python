#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 15, 2021
# The program uses a loop to enter each mark into a list of integers.
# When the user enters -1, the loop stops. It then calls a function that
# accepts a list of integers and returns the average of all the marks entered.

def calc_average(list_of_num):
    # calculate the average in the list
    sum = 0

    # calculate average of the list
    for number in list_of_num:
        sum += number
    try:
        average = sum / len(list_of_num)
    except ZeroDivisionError:
        # Checks to see if the list is empty
        average = -1
    return average


def main():
    # initilizations
    # Create empty list
    list_mark = []

    print("This program calculates the average of different marks.")
    print("")

    while True:
        user_mark_string = input("Enter a mark between 0 to 100. Enter"
                                 "-1 to stop: ")

        try:
            user_mark_int = int(user_mark_string)

            if (user_mark_int == -1):
                print("Thank you for your input")
                break
            elif (user_mark_int < 0 or user_mark_int > 100):
                print("{} is not between 0 to 100.". format(user_mark_int))
            else:
                # add mark to the list
                list_mark.append(user_mark_int)
        except ValueError:
            print("{} is not a valid number.". format(user_mark_string))
            print("")
        else:
            user_average = calc_average(list_mark)
            user_average = round(user_average)

            if (user_average == -1):
                print("Cannot calculate the average of an empty list")
            else:
                print("Here is the list of marks: {}". format(list_mark))
                print("The average is: {}". format(user_average))


if __name__ == "__main__":
    main()
