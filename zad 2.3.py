from tkinter import filedialog, Tk
import csv
import os
import shutil


class Tranzakcje:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


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
                print(row['Numer placówki'])
                if row['Numer placówki'] not in Placowka.nrPlacowek:
                    Placowka.nrPlacowek.append(row['Numer placówki'])
                    Placowka.placowki.append(Placowka(row['Numer placówki']))

        stream.close()
print("TEST")
print(len(Placowka.placowki))
print(Placowka.placowki[0].name)


### -sumarycznej kwocie transakcji w poszczególnych placówkach (uwaga: przykładowe pliki uwzględniają 3 placówki, ale przyjmujemy, że nie mamy pewności, ile ich jest), 

### -średniej (dla wszystkich placówek) wysokości transakcji w poszczególnych tygodniach (uwaga: przykładowe pliki grupują transakcje tygodniami, ale przyjmujemy, że nie jest to zagwarantowane) 

### -średnim tygodniowym przychodzie z poszczególnych placówek



