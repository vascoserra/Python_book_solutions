from pathlib import Path
path = Path('cats.txt')

def read(path):
    try : 
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        content = contents.split()
        print(content)

filenames = ['cats.txt', 'dogs.txt', 'cavalos.txt']
for filename in filenames:
    path = Path(filename)
    read(path)