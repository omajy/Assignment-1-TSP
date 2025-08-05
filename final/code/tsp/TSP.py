import math
import os
class TSP:
    # loads a TSP file and parses it into a data structure
    def __init__(self):
        #holds the number of cities, a dictionary of city coordinates, and a distance matrix
        self.num_cities = 0
        self.cities = {}
        self.dist_matrix = []
        
    def load_from_file(self, filename):
        # Reads the .tsp file from our TSPlib_data folder and begins to parse it into our data structure
        
        here = os.path.dirname(__file__)
        data_path = os.path.join(here, '../TSPlib_data', filename)
        
        with open(data_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                #extracts the number of cities
                if line.startswith('DIMENSION'):
                    parts = line.split(':')
                    self.num_cities = int(parts[1].strip())
                    
                elif line.strip() == 'NODE_COORD_SECTION':
                    # Start reading city data from the next line
                    for city_line in lines[i+1 : i+1 + self.num_cities]:
                        #split each line into parts and inputs them into our cities dictionary
                        
                        parts = city_line.split()
                        city_id, x, y = int(parts[0]), float(parts[1]), float(parts[2])
                        self.cities[city_id] = (x, y)
                        
                    break

