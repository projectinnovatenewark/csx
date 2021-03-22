####################################################################################################

# 

# Let's walk through how to use functions and return values with one another. We will
# write a program that specifies what type of pizza pie a user wants with separate functions
# for each of the following. One function should ask a user what size they want and only
# accept small, medium, or large. Another function should ask about toppings, but tell the
# user they don't have pepperoni (if they ask for pepperoni). Our last function should confirm
# the order with the user.

def sizeInquiry():
    """Ask a user what size pizza they want and return it if it is a valid response"""

    sizeOfPie = input("What size pie do you want? (small, medium, or large): ")
    acceptableInputs = ["small", "medium", "large"]
    if (sizeOfPie not in acceptableInputs):
        print("Try again and enter a valid pizza size.")
        return False
    else:
        return sizeOfPie

def toppingsInquiry():
    """
    Ask a user what toppings they want- make sure to let them know we dont 
    have pepperoni if they ask!
    """

    toppings = input("What toppings would you like to have with your pizza?: (separate your toppings with commas and no spaces in between) ")
    # Lets split the user's string into separate items in a list. We want to make sure 
    # they didnt try to order pepperoni!
    listOfToppings = toppings.split(",")

    if ("pepperoni" in listOfToppings):
        followUp = input("Sorry dog, we don't have pepperoni. Do you want to change your order? (y/n) ")
        if (followUp == "y"):
            return False
        if (followUp == "n"):
            listOfToppings.remove("pepperoni")
            toppingsString = ", ".join(listOfToppings)
            return toppingsString
    else:
        return toppings

def formatOrder(s, t):
    """Create a basic formatted string to output to our user"""

    userMessage = f"Your order is for a {s} pizza with {t}"
    return userMessage

def main():
    """Guide a user through ordering a pizza"""

    # The return value of a function call can be set equal to a variable.
    size = sizeInquiry()
    if (size is False):
        # If the input value was incorrect and returned False, then we want to return 
        # a main function call to start over.
        return main()

    toppings = toppingsInquiry()
    if (toppings is False):
        # If the input value was incorrect and returned False, then we want 
        # to return a main function call to start over.
        return main()

    message = formatOrder(size, toppings)
    print(message)

main()