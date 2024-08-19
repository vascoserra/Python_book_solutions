from city_functions import country_city


def test_city():
    city = country_city('lisboa', 'portugal')
    assert city == 'Lisboa, Portugal'


def test_city_country_population():
    city = country_city('lisboa', 'portugal', '5000')
    assert city == 'Lisboa, Portugal, 5000'
