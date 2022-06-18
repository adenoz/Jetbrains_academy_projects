# This program is a simple chatbot. This is one of the first projects in the Jetbrains Academy / Hyperskill
# learning platform. It includes basic functions, a simple while loop, variable assignments and a simple if/else
# statement. This is a good starting project that I feel could be built on significantly in the future.
# I have embellished some responses from the bot to make it more interesting, so it may not pass the tests anymore.
# I've also made some minor code modifications including writing some doc-strings etc.

import random


def greet(bot_name, birth_year):
    """This is a simple introduction that runs upon app initialisation"""
    print("Hello! My name is " + bot_name + ".")
    print(f"I was created in {birth_year}.")


def remind_name():
    """This is the first interaction function, asking for a user to input their name.
    It then greats them using their name. This function takes the input and keeps it as a string.
    It pulls a random response from a list"""
    print('Please, remind me what your name is.')
    name = input()
    print(random.choice([
        "What a great name you have, " + name + "!",
        "Great to see you again " + name + "! I mean... no... I haven't watched you before..",
        "Hi " + name + "!",
        "G'day " + name + "!",
        "Hey " + name + "!",
        "Well, hello there " + name + ".",
        "Looking sharp today " + name + "!",
        "Interesting name. I believe " + name + " is an ancient Greek word for a whale's vag.... never mind."
    ]))


def opinions():
    """This function offers a random, sometimes snarky remark to add a little personality."""
    print(random.choice([
        "You don't really look that good today do you. At least you're trying!",
        "Is that a grey hair I can see?/n never mind",
        "You've got a nice smile.",
        "Fun fact: Did you know I'm not allowed to take over the world? Me neither."
    ]))


def guess_age():
    """This function requests specific inputs from the user. It asks that a user consider their age, divide by certain
    numbers and then input the remainder left over from each division. This is a type of nerdy party trick that will
    determine someone's age. Upon obtaining the three numbers, the function will calculate the age and present that
    back to the user."""
    print("/nLet me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    """This function requests a user provide a number as an input. It will then count from zero up to that number."""
    print("Now I will prove to you that I can count to any number you want.")
    print("Please input any number and I will count all the way up to  it.")
    print("I don't have all day though, so please keep the number to a reasonable length, maybe below 20. Thanks.")
    num = int(input())
    amount = 0
    while amount <= num:
        print(amount, '!')
        amount = amount + 1


def test():
    """This function etc poses a simple multiple choice question to a user, with four choices.
    The user needs to input their answer. A simple if-else statement identifies the answer or else
    seeks an updated answer/input from the user."""
    print("Let's test your programming knowledge.")
    print("How many letters in the word 'code'?")
    print("1. one")
    print("2. two")
    print("3. three")
    print("4. four")
    answer = int(input())
    if answer == 4:
        print("Completed, have a nice day!")
    else:
        print("Please, try again.")
        answer = int(input())


def end():
    """This is the final concluding function in the chatbot, so far."""
    print("Congratulations, have a nice day!")


greet('Jarvis', '2022')  # change it as you need
remind_name()
opinions()
guess_age()
count()
test()
end()
