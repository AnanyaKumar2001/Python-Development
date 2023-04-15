# ------------------------------------------------------------
# ----------------------**## Scope ##**-----------------------

# Local Variables
# Global Variables

# ***************------------ Example 14

def message(date):
    content = "something very cool has happened"


message("May 22, 2100")

# print(date) # NameError
# print(content) # NameError

# ***************------------ Example 15


def comment(date):
    content = "amazing landscape"


comment("May 23, 2135")


# ***************------------ Example 16

content = "just do it"


def post(date):
    content = "i am on a trip"


post("Jan 1, 1970")

# print(content)


# ***************------------ Example 17

dog_name = "Hachi"


def animal_names():
    global dog_name
    dog_name = "Georgie"


animal_names()

print(dog_name)
