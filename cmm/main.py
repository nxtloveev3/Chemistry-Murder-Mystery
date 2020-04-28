#######################################################
#Imported Modules
#######################################################

#built-in modules
from tkinter import *
import random

#Outside module
from cmu_112_graphics import *
import simpleaudio as sa

#custom modules
from lib.bedroom import*
from lib.kitchen import*
from lib.backyard import*
from lib.livingroom import*
from lib.checkpoint import*
from lib.AI import*
from lib.hintAI import *
from lib.conversation import*
from lib.people import*
########################################################
#citation this program uses 112 graphics from http://www.kosbie.net/cmu/fall-19/15-112/notes/notes-animations-part2.html#subclassingModalApp
# coler selection is based on color chart from https://www.webucator.com/blog/2015/03/python-color-constants-module/
# timer display methods adopted from https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
# structure disign adopted from https://github.com/LingDong-/Hermit
# sound methods adopted form https://simpleaudio.readthedocs.io/en/latest/tutorial.html
# every other modes have their own citations on the very top
########################################################


#######################################################
#Initiation + core Programs
#######################################################


#welcome screen
#welcome screen gives basic instructions to the player about
#what they can do in the game and what operation they can do
#This part also generates the random story line of the game!
########################################################
class welcomeMode(Mode): 
    def appStarted(mode):
        mode.combinationPool = {'Killer': ('John Patrick','Molly Barnett','Marlin Walter'),
                                'Location': ('livingroom','kitchen','backyard','bedroom'),
                                'Weapon': ('knife','GHB','pillow')}
        mode.result = []
        killer = random.choice(mode.combinationPool['Killer'])        
        mode.result.append(killer)
        location = random.choice(mode.combinationPool['Location'])
        mode.result.append(location)
        weapon = random.choice(mode.combinationPool['Weapon'])
        mode.result.append(weapon)
        mode.killer=mode.result[0]
        mode.location=mode.result[1]
        mode.weapon=mode.result[2]
        digits = ''
        for n in range(6):
            digits += str(random.randint(0,9))
        mode.code = digits
        mode.checkpointList = generateCheckpoint()
        mode.instruction = False
        print(mode.result)
        
    def keyPressed(mode, event):
        if (event.key=='h'):
            mode.app.hardMode = True
        elif (event.key=='e'):
            mode.app.easyMode = True
        if mode.app.easyMode == False and mode.app.hardMode == False and (event.key=='Space'):
            mode.instruction = True
        elif (mode.app.easyMode != False or mode.app.hardMode != False) and (event.key=='Space'):
            mode.app.gameStarted = True
            mode.app.setActiveMode(mode.app.livingRoomMode)
        else: return
           
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height, fill='lightblue')
        canvas.create_text(mode.width/2, mode.height/5, text='Welcome to Chemistry Murder Mystery!', fill='red', font='Arial 38 bold')
        canvas.create_text(mode.width/2, mode.height/2, text="The local police is baffled about Nico's missing case\n    and they want you to help them out. You can \n      investigate the crime scene(Nico's house) \n        use 'Left', 'Right', 'Up', and 'Down'. When \n         you want to exit an interactive scene\n            press 'Escape'. Each attempt will be \n          different! Press 'n' for notes. Press 's'\n    to confirm killer, location, and weapon.Press\n'h' for hard mode or 'e' for easy mode. Press 'Space'\n                           to start. Good luck!", font='Arial 26')
        canvas.create_text(mode.width/2, mode.height*5/6, text="                 Have Fun! \n A 112 game made by Leo Dong", font='Arial 14')
        if mode.instruction == True:
            canvas.create_rectangle(mode.width/8,mode.height/6,mode.width*7/8,mode.height*5/6,fill='gray')
            canvas.create_text(mode.width/2,mode.height/2,text="Please select game level!\n\n\n\n\n'E' for Easy   'H' for Hard",font='Arial 28 bold')
########################################################


#caseSolve
#This part basic varifies the guess user made and compare to 
#the correct answers and determine if you have complete the 
#game or not.
########################################################
class caseSolvedMode(Mode):
    def appStarted(mode):
        mode.checkpoint1=False
        mode.checkpoint2=False
        mode.checkpoint3=False
        mode.end=False
        mode.tryAgain=False

    def mousePressed(mode,event): 
        if mode.width/4<event.x<mode.width*3/4 and mode.height/7<event.y<mode.height*2/7:
            killer=mode.getUserInput('Suspect Name')
            if killer != None:
                if killer.lower()==mode.app.welcomeMode.killer.lower():
                    mode.checkpoint1=True
            else: return
        if mode.width/4<event.x<mode.width*3/4 and mode.height*3/7<event.y<mode.height*4/7:
            location=mode.getUserInput('Crime location')
            if location != None:  
                if location.lower()==mode.app.welcomeMode.location.lower():
                    mode.checkpoint2=True
            else: return
        elif mode.width/4<event.x<mode.width*3/4 and mode.height*5/7<event.y<mode.height*6/7:
            weapon=mode.getUserInput('Weapon')
            if weapon != None:
                if weapon.lower()==mode.app.welcomeMode.weapon.lower():
                    mode.checkpoint3=True
            else: return

    def keyPressed(mode,event):
        if(event.key == 'Escape') and mode.end == False:
            mode.tryAgain = False
            mode.app.setActiveMode(mode.app.currentMode)
        elif(event.key == 'Enter'):
            if mode.checkpoint1==mode.checkpoint2==mode.checkpoint3==True:
                mode.app.gameStarted = False
                mode.end = True
            else:
                mode.tryAgain = True
        elif (event.key == 'Escape') and mode.end == True:
            mode.app.quit()
        elif (event.key=='n'):
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='brown')
        for n in range(1,6,2):
            canvas.create_rectangle(mode.width/4,mode.height/7*n,mode.width*3/4,mode.height/7*(n+1),fill='gray')
        canvas.create_text(mode.width/2,mode.height*3/14,text='Suspect',font='Arial 20')
        canvas.create_text(mode.width/2,mode.height/2,text='Location',font='Arial 20')
        canvas.create_text(mode.width/2,mode.height*11/14,text='Weapon',font='Arial 20')
        canvas.create_text(mode.width/2,mode.height*13/14,text="Press 'Enter' to confirm",font='Arial 20 bold')
        if mode.end == True:
            canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
            canvas.create_text(mode.width/2,mode.height/2,text=f'Congratulation you solved the mystery in {mode.app.hourCount:02d}h {mode.app.minCount:02d}m {mode.app.secCount:02d}s',font='Arial 26')
        if mode.tryAgain == True:
            canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
            canvas.create_text(mode.width/2,mode.height/2,text=f'Sry Try Again',font='Arial 26')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')
