from tkinter import filedialog, Tk
import csv
import os
import shutil
from datetime import datetime

class Tranzakcje:
    listaTranzakcji = list()
    listaPlacówek = list()

    def __init__(self, placowka, data, kwota):
        self.placowka = placowka
        self.data = data
        self.kwota = kwota

Tk().withdraw()
### Napisać skrypt, który z podanego folderu (przykładowy folder i pliki w z6 dane) 
### wybierze wszystkie pliki z rozszerzeniem .csv i stworzy nowe pliki z informacjami o:
di = filedialog.askdirectory(title = 'Wybierz folder')  
files = os.listdir(di) 
print(files)
print(len(files))
print(di + '/' + files[0])
for i in range(len(files)):                         #for every file name
    if str(files[i]).endswith(".csv"):              #if file ends with.csv
        with open(di + '/' + files[i]) as stream:   #open file stream
            reader = csv.DictReader(stream)         #use csv dictionary for a stream
            for row in reader:                      #for every row in csv
                t = Tranzakcje(str(row['Numer placówki']), datetime.strptime(row['Data i godzina'], '%Y.%m.%d.%H.%M'), int(row['Kwota transakcji'])) #create object with parameters' values from csv
                Tranzakcje.listaTranzakcji.append(t) #add object to static list of objects
                if row['Numer placówki'] not in Tranzakcje.listaPlacówek: #if there is no number in a list...
                    Tranzakcje.listaPlacówek.append(row['Numer placówki']) #...add it
        stream.close()

print("TEST")
print(Tranzakcje.listaTranzakcji[28].data)


### -sumarycznej kwocie transakcji w poszczególnych placówkach (uwaga: przykładowe pliki uwzględniają 3 placówki, ale przyjmujemy, że nie mamy pewności, ile ich jest), 
def sumPlacowki():
    s = list()
    for p in range(len(Tranzakcje.listaPlacówek)):
        total = 0
        for tranzakcja in range(len(Tranzakcje.listaTranzakcji)):
            if Tranzakcje.listaTranzakcji[tranzakcja].placowka == Tranzakcje.listaPlacówek[p]:
                total += Tranzakcje.listaTranzakcji[tranzakcja].kwota
        s.append('Placowka nr ' + str(Tranzakcje.listaPlacówek[p]) + ': ' + str(total))
    return s

s = sumPlacowki()

for i in range(len(s)):
    print(s[i])


### -średniej (dla wszystkich placówek) wysokości transakcji w poszczególnych tygodniach (uwaga: przykładowe pliki grupują transakcje tygodniami, ale przyjmujemy, że nie jest to zagwarantowane) 

### -średnim tygodniowym przychodzie z poszczególnych placówek



