from datetime import datetime
from tkinter import filedialog, Tk
import subprocess
import webbrowser


Tk().withdraw() #hides main window
di = filedialog.askdirectory(title='Wybierz folder') #shows dialog to choose a folder and saves directory in var
print(di)
fn = di + '/' + str(datetime.now()).replace(":", "-") + '.txt' #replaces every ":" char with "-""
print (fn)
with open(fn, 'w+') as f: #opens stream, opens or creates file
    pass
f.close()

proc = subprocess.Popen(('notepad.exe', fn)) #opens notepad.exe
proc.wait() #wait until it closes


with open(fn, 'r') as f: #open file in read mode
    linesCount = 0
    for line in f: #count lines in file
        linesCount += 1
    print(linesCount)
    name = ''
    if linesCount == 0: 
        name = "puste"
    elif linesCount == 1:
        name = "krótkie"
    elif 10 > linesCount > 1:
        name = "średnie"
    else:
        name = "długie"
    name += '.txt'
f.close()
with open(di + '/' + name, 'a') as fn2: #open file in append mode
    fn2.write(fn + '\n') #write new line with file name
fn2.close()