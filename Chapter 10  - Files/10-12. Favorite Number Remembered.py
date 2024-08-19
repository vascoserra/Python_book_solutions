from pathlib import Path
import json


path = Path('favorite_number.txt')
if path.exists():
    content = path.read_text()
    number  = json.loads(content)
    print(f"I already know that you love number {number}!!")
else:
    fav_number = input("Whats your favorite number? ")
    content = json.dumps(fav_number)
    path.write_text(content)
    print(f"I will remember that your favorite number is {fav_number}")
