planets_map = {'1': 'Mercury', '2': 'Venus', '3': 'Earth', '4': 'Mars', '5': 'Jupiter'}

planet_index = input()  # 3 -> Earth
print(planets_map[planet_index])

planet_name = input()  # Mars -> 4
print(list(planets_map.keys())[list(planets_map.values()).index(planet_name)])
