animais = []

simba = {
    'nome': 'simba',
    'dono': 'nina',
    'cor': 'laranja',
    'castrado': 'sim',
}

julia = {
    'nome': 'julia',
    'dono': 'nuno',
    'cor': 'malhada',
    'castrado': 'nao',
}
preta = {
    'nome': 'preta',
    'dono': 'nina',
    'cor': 'preto',
    'castrado': 'sim',
}
maria = {
    'nome': 'maria',
    'dono': 'joana',
    'cor': 'malhada',
    'castrado': 'sim',
}
animais.append(simba)
animais.append(preta)
animais.append(maria)
animais.append(julia)

for animal in animais:
    print(f"O que sabemos sobre: {animal['nome'].title()}")
    for k, v in animal.items():
        print(f"\t{k} : {v} ")
