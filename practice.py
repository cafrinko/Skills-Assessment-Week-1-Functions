"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    return "Hello World"
# print hello_world()

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    return "Hi {}".format(name)
# print say_hi("Raquel")

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(integer1, integer2):
    return integer1 * integer2
# print print_product(8, 9)

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(string, integer):
    return (string)*integer
# print repeat_string("Charlie Horse", 20)

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(integer):
    # integer = int(number)
    # try:
    if type(integer) == int:
        if integer > 0:
            return "Higher than 0"
        elif integer < 0:
            return "Lower than 0"
        else:
            return "Zero"
    else:
        return "Please enter a number and only a number"
# print print_sign("turnup")

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(integer):
    if integer % 3 == 0:
        return True
    else:
        return False
# print is_divisible_by_three(33)

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence):
    return sentence.count(" ")
# print num_spaces("Celestial bodies of cosmosic proportions")

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip_percentage=0.15):
    return meal_price*tip_percentage + meal_price
# print total_meal_price(43)

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def sign_and_parity(integer):
    a_list = []
    if integer % 2 == 0:
        a_list.append("Even")
    if integer % 2 != 0:
        a_list.append("Odd")
    if integer >= 0:
        a_list.append("Positive")
    if integer < 0:
        a_list.append("Negative")
    return a_list

another_list = sign_and_parity(18)
# print another_list
sign, parity = another_list
print "%s and %s" % (sign, parity)
################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def profesh_id(name, job_title="Engineer"):
    return "%s, %s" % (name, job_title)
print profesh_id("Matthias Squillwater", "Lead Architect")

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#
#    Use the function from #1 to construct the full title for the letter's
#       Sincerely, SENDER_NAME.
#    greeting.

# def full_title(sender_name):
#     return "Dear" + profesh_id(job_title="Engineer", name) + ", I think you are amazing! Sincerely, {}.".format(sender_name.upper())
# print full_title(profesh_id("Kumar", "Gloria Steinum")
# ********* so confused about how to use decorators and nested functions, still :-\

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
