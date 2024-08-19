from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers1.json')
content = json.dumps(numbers)
path.write_text(numbers)