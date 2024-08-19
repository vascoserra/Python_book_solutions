from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    content = path.read_text()
    user = json.loads(content)
    print(f"{user.title()} good to see you back!")
else:
    user = input("What is your username? ")
    path = Path('username.json')
    content = json.dumps(user)
    path.write_text(content)
    print(f"We will remeber you {user}!")