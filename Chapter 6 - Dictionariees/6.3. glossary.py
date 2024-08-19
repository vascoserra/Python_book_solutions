glossary = {
    'tuple': 'a finite ordered list (sequence) of elements',
    'list': 'a finite ordered list (sequence) of elements',
    'loop': 'used for iterating over a sequence',
    'dictionaries': 'key-value pairs'
}
# print(f"A tuple is {glossary['tuple']}")
# print(f"A list is {glossary['list']}")
# print(f"A loop is {glossary['loop']}")
# print(f"A dictionarie is {glossary['dictionaries']}")
for types, meaning in glossary.items():
    print(f"{types} are {meaning}")
