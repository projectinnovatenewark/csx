"""
Using functions and understanding scope
"""

EXAMPLE_DICTIONARY = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
EXAMPLE_DICTIONARY_TWO = {"Andy": 78, "Brovan": 86, "Celeste": 95, "Danilo": 100, "Epsilo": 88}

def dictionary_reader(dictionary):
    """this function will format and print a dictionary"""
    print("Let's output a dictionary")

    for student in dictionary:
        print(student + " got a score of " + str(dictionary[student]) + " on their exam!")

    print("Completed dictionary output")

dictionary_reader(EXAMPLE_DICTIONARY_TWO)
