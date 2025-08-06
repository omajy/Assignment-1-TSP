from TSP import TSP

tsp = TSP('eil51.tsp')
print("City 1 Cordinates:", tsp.cities[0], " city 2 coords: " ,tsp.cities[1], " number of cities:", tsp.num_cities, "Distance between city 1 and 2:", tsp.dist_matrix[0][1])
