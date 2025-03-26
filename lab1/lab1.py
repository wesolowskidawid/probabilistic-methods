import math


class City:
    id = 0
    town = ""
    population = 0
    latitude = 0.0
    longitude = 0.0

    def __init__(self, id, town, population, latitude, longitude):
        self.id = int(id)
        self.town = town
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self) -> str:
        return str(self.town)

    def __repr__(self) -> str:
        return str(self.town)

plik = open("france.txt", "r").read().split("\n")[1:]
cities = []
for linia in plik:
    podzial = linia.split(" ")
    cities += [City(podzial[0], podzial[1], podzial[2], podzial[3], podzial[4])]


def distance(miasto1: City, miasto2: City) -> float:
    return math.sqrt((miasto2.latitude - miasto1.latitude)**2 + (miasto2.longitude - miasto1.longitude)**2)



licznik2 = 1


def wariacje_bez_powtorzen(n, m, ob=[], wynik=[]):
    global licznik2
    if len(ob) == m:
        if ob in wynik:
            return
        wynik += [ob]
        print(f"{licznik2}: {ob}")
        licznik2 += 1
        return

    for i in range(n):
        miasto = cities[i]
        if miasto not in ob:
            wariacje_bez_powtorzen(n, m, ob + [miasto], wynik)
    return wynik


licznik = 1
def kombinacje(n, m, ob, wynik):
    global licznik
    if len(ob) == m:
        if ob in wynik:
            return
        wynik += [ob]
        print(f"{licznik}: {ob}")
        licznik += 1
        return
    for i in range(n):
        miasto = cities[i]
        if miasto not in ob:
            kombinacje(n, m, ob + [miasto], wynik)
    return wynik

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def newton(n, k):
    gora = factorial(n)
    dol = factorial(k) * factorial(n-k)
    return gora/dol


N = int(input("Wpisz N: "))
M = int(input("Wpisz M: "))

# zadanie 1
powinno = int(factorial(N)/factorial(N-M))
if M > N:
    powinno = 0
#print(f"powinno byc: {powinno}")
#wariacje_bez_powtorzen(N, M, [], [])

# zadanie 2
powinno = newton(M+N-1, N-1)
#print(f"powinno byc: {int(powinno)}")
#kombinacje(N, M, [], [])

def trzyuz():
    wycieczki = wariacje_bez_powtorzen(7, 5, [], [])
    odleglosci = []
    for i in range(len(wycieczki)):
        ob = wycieczki[i]
        poprz = ob[0]
        ob_odl = 0
        for j in range(1, len(ob)):
            ob_odl += distance(poprz, ob[j])
            poprz = ob[j]
        ob.append(ob[0])
        ob_odl += distance(poprz, ob[len(ob) - 1])
        odleglosci.append(ob_odl)
    zl = list(zip(wycieczki, odleglosci))
    zl.sort(key=lambda x: x[1])
    return zl

wyniktrzecie = trzyuz()
#print(wyniktrzecie[0])

def czwuz():
    komb = kombinacje(N, M, [], [])
    l = len(komb)
    zakr = 0
    suma = sum(map(lambda x: x.population, cities[:N]))
    for ob in komb:
        uni = list(set(ob))
        ob_suma = sum(map(lambda x: x.population, uni))
        if ob_suma >= 0.4*suma and ob_suma <= 0.6*suma:
            zakr += 1
    print(f"{zakr}/{l} = {zakr/l}")


czwuz()
