from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back!\n")
        for k, v in username.items():
            print(f"We remember that {k} -> {v}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you!")
        for k, v in username.items():
            print(f"We remember that {k} -> {v}!")

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = {}
    name = input("What is your username? ")
    username['name'] = name
    age = input("What is your age? ")
    username['age'] = age
    contents = json.dumps(username)
    path.write_text(contents)
    return username

greet_user()