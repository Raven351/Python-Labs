from datetime import datetime
from tkinter import filedialog, Tk
import os

Tk().withdraw()
foldersList = list()
### Napisać skrypt, który pobiera z ustalonego pliku listę (w kolejnych wierszach) folderów
with filedialog.askopenfile(title = 'Wybierz plik tekstowy') as f:
    foldersList = f.readlines()
f.close()
print(*foldersList, sep='\n')
print("dr " + foldersList[0])

### w osobnym ustalonym folderze tworzy podfolder z nazwą wskazującą na aktualną date
di = filedialog.askdirectory(title = 'Wybierz folder')
di += '/' + str(datetime.now()).replace(":", "-")
if not os.path.exists(di):
    os.makedirs(di)
print(di)

### po czym kopiuje do niego wszystkie pliki z folderów z list
for folder in foldersList:
    