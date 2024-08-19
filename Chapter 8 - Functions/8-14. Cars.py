def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


car = make_car('tesla', 'Model S', color='red', horse_power='500')
print(f"\nWe build this car :{car}")
