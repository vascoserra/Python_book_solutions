from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print(content.replace('Python', 'Java'))
print("\n")
lines = content.splitlines()

for line in lines:
    print(line.replace('Python', 'Java'))