from TSP import TSP

tsp = TSP()
tsp.load_from_file('eil51.tsp')
print("City 32 coordinates:", tsp.cities[32], " number of cities:", tsp.num_cities)
