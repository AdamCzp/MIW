Slownik = []
atrybuty = []
with open("plik.txt", "r") as f:
    linie = f.readlines()
liczba_kolumn = len(linie[0].split())
atrybuty = [f"a{i+1}" for i in range(liczba_kolumn - 1)]
for linia in linie:
    liczby = list(map(int, linia.split()))
    dane = {atrybuty[i]: liczby[i] for i in range(len(atrybuty))}
    dane["d"] = liczby[-1]
    Slownik.append(dane)
for objekt in Slownik:
    print(objekt)


def sprzecznosc(ob1, ob2, atrybuty):
    zgodne_atrybuty = all(ob1[a] == ob2[a] for a in atrybuty)
    rozne_decyzje = ob1['d'] != ob2['d']
    return zgodne_atrybuty and rozne_decyzje


def generuj_kombinacje(atrybuty, n):
    if n == 1:
        return [[a] for a in atrybuty]
    wynik = []
    for i in range(len(atrybuty)):
        for reszta in generuj_kombinacje(atrybuty[i + 1:], n - 1):
            wynik.append([atrybuty[i]] + reszta)
    return wynik


znalezione_reguly = []
pokryte_obiekty = []
liczba_pokryte_obiekty = 0

for ilosc_atrybutow in range(1, len(atrybuty) + 1):
    for i in range(len(Slownik)):
        if i in pokryte_obiekty:
            continue
        obj_i = Slownik[i]
        for kombinacja in generuj_kombinacje(atrybuty, ilosc_atrybutow):
            if i in pokryte_obiekty:
                continue
            if any(sprzecznosc(obj_i, obj, kombinacja) for obj in Slownik if obj != obj_i):
                continue
            for j in range(len(Slownik)):
                obj_j = Slownik[j]
                if all(obj_j[a] == obj_i[a] for a in kombinacja):
                    liczba_pokryte_obiekty = liczba_pokryte_obiekty + 1
                    if j not in pokryte_obiekty:
                        pokryte_obiekty.append(j)
            regula = 'o'+f"{i+1}" f"{''.join(f'({a}={obj_i[a]})' for a in kombinacja)} -> (d={(obj_i['d'])})" '['+f"{liczba_pokryte_obiekty}"+']'
            if regula not in znalezione_reguly:
                znalezione_reguly.append(regula)
            liczba_pokryte_obiekty = 0

for regula in znalezione_reguly:
    print(regula)