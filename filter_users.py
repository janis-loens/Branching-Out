
import json

def load_users(path: str = "users.json") -> list:
    with open(path, "r") as file:
        users = json.load(file)
        print(type(users))
    return users

def filter_users_by_name(name: str):
    """Filter users by name from a JSON file.
    This function reads a JSON file containing user data and filters users by their name.
    It prints the details of users whose name matches the provided name (case-insensitive).

    Args:
        name (str): The name to filter users by.
    Returns:
        None
    """
    users = load_users()
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)


def filter_users_by_age(age: int):
    """Filter users by age from a JSON file.
    This function reads a JSON file containing user data and filters users by their age.
    It prints the details of users whose age matches the provided age.

    Args:
        age (int): The age to filter users by.
    Returns:
        None
    """
    users = load_users()
    
    filtered_users = [user for user in users if user["age"] == age]
    
    for user in filtered_users:
        print(user)


def filter_users_by_email(email: str):
    """Filter users by email from a JSON file.
    This function reads a JSON file containing user data and filters users by their email.
    It prints the details of users whose email matches the provided email (case-insensitive).
    Args:
        email (str): The email to filter users by.
    Returns:
        None
    """
    users = load_users()
    
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid integer for age.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
