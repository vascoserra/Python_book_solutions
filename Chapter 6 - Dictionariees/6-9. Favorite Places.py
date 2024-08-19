favorite_places = {
    'nuno': ['bariloche', 'porto', 'barcelona'],
    'joana': ['marselha', 'roma', 'veneza'],
    'conceicao': ['santiago de compostela', 'serta', 'milhazes']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")
