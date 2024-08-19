from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print(content)
print("\n")

for line in content.splitlines():
    print(line.replace('Python', 'Java'))