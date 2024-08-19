from pathlib import Path
import json

fav_number = input("Whats your favorite number? ")
path = Path('favorite_number.txt')
content = json.dumps(fav_number)
path.write_text(content)
print(f"I know your favorite number is {fav_number}")