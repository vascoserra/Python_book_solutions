def country_city(city, country, population=""):
    if population:
        description = f"{city}, {country}, {population}"
    else:
        description = f"{city}, {country}"
    return description.title()


portugal = country_city('lisboa', 'portugal', '5000')
print(portugal)
