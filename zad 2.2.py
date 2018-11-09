from datetime import datetime
from tkinter import filedialog, Tk
import os
import shutil

Tk().withdraw()
foldersList = list()

### Napisać skrypt, który pobiera z ustalonego pliku listę (w kolejnych wierszach) folderów
with filedialog.askopenfile(title = 'Wybierz plik tekstowy') as f:  #asks which file to open
    foldersList = f.readlines()                                     #adds folder directory from opened file to list
f.close() 
print("Folder list:")                                               #tests
print(*foldersList, sep='\n')
print("First folder is: " + foldersList[0])

### w osobnym ustalonym folderze tworzy podfolder z nazwą wskazującą na aktualną date
di = filedialog.askdirectory(title = 'Wybierz folder')  #asks for folder directory
fn = di + '/' + str(datetime.now()).replace(":", "-")   #adds current date to the path as a name the for new folder
if not os.path.exists(fn):                              #checks if path doesn't exist
    os.makedirs(fn)                                     #creates new folder in (fn) directory
print("New folder directory is: " + fn)

### po czym kopiuje do niego wszystkie pliki z folderów z list
for i in range(len(foldersList)):                                   #for every item (folder) in list
    print(foldersList[i])
    files = os.listdir(foldersList[i].strip())                      #collects names of all files in specified folder, .strip() removes whitespaces from paths
    for filename in files:                                          #for every file
        fullName = os.path.join(foldersList[i].strip(), filename)   #joins file's paths with file's names to create full directory of file
        if os.path.isfile(fullName):                                #checks if path includes file
            shutil.copy(fullName, fn)                               #copies file from "fullname" directory to "fn" directory
