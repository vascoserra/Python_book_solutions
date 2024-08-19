from pathlib import Path
import json

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
    username = input("What is your usernname? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('name.json')
    username = get_stored_username(path)
    if username:
        confirm = input(f"{username} its your username? (y/n)")
        if confirm == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()