#Ausztria;1995.01.01
#Belgium;1958.01.01

class Eu:
    def __init__(self, sor):
        orszag, datum = sor.strip().split(';')
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[:4])
        self.honap = int(datum[5:7])
        self.nap = int(datum[8:10])

#2. feladat

lista = []

with open('EUcsatlakozas.txt', 'r', encoding='latin2') as f:
    for sorok in f:
        lista.append(Eu(sorok))

#3. feladat

print(f'3. feladat: EU tagállamainak száma: {len(lista)} db')

#4. feladat

csatlakozas = len([sor for sor in lista if sor.ev == 2007])

print(f'4. feladat: 2007-ben {csatlakozas} ország csatlakozott.')

#5. feladat

magyarcsatlakozas = [sor.datum for sor in lista if sor.orszag == 'Magyarország']

print(f'5. feladat: Magyarország csatlakozásának dátuma: {magyarcsatlakozas[0]}')

#6. feladat

volte = len([sor for sor in lista if sor.honap == 5])

if volte > 0:
    print(f'6. feladat: Májusban volt csatlakozás.')
else:
    print(f'6. feladat: Májusban nem volt csatlakozás.')


#7. feladat

utoljara = max(lista, key=lambda x:x.datum).orszag
print(f'7. feladat: Legutoljára csatlakozott ország: {utoljara}')

#8. feladat
print('8. feladat: Statisztika')
stat = dict()

for sor in lista:
    stat[sor.ev] = stat.get(sor.ev, 0) + 1

for ertek, kulcs in stat.items():
    print(f'        {ertek} - {kulcs} ország')
    