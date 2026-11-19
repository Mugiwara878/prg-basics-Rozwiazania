###
# Compares average hotel prices in Krakow and Sopot
#
def hotel_list(hotels):
    names = []
    for h in hotels:
        names.append(h['name'])       # wyciaga sama nazwe ze slownika
    return ','.join(names)             # laczy liste w jeden string, przecinkami

def avg_price(hotels):
    total = 0
    for h in hotels:
        total += h['price']
    return round(total / len(hotels))  # srednia, zaokraglona do calkowitej

hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

avg_krakow = avg_price(hotels_in_Krakow)
avg_sopot = avg_price(hotels_in_Sopot)

print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))
print('Average hotel price in Krakow:', avg_krakow)
print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))
print('Average hotel price in Sopot:', avg_sopot)
cheaper = 'Krakow' if avg_krakow < avg_sopot else 'Sopot'   # ternary - ktory tanszy
print('Cheaper hotels in:', cheaper)