import math

def load_cities(filename):
    cities = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.split()
            city = {
                "id": int(parts[0]),
                "name": parts[1],
                "population": int(parts[2]),
                "lat": float(parts[3]),
                "lon": float(parts[4])
            }
            cities.append(city)
    return cities

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]
    result = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for perm in generate_permutations(rest):
            result.append([elements[i]] + perm)
    return result

def generate_combinations(elements, k):
    if k == 0:
        return [[]]
    if len(elements) < k:
        return []
    result = []
    for i in range(len(elements)):
        rest = elements[i+1:]
        for comb in generate_combinations(rest, k-1):
            result.append([elements[i]] + comb)
    return result

def generate_multisets(elements, k):
    if k == 0:
        return [[]]
    result = []
    for i in range(len(elements)):
        for subset in generate_multisets(elements[i:], k-1):
            result.append([elements[i]] + subset)
    return result


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    def radians(deg):
        return deg * math.pi / 180
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = (math.sin(dphi/2))**2 + math.cos(phi1) * math.cos(phi2) * (math.sin(dlambda/2))**2
    return 2 * R * math.asin(math.sqrt(a))

def shortest_tsp_route(cities):
    best_route, min_distance = None, float('inf')
    for perm in generate_permutations(cities):
        distance = 0
        for i in range(len(perm) - 1):
            distance += haversine(perm[i]['lat'], perm[i]['lon'], perm[i+1]['lat'], perm[i+1]['lon'])
        distance += haversine(perm[-1]['lat'], perm[-1]['lon'], perm[0]['lat'], perm[0]['lon'])
        if distance < min_distance:
            min_distance = distance
            best_route = perm
    return best_route, min_distance

def closest_population_subset(cities):
    total_population = 0
    for city in cities:
        total_population += city['population']
    target = total_population / 2
    best_subset, best_diff = None, float('inf')
    for r in range(1, len(cities) + 1):
        for subset in generate_combinations(cities, r):
            subset_population = 0
            for city in subset:
                subset_population += city['population']
            diff = subset_population - target if subset_population > target else target - subset_population
            if diff < best_diff:
                best_diff, best_subset = diff, subset
    return best_subset

italy_cities = load_cities("Italy.txt")
france_cities = load_cities("France.txt")

N, M = 4, 2
selected_cities = italy_cities[:N]

print("Permutacje:")
for i, p in enumerate(generate_permutations(selected_cities), 1):
    print(i, [city["name"] for city in p])

print("\nKombinacje:")
for i, c in enumerate(generate_combinations(selected_cities, M), 1):
    print(i, [city["name"] for city in c])

print("\nMultizbiory:")
for i, m in enumerate(generate_multisets(selected_cities, M), 1):
    print(i, [city["name"] for city in m])

print("\nNajkrótsza trasa (TSP):")
best_route, min_distance = shortest_tsp_route(selected_cities)
print("Najkrótsza trasa:", [city["name"] for city in best_route])
print("Długość trasy:", min_distance, "km")

print("\nPodzbiór miast z populacją najbliższą 50%:")
best_subset = closest_population_subset(selected_cities)
print("Najlepszy podzbiór:", [city["name"] for city in best_subset])
