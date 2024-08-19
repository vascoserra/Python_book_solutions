countries = {
    'china': {
        'population': '1.2 bilion',
        'native language': 'chinese',
        'favorite food': 'rice'
    },

    'portugal': {
        'population': '11 million',
        'native language': 'portuguese',
        'favorite food': 'cozido'
    },

    'india': {
        'population': '1.1 billion',
        'native language': 'indian',
        'favorite food': 'chiken taka masalah'
    },
}

# for country, countries_info in countries.items():
#    print(f"\nThis is what we know about :{country.title()}")
#    for k, v in countries_info.items():
#        print(f"\t{k} : {v}")

for country, countries_info in countries.items():
    name = country.title()
    population = countries_info['population'].title()
    native_language = countries_info['native language'].title()

    print(f"\n{name}'s has a population of {population} and their native language is {native_language}")