########################################################


#User Notes 
#It's a note app that takes in user input and save it in
#it. It automatically indexes when recognize you enter
#different notes. On top of that it add new line if you
#exceeded the window side.
########################################################
class userNotesMode(Mode):
    def appStarted(mode):
        mode.notes = ''
        mode.cleanNotes = None
        mode.instruction = True
        
    def processNote(mode,note,string):   
        maxChar = mode.width//8
        if len(note)<maxChar:
            return string + note
        else:
            location = maxChar-len(note)
            string = string + note[:location] + '\n'
            return mode.processNote(note[location:],string)
    
    def keyPressed(mode,event):
        if (event.key=='Escape'):
            mode.app.setActiveMode(mode.app.currentMode)
        else:
            return       

    def mousePressed(mode,event):
        mode.instruction = False
        notes = mode.getUserInput('Type down your thoughts.')
        if notes != None:
            if len(mode.notes) == 0:
                mode.notes += notes
            else: mode.notes = mode.notes + '\t' + notes
            mode.cleanNotes = mode.processNote(mode.notes,'')
        else:
            mode.app.setActiveMode(mode.app.currentMode)
    
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height/8,fill='yellow')
        canvas.create_rectangle(0,mode.height/8,mode.width,mode.height,fill='white')
        if mode.cleanNotes != None:
            canvas.create_text(mode.width/2,mode.height/2,text=f'{mode.cleanNotes}',font='Arial 18')
        if mode.instruction == True:
            canvas.create_text(mode.width/2,mode.height/2,text="Click to enter what you want to write down as notes.",font='Arial 22 bold')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold')
########################################################


#game app
#This is the main game app that stores every modules 
#it also keep the timer updated
########################################################
class myGameApp(ModalApp):
    def appStarted(app):
        app.welcomeMode = welcomeMode()
        app.currentMode = welcomeMode()
        app.userNotesMode = userNotesMode()
        app.lewisStructureMode = lewisStructureMode()
        app.lewisStructureStartMode = lewisStructureStartMode()

        #livingroom
        app.livingRoomMode = livingRoomMode()
        app.tvMode = tvMode()
        app.tvSubMode = tvSubMode()
        app.computerMode = computerMode()
        app.desktopMode = desktopMode()
        app.table1Mode = table1Mode()
        app.notesMode = notesMode()
        app.table2Mode = table2Mode()

        #kitchen
        app.kitchenMode = kitchenMode()
        app.suspect1Mode = suspect1Mode()
        app.sinkMode = sinkMode()
        app.dinningMode = dinningMode()
        app.counterMode = counterMode()

        #bedroom
        app.bedroomMode = bedroomMode()
        app.suspect2Mode = suspect2Mode()
        app.tvDrawerMode = tvDrawerMode()
        app.bedMode = bedMode()

        #backyard
        app.backyardMode = backyardMode()
        app.suspect3Mode = suspect3Mode()
        app.storageMode = storageMode()
        app.nicoMode = nicoMode()

        #caseSolve
        app.caseSolvedMode = caseSolvedMode()

        #Hint System
        app.hintAI = hintAI()

        #Start Game
        app.setActiveMode(app.welcomeMode)
        app.door = sa.WaveObject.from_wave_file("door.wav")
        app.sink = sa.WaveObject.from_wave_file("water.wav")
        app.checkpoint = 0
        app.gameStarted = False
        app.easyMode = False
        app.hardMode = False
        app.secCount = 0
        app.minCount = 0
        app.hourCount = 0  
        app.timerDelay = 1000

    def playSound(mode,location):
        if location == "sink":
            play_obj = mode.sink.play()
            play_obj.wait_done()
        elif location == "door":
            play_obj = mode.door.play()
            play_obj.wait_done()       
    
    def timerFired(app):
        if app.gameStarted == True:
            if app.secCount < 60:
                app.secCount += 1
            else: 
                app.secCount -= 60
                app.minCount += 1
            if app.minCount >= 60:
                app.minCount -= 60
                app.hourCount += 1
        else:
            return

app = myGameApp(width = 800, height = 600)