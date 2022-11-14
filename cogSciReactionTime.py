import tkinter as tk
import time

test = False

wordList = [['DIVE', 'V         N'], 
            ['F', 'F         R'], 
            ['CGSL', 'P         G'], 
            ['SENM', 'R         S'], 
            ['JUMP', 'M         S'],
            ['L', 'H         L'],
            ['JWOS', 'W         V'], 
            ['E', 'E         A'],
            ['NWRO', 'P         W'],
            ['SOAP', 'L         P'],
            ['O', 'B         O'],
            ['BRAT', 'A         O'],
            ['WSKE', 'K         Y'],
            ['J', 'K         J'],
            ['CMIW', 'Y         C'],
            ['BLUE', 'R         L'],
            ['HAND', 'A         U'],
            ['Y', 'K         Y'],
            ['AENP', 'P         U'],
            ['TNIS', 'N         L'],
            ['G', 'G         B'],
            ['FLAT', 'R         T'],
            ['N', 'L         N'],
            ['SING', 'S         C'],
            ['LKFO', 'F         R'],
            ['B', 'F         B'],
            ['FIVE', 'K         V'],
            ['CNWO', 'N         L'],
            ['SDNE', 'D         V'],
            ['U', 'Y         U'],
            ['RATE', 'G         T'],
            ['WORK', 'R         V'],
            ['A', 'O         A'],
            ['COME', 'J         M'],
            ['K', 'K         W'],
            ['PLAY', 'Y         K'],
            ['CROW', 'S         C'],
            ['WKEN', 'E         A'],
            ['C', 'R         C'],
            ['DARK', 'R         G'],
            ['T', 'T         H'],
            ['BYSL', 'P         Y'],
            ['EHUR', 'C         H'],
            ['S', 'S         F'],
            ['JNDX', 'D         S']
            ]
if test:
    wordList = [['TEST', 'T         X'], 
            ['DKJF', 'J         L'], 
            ['A', 'A         B'], 
            ]

i = 0
timeVar = 0
noPress = False

def main():
    global wordList
    global i
    global timeVar
    global noPress
    
    #create root window
    root = tk.Tk()

    #create label for text
    l = tk.Label(text="A word or character is going to be flashed on the screen, and then after a brief pause, two letters will appear. One of those letters was present in the word or character that was flashed, and one was not. Click the shift key of the corresponding side of the screen where the letter was present.                         Click any shift key to begin", wraplength='500', justify='center', width='100', height='25', font=("Arial", 20))

    #pack label to root window
    l.pack()

    def delay():
        #delay before displaying letters
        l["text"] = "- - - -"
        l.after(1500, switch_screen)

    def switch_screen():
        #displays letters to chooose from
        global i
        global noPress
        global timeVar
        l["text"] = wordList[i][1]

        #starts timer
        timeVar = time.time()

        i += 1
        noPress = False

    def handle_keypress(event):
        global noPress
        if not noPress:
            #checks if we are allowed to make selection
            if event.keycode == 131076 or event.keycode == 131074 or event.keycode == 131332: 
                global timeVar
                if timeVar == 0:
                    timeDifference = -1
                    l["font"] = ("Arial", 60)
                else:
                    #caclulates reaction time
                    timeDifference = time.time() - timeVar
                
                global wordList
                global i
                text = "BEGIN"
                rSide = '.'
                lSide = '.'
                if timeVar != 0:
                    text = wordList[i-1][0]
                    rSide = wordList[i-1][1][-1]
                    lSide = wordList[i-1][1][0]

                #check which key was hit
                if event.keycode == 131076:
                    #right shift
                    if rSide not in text:
                        print('WRONG: ' + text + ' - ' + rSide + ' - ' + str(timeDifference*1000))
                    else:
                        print(text + ' - ' + rSide + ' - ' + str(timeDifference*1000))

                if event.keycode == 131074:
                    #left shift
                    if lSide not in text:
                        print('WRONG: ' + text + ' - ' + lSide + ' - ' + str(timeDifference*1000))
                    else:
                        print(text + ' - ' + lSide + ' - ' + str(timeDifference*1000))
                    
                # Set new word for the label or close program
                if i >= len(wordList):
                    root.destroy()
                else:
                    l["text"] = wordList[i][0]
                    noPress = True
                    l.after(300, delay)

    # Attach the keypress event to our root window
    root.bind("<Key>", handle_keypress)

    root.mainloop()

if __name__=='__main__':
    main()
