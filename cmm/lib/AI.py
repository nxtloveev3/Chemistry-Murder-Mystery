from cmu_112_graphics import *
from tkinter import *
import math

#lewisStructure
########################################################

#starting + instruction Page
class lewisStructureStartMode(Mode):
    def keyPressed(mode,event):
        if (event.key == 'd'):
            mode.app.setActiveMode(mode.app.lewisStructureMode)
        elif (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.currentMode)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='lightblue')
        canvas.create_text(mode.width/2,mode.height/2,text=f"You found out there is substantial amount of unusal compound {mode.app.currentMode.compound}.\n Press 'd' to draw the lewis dot structure.\n If you get it right there will be time deduction. \nGood luck! Press 'Escape' to exit to livingroom.",font='Arial 22')

#main program
class lewisStructureMode(Mode):
    def appStarted(mode):
        mode.x = 0
        mode.y = 0
        mode.electronMode = False
        mode.drawElectron = False
        mode.electronCords = []
        mode.bondMode = False
        mode.drawBond = False
        mode.bondCords = []
        mode.atomsMode = False
        mode.drawAtoms = False
        mode.atomsCords = []
        mode.atomsSubMode = False
        mode.bondLength = 80
        mode.leftCount = 0
        mode.rightCount = 0
        mode.chemicalCompound = mode.app.currentMode.compound
        mode.atomList = mode.searchForAtoms(mode.chemicalCompound)
        mode.atomColor = {'H': 'orange',
                         'C': 'red',
                         'O': 'green'}
        mode.atomCharge = {'H': 1,
                          'C': 4,
                          'O': 6}
        mode.atomCount = len(mode.atomList)
        mode.colorList = []
        mode.charge = 0
        for atom in mode.atomList:
            mode.colorList.append(mode.atomColor[atom])
            mode.charge += mode.atomCharge[atom]
        mode.hydrogen = False
        mode.carbon = False
        mode.oxygen = False
        mode.correct = False
        mode.tryAgain = False

    def checkDrawing(mode):
        electronCount = len(mode.electronCords)
        bondCount = len(mode.bondCords)
        atomCount = len(mode.atomsCords)
        totalCharge = electronCount + bondCount*2
        if totalCharge == mode.charge and mode.atomCount == atomCount:
            for atomCord in mode.atomsCords:
                x = atomCord[0]
                y = atomCord[1]
                nearElectronCount = 0
                nearBondCount = 0
                color = atomCord[2]
                if color in mode.colorList:
                    mode.colorList.remove(color)
                for electronCord in mode.electronCords:
                    xE = electronCord[0]
                    yE = electronCord[1]
                    distenceToAtom = ((xE-x)**2+(yE-y)**2)**0.5
                    if distenceToAtom <= 35:
                        nearElectronCount += 1
                for bondCord in mode.bondCords:
                    xB = bondCord[0]
                    yB = bondCord[1]
                    x2B = bondCord[2]
                    y2B = bondCord[3]
                    distenceToBond1End = ((xB-x)**2+(yB-y)**2)**0.5
                    distenceToBond2End = ((x2B-x)**2+(y2B-y)**2)**0.5
                    if distenceToBond1End <= 20 or distenceToBond2End <= 20:
                        nearBondCount += 1
                if nearElectronCount + nearBondCount*2 == 8:
                    atomCheck = True
                elif nearElectronCount == 0 and nearBondCount == 1:
                    hydrogenCheck = True
                else:
                    return False
                    break
            if atomCheck == True and hydrogenCheck == True and len(mode.colorList) == 0:
                return True
        else:
            return False
        
    def searchForAtoms(mode,n):
        result = []
        for char in n:
            if char.isalpha():
                result.append(char)  
            else:
                for n in range(int(char)-1):
                    result.append(result[-1])
        return sorted(result)

    def mousePressed(mode,event):
        if (0<event.x<mode.width/3) and (mode.height*5/6<event.y<mode.height):
            mode.electronMode = True
            mode.bondMode = False
            mode.atomsSubMode = False
        elif (mode.width/3<event.x<mode.width*2/3) and (mode.height*5/6<event.y<mode.height):
            mode.electronMode = False
            mode.bondMode = True
            mode.atomsSubMode = False
        elif (mode.width*2/3<event.x<mode.width) and (mode.height*5/6<event.y<mode.height):
            mode.electronMode = False
            mode.bondMode = False
            mode.atomsSubMode = True
        if (mode.width*2/3<event.x<mode.width) and (mode.height/2<event.y<mode.height*11/18 and mode.atomsSubMode == True):
            mode.atomsMode = True
            mode.carbon = True
            mode.hydrogen = False
            mode.oxygen = False
        elif (mode.width*2/3<event.x<mode.width) and (mode.height*11/18<event.y<mode.height*13/18 and mode.atomsSubMode == True):
            mode.atomsMode = True
            mode.hydrogen = True
            mode.carbon = False
            mode.oxygen = False
        elif (mode.width*2/3<event.x<mode.width) and (mode.height*13/18<event.y<mode.height*5/6) and mode.atomsSubMode == True:
            mode.atomsMode = True
            mode.oxygen = True
            mode.hydrogen = False
            mode.carbon = False

    def mouseDragged(mode,event):
        mode.x = event.x
        mode.y = event.y
        if mode.electronMode == True:
            mode.drawElectron = True
        elif mode.bondMode == True:
            mode.drawBond = True
        elif mode.atomsMode == True:
            mode.drawAtoms = True
    
    def mouseReleased(mode,event):
        mode.x = event.x
        mode.y = event.y
        cx = event.x-40
        cy = event.y
        x1 = event.x+40
        y1 = event.y
        if mode.electronMode == True:
            mode.electronCords.append([mode.x,mode.y])
            mode.drawElectron = False
        elif mode.bondMode == True:
            mode.bondCords.append([cx,cy,x1,y1])
            mode.drawBond = False
        elif mode.atomsMode == True:
            if mode.carbon == True:
                mode.atomsCords.append([mode.x,mode.y,'orange'])
            elif mode.oxygen == True:
                mode.atomsCords.append([mode.x,mode.y,'red'])
            elif mode.hydrogen == True:
                mode.atomsCords.append([mode.x,mode.y,'green'])
            mode.drawAtoms = False

    def keyPressed(mode,event):
        if (event.key == 'x') or (event.key == 'X'):
            if mode.electronMode == True and len(mode.electronCords)>0:
                mode.electronCords.pop()
            elif mode.bondMode == True and len(mode.bondCords)>0:
                mode.bondCords.pop()
            elif mode.atomsMode == True and len(mode.atomsCords)>0:
                mode.atomsCords.pop()
        elif (event.key == 'a') or (event.key == 'A'):
            mode.leftCount += 1
            if mode.bondMode == True and mode.bondCords != None:
                mode.bondCords[-1][3] = mode.bondCords[-1][1] - mode.bondLength*math.sin(math.pi/4*mode.leftCount)
                mode.bondCords[-1][2] = mode.bondCords[-1][0] + mode.bondLength*math.cos(math.pi/4*mode.leftCount)
        elif (event.key == 'd') or (event.key == 'D'):
            mode.rightCount += 1
            if mode.bondMode == True and mode.bondCords != None:
                mode.bondCords[-1][3] = mode.bondCords[-1][1] + mode.bondLength*math.sin(math.pi/4*mode.rightCount)
                mode.bondCords[-1][2] = mode.bondCords[-1][0] + mode.bondLength*math.cos(math.pi/4*mode.rightCount)
        elif (event.key == 'Enter'):
            if mode.checkDrawing():
                mode.correct = True
                mode.tryAgain = False
                mode.app.minCount -= 4
            else:
                mode.tryAgain = True
        elif (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.currentMode)

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
        canvas.create_rectangle(0,mode.height*5/6,mode.width/3,mode.height,fill='gray')
        canvas.create_text(mode.width/6,mode.height*11/12,text='Electron')
        canvas.create_rectangle(mode.width/3,mode.height*5/6,mode.width*2/3,mode.height,fill='gray')
        canvas.create_text(mode.width/2,mode.height*11/12,text='Bond')
        canvas.create_rectangle(mode.width*2/3,mode.height*5/6,mode.width,mode.height,fill='gray')
        canvas.create_text(mode.width*5/6,mode.height*11/12,text='Atom')
        
        if mode.atomsSubMode==True:
            canvas.create_rectangle(mode.width*2/3,mode.height/2,mode.width,mode.height*5/6,fill='gray')
            for n in range(1,3):
                canvas.create_line(mode.width*2/3,mode.height/2+n*mode.height/9,mode.width,mode.height/2+n*mode.height/9)
            canvas.create_text(mode.width*5/6,mode.height*5/9,text='Hydrgen')
            canvas.create_text(mode.width*5/6,mode.height*2/3,text='Oxygen')
            canvas.create_text(mode.width*5/6,mode.height*7/9,text='Carben')
        if mode.drawElectron==True:
            canvas.create_oval(mode.x-5,mode.y-5,mode.x+5,mode.y+5,fill='black')
        elif mode.drawBond==True:
            canvas.create_line(mode.x-40,mode.y,mode.x+40,mode.y,width=10)
        elif mode.drawAtoms==True:
            if mode.carbon==True:
                canvas.create_oval(mode.x-20,mode.y-20,mode.x+20,mode.y+20,fill='orange')
            elif mode.hydrogen==True:
                canvas.create_oval(mode.x-20,mode.y-20,mode.x+20,mode.y+20,fill='green')
            elif mode.oxygen==True:
                canvas.create_oval(mode.x-20,mode.y-20,mode.x+20,mode.y+20,fill='red')
        for row in mode.electronCords:
            canvas.create_oval(row[0]-5,row[1]-5,row[0]+5,row[1]+5,fill='black')
        for row in mode.bondCords:
            canvas.create_line(row[0],row[1],row[2],row[3],width=10)
        for row in mode.atomsCords:
            canvas.create_oval(row[0]-20,row[1]-20,row[0]+20,row[1]+20,fill=f'{row[2]}')
        if mode.correct == True:
            canvas.create_rectangle(mode.width/8,mode.height/6,mode.width*7/8,mode.height*5/6,fill='silver')
            canvas.create_text(mode.width/2,mode.height/2,text='Nice Job! Time reduction',font='Arial 26')
        if mode.tryAgain == True:
            canvas.create_rectangle(mode.width/8,mode.height/6,mode.width*7/8,mode.height*5/6,fill='silver')
            canvas.create_text(mode.width/2,mode.height/2,text="Incorrect, press 'Escape' to exit.",font='Arial 26')
