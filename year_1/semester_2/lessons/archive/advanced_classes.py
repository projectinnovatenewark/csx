# ########################################################################################

class Classmate:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age


    # this is a function
    def format_class(self):
        # here we will create a list of items to print within the class definition
        # and then join them to create one string. The dashes are just for readability.
        s = ["----------",
             # the f before each string allows for f-string literals
             # these allow for the format() function to be used, and for
             # curly braces to be used for replacement fields. link for reference:
             # https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
             f"First Name : {self.first_name}",
             f"Last Name : {self.last_name}",
             f"City : {self.city}",
             f"Age : {self.age}"]
        return print("\n".join(s))

def complete_form(n_users):
    """The function will ask questions with the helper function of ask_user() and create Classmates.
    This function will return a list with the number of classmates you passed to this function."""
    # here we used a list comprehension to create classes for the amount n_users
    # and add them to the list
    value = [Classmate(ask_user("Enter First Name: ").title(),
                       ask_user("Enter Last Name: ").title(),
                       ask_user("Enter City: ").title(),
                       # this type=int specifies that the age input will
                       # only work if it is passed a number
                       ask_user("Enter Age: ", type=int)
                      )
             for question in range(n_users)
            ]
    # this will print the 3 Classmate objects that we arranged in our list comprehension above
    print(value)
    return value
​
def ask_user(message='', type=str):
    """this is a helper function for getting the class of Classmate's inputs"""
    user_input = ''
    while not user_input:
        try:
            # we added a call to str.strip, so user names like (spaces) and (tabs) are not allowed.
            # if spaces are entered, a ValueError will be thrown and the question will be repeated.
            # since the default type is str (for string), it will convert the input to a string. But
            # when we pass the type as int, it will convert the user input to an integer
            user_input = type(input(message).strip())
        except ValueError:
            # if this recieves a value error, it will reiterate the same question until the input is satisfied
            continue
    return user_input
​
# this line of code is explained very well here:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# the short answer from that question is here:
# https://stackoverflow.com/a/419986/9662099
​
if __name__ == '__main__':
​
    # here we specify that we want three classes of Classmate to be instantiated
    USERS = complete_form(3)
​
    # since the complete_form function returns a list of Classmates, we can iterate
    # through that list with a for loop. Then, we will call the format_class function for
    # each of those objects
    for a in range(len(USERS)):
        USERS[a].format_class()

