
# Ask the user for a whole number and keep asking until it is valid
def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number <= 0:
                print("Please enter a number greater than 0.")
            else:
                return number
        except ValueError:
            # Happens when the user types letters or symbols
            print("Invalid input. Please enter a whole number.")


# Ask for a name and make sure it is not empty and has letters only
def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if name == "":
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name should contain letters only.")
        else:
            return name.title()


# Ask a yes/no question and return True for 'y' and False for 'n'
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")