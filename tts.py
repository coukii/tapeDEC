import glob
from tkinter import *


noteDict = {'C2':	1,
            'C#2':	2,
            'D2':	3,
            'D#2':	4,
            'E2':	5,
            'F2':	6,
            'F#2':	7,
            'G2':	8,
            'G#2':	9,
            'A2':	10,
            'A#2':	11,
            'B2':	12,
            'C3':	13,
            'C#3':	14,
            'D3':	15,
            'D#3':	16,
            'E3':	17,
            'F3':	18,
            'F#3':	19,
            'G3':	20,
            'G#3':	21,
            'A3':	22,
            'A#3':	23,
            'B3':	24,
            'C4':   25,
            'C#4':	26,
            'D4':	27,
            'D#4':	28,
            'E4':	29,
            'F4':	30,
            'F#4':	31,
            'G4':	32,
            'G#4':	33,
            'A4':	34,
            'A#4':	35,
            'B4':	36,
            'C5':	37}


txtFiles = []

for file in glob.glob('*.txt'):
    txtFiles.append(file)

looping = True
newfile = False


print('''
███████████████████████████████████████████████████████████
█                                                         █
█  █████████████████████████████████████████████████████  █
█  ███████████████████████████████████████████████  █  █  █
█  ██████████████████████████████████████████████████  █  █
█  █████████████████████████████████████████████████████  █
█  ███                                               ███  █
█  ███  ███████████████████████████████████████████  ███  █
█  ███  ███                                     ███  ███  █
█  ███  ██   █████   █████████████████   █████   ██  ███  █
█  ███  ██  ███████  █tapeDEC v.0.0.1█  ███████  ██  ███  █
█  ███  ██   █████   █████████████████   █████   ██  ███  █
█  ███  ███                                     ███  ███  █
█  ███  ███████████████████████████████████████████  ███  █
█  ███                                               ███  █
█  █████████████████████████████████████████████████████  █
█  ███████                                       ███████  █
█  ██████  █████████████████████████████████████  ██████  █
█  █████  ███████████████████████████████████████  █████  █
█  ████  █████████████████████████████████████████  ████  █
█                                                         █
███████████████████████████████████████████████████████████
''')


while looping == True:
    choice = input('############################################################### \nWELCOME TO tapeDEC! \n\nDO YOU WANT TO: \n 1. OPEN EXISTING FILE \n 2. CREATE NEW FILE \n')

    if choice == '1':
        for file in txtFiles:
            print(file)
        filename = input('INPUT FILENAME (NO EXTENSION): ')
        if filename + '.txt' in txtFiles:
            newfile = False
            looping = False
        else:
            print("FILE DOES NOT EXIST. \n \n")

    elif choice == '2':
        filename = input('INPUT FILENAME (NO EXTENSION) \n')
        if filename + '.txt' in txtFiles:
            print("FILE ALREADY EXISTS.\n \n")
        else:
            newfile = True
            looping = False

txt = open(filename + '.txt', 'a+')

if newfile == True:
    txt.write('[tts ')
else:
    txt.seek(0)
    for line in txt:
        print(line)
    txt.write('\n')

while True:
    note = input('ENTER NOTE: ').upper()
    if note == 'STOP':
        break
    elif note == '_':
        while True:
            try:
                length = int(input('ENTER LENGTH: '))
                break
            except (ValueError) as err:
                print('INVALID!')
        txt.write('[_<'+str(length)+'>]\n')
    elif note in noteDict:
        while True:
            try:
                length = int(input('ENTER LENGTH: '))
                break
            except (ValueError) as err:
                print('INVALID!')
        txt.write('[dah<'+str(length)+','+str(noteDict[note])+'>]\n')
    else:
        print('INVALID!')

txt.close()
