def country_city(country, city):
    description = f"{city}, {country}"
    return description.title()

portugal = country_city('lisboa', 'portugal')
print(portugal)