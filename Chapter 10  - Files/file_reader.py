from pathlib import Path

path = Path('number.txt')
#contents = path.read_text()
#contents = contents.rstrip()
contents = path.read_text()
lines = contents.splitlines()
space = ' '
for line in lines:
    space += line

print(space)
print(len(space))

