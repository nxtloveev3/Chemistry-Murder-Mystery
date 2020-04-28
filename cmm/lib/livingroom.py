from cmu_112_graphics import*
import random

#citation furniture images used in this room dowloaded from https://www.shutterstock.com/image-vector/icons-set-interior-furniture-top-view-699488854
#cat image from https://www.amazon.com/Cat-Notebook-Journal-Accessories-Novelty/dp/1095009443
#burger image from https://www.dreamstime.com/stock-photo-bitten-off-burger-paper-background-top-view-image75184297
#chemical image from http://www.emcdda.europa.eu/media-library/molecular-structure-ghb_en
#questionmark image from http://pixelartmaker.com/art/30ac2a54dfa0553
########################################################
class livingRoomMode(Mode):
    def appStarted(mode):
        mode.app.currentMode = mode.app.livingRoomMode
        mode.playerx = (mode.width*4/7+mode.width*5/7)/2
        mode.playery = (2*mode.height-30)/2
        mode.sofaRaw = mode.loadImage('sofa.png')
        mode.sofa = mode.scaleImage(mode.sofaRaw, 3/5)
        mode.sofa2Raw = mode.loadImage('sofa2.png')
        mode.sofa2 = mode.scaleImage(mode.sofa2Raw, 3/5)
        mode.tvRaw = mode.loadImage('tv.png')
        mode.tv = mode.scaleImage(mode.tvRaw, 4/5)
        mode.tableRaw = mode.loadImage('table.png')
        mode.table = mode.scaleImage(mode.tableRaw, 4/5)
        mode.workRaw = mode.loadImage('work.png')
        mode.workdesk= mode.scaleImage(mode.workRaw, 1/2)
        mode.rugRaw = mode.loadImage('rug.png')
        mode.rug= mode.scaleImage(mode.rugRaw, 1/5)
        mode.table2Raw = mode.loadImage('table2.png')
        mode.table2 = mode.scaleImage(mode.table2Raw, 3/5)
        mode.chairRaw = mode.loadImage('chair.png')
        mode.chair = mode.scaleImage(mode.chairRaw, 4/5)
        mode.chair2Raw = mode.loadImage('chair2.png')
        mode.chair2 = mode.scaleImage(mode.chair2Raw, 4/5)
        mode.questionmarkRaw = mode.loadImage('questionmark.png')
        mode.questionmark = mode.scaleImage(mode.questionmarkRaw, 1/25)
        mode.compound = "C4H8O3"
        mode.hintCount = 0
        mode.complete = 0

    def makePlayerInteractive(mode):
        if mode.app.hardMode == True:
            if (mode.width*2/15-50<mode.playerx<mode.width*2/15+50) and (mode.height-40<mode.playery<mode.height) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['tvMode']:
                mode.app.setActiveMode(mode.app.tvMode)
            elif (mode.width-50<mode.playerx<mode.width) and (mode.height-85<mode.playery<mode.height) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['computerMode']:
                mode.app.setActiveMode(mode.app.computerMode)
            elif (mode.width/7-30<mode.playerx<mode.width/7+30) and (mode.height*4/5-30<mode.playery<mode.height*4/5+30) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['table1Mode']:
                mode.app.setActiveMode(mode.app.table1Mode)
            elif (mode.width*2/7-75<mode.playerx<mode.width*2/7+75) and (mode.height/6<mode.playery<mode.height/6+52) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['table2Mode']:
                mode.app.setActiveMode(mode.app.table2Mode)   
        else:
            if (mode.width*4/7<mode.playerx<mode.width*5/7) and (mode.height-30< mode.playery<mode.height):
                mode.app.setActiveMode(mode.app.hintAI)
            elif (mode.width*2/15-50<mode.playerx<mode.width*2/15+50) and (mode.height-40<mode.playery<mode.height):
                mode.app.hintAI.recordEnterTime('livingroom','tv')
                mode.app.setActiveMode(mode.app.tvMode)
            elif (mode.width-50<mode.playerx<mode.width) and (mode.height-85<mode.playery<mode.height):
                mode.app.hintAI.recordEnterTime('livingroom','computer')
                mode.app.setActiveMode(mode.app.computerMode)
            elif (mode.width/7-30<mode.playerx<mode.width/7+30) and (mode.height*4/5-30<mode.playery<mode.height*4/5+30):
                mode.app.hintAI.recordEnterTime('livingroom','table1')
                mode.app.setActiveMode(mode.app.table1Mode)
            elif (mode.width*2/7-75<mode.playerx<mode.width*2/7+75) and (mode.height/6<mode.playery<mode.height/6+52):
                mode.app.hintAI.recordEnterTime('livingroom','table2')
                mode.app.setActiveMode(mode.app.table2Mode) 
        if (mode.width-30<mode.playerx<mode.width) and (mode.height*2/5<mode.playery<mode.height*3/5):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.kitchenMode)
        elif (mode.width*5/9<mode.playerx<mode.width*8/9) and (0<mode.playery<30):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.backyardMode)
        elif (0<mode.playerx<30) and (mode.height*2/7<mode.playery<mode.height*4/7):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.bedroomMode)
        if mode.app.welcomeMode.weapon == "knife" and mode.app.welcomeMode.location  == "livingroom":
            if (mode.width*4/5-10<mode.playerx<mode.width*4/5+10) and (mode.height/4-10<mode.playery<mode.height/4+10):
                mode.app.lewisStructureMode.chemicalCompound = "H2O2"
                mode.compound = "H2O2"
                mode.app.setActiveMode(mode.app.lewisStructureStartMode)

    def movePlayer(mode,dx,dy):
        mode.playerx += dx
        mode.playery += dy
        mode.makePlayerInteractive()

    def keyPressed(mode, event):
        if (event.key == 'Up' and mode.playery > 20): mode.movePlayer(0,-10)
        elif (event.key == 'Down' and mode.playery < mode.height-10): mode.movePlayer(0,10)
        elif (event.key == 'Left' and mode.playerx > 20): mode.movePlayer(-10,0)
        elif (event.key == 'Right' and mode.playerx < mode.width-10): mode.movePlayer(10,0)
        elif (event.key == 's'): mode.app.setActiveMode(mode.app.caseSolvedMode)
        elif (event.key == 'n'): 
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.hintCount += 1
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('livingroom',mode.complete,mode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)

        else: return

    def redrawAll(mode, canvas):
        # create using tkinter
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill='#8A3324')
        canvas.create_rectangle(mode.width*4/7,mode.height-30,mode.width*5/7,mode.height, fill='white')
        canvas.create_text(mode.width*9/14,mode.height-15, text='Front Door', font='Arial 16')
        canvas.create_rectangle(mode.width*5/9,0,mode.width*8/9,30, fill='white')
        canvas.create_text(mode.width*13/18,15, text='Backyard', font='Arial 16')
        canvas.create_rectangle(mode.width,mode.height*2/5,mode.width-30,mode.height*3/5, fill='white')
        canvas.create_text(mode.width-15,mode.height*1/2, text='K\ni\nt\nc\nh\ne\nn', font='Arial 15')
        canvas.create_rectangle(0,mode.height*2/7,30,mode.height*4/7, fill='white')
        canvas.create_text(15,mode.height*6/14, text='B\ne\nd\nr\no\no\nm', font='Arial 14')
        canvas.create_oval(mode.width*3/5-150,mode.height*1/2-150,mode.width*3/5+150,mode.height*1/2+150,fill = 'indigo')
        canvas.create_oval(mode.width*3/5-125,mode.height*1/2-125,mode.width*3/5+125,mode.height*1/2+125,fill = 'yellow')
        canvas.create_oval(mode.width*3/5-100,mode.height*1/2-100,mode.width*3/5+100,mode.height*1/2+100,fill = 'green')
        canvas.create_oval(mode.width*3/5-75,mode.height*1/2-75,mode.width*3/5+75,mode.height*1/2+75,fill = 'violet')
        canvas.create_oval(mode.width*3/5-50,mode.height*1/2-50,mode.width*3/5+50,mode.height*1/2+50,fill = 'orange')
        canvas.create_oval(mode.width*3/5-25,mode.height*1/2-25,mode.width*3/5+25,mode.height*1/2+25,fill = 'blue')
        if (mode.width/2-20<mode.playerx<mode.width/2+15) and (mode.height-40<mode.playery<mode.height):
            canvas.create_rectangle(mode.width/2+15,mode.height-60,mode.width/2+58,mode.height-45,fill='gray',outline='white')
            canvas.create_text(mode.width/2+38,mode.height-53,text='Meow!')
        elif (mode.width*3/5-25<mode.playerx<mode.width*3/5+25) and (mode.height*1/2-25<mode.playery<mode.height*1/2+25):
            canvas.create_rectangle(mode.width*3/5-110,mode.height/2+10,mode.width*3/5+110,mode.height/2+30,fill='gray',outline='white')
            canvas.create_text(mode.width*3/5,mode.height/2+20,text='Nothing special, just a colorful rug!')
        if mode.app.easyMode == True:
            if mode.app.secCount <= 5 and mode.app.minCount==mode.app.hourCount==0:
                canvas.create_text(mode.width/2,mode.height/5,text="Press 'h' for hints!",fill='yellow',font='Arial 18 bold')
                if mode.app.secCount%2 == 0:
                    canvas.create_text(mode.width/2,mode.height/5,text="Press 'h' for hints!",fill='red',font='Arial 20')
                
        #create image
        canvas.create_image(mode.width/7,mode.height*3/5, image=ImageTk.PhotoImage(mode.sofa))   
        canvas.create_image(mode.width*2/7,mode.height*4/5, image=ImageTk.PhotoImage(mode.sofa2))
        canvas.create_image(mode.width*2/15,mode.height-20, image=ImageTk.PhotoImage(mode.tv))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['tvMode']:
                canvas.create_image(mode.width*2/15,mode.height-20, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*2/15,mode.height-20, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width/7,mode.height*4/5, image=ImageTk.PhotoImage(mode.table))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['table1Mode']:
                canvas.create_image(mode.width/7,mode.height*4/5, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width/7,mode.height*4/5, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width-28,mode.height-55, image=ImageTk.PhotoImage(mode.workdesk))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['computerMode']:
                canvas.create_image(mode.width-28,mode.height-55, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width-28,mode.height-55, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width*2/7,mode.height/6, image=ImageTk.PhotoImage(mode.table2))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['table2Mode']:
                canvas.create_image(mode.width*2/7,mode.height/6, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*2/7,mode.height/6, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width*2/9, mode.height/3, image=ImageTk.PhotoImage(mode.chair))
        canvas.create_image(mode.width*3/9, mode.height/3, image=ImageTk.PhotoImage(mode.chair))
        canvas.create_image(mode.width*2/12, mode.height/7, image=ImageTk.PhotoImage(mode.chair2))
        canvas.create_image(mode.width/2,mode.height-20, image=ImageTk.PhotoImage(mode.rug))
        canvas.create_image(mode.width/2,mode.height-20, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width*3/5,mode.height/2, image=ImageTk.PhotoImage(mode.questionmark))
        if mode.app.welcomeMode.location  == 'livingroom' and mode.app.welcomeMode.weapon == "knife":
            canvas.create_image(mode.width*4/5,mode.height/4, image=ImageTk.PhotoImage(mode.questionmark))

        #player
        canvas.create_oval(mode.playerx-10,mode.playery-10,mode.playerx+10,mode.playery+10,fill='black')     

        #timer:
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

# interactive screens in livingroom:
########################################################
class tvMode(Mode):
    def appStarted(mode):
        mode.app.livingRoomMode.complete += 1
        mode.app.checkpoint += 1

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        else: return

    def mousePressed(mode,event):
        if (mode.width*3/5<event.x<mode.width*4/5) and (mode.height/2<event.y<mode.height*3/4):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif(mode.width/5<event.x<mode.width*2/5) and (mode.height/2<event.y<mode.height*3/4):
            mode.app.setActiveMode(mode.app.tvSubMode)

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height, fill='black')
        canvas.create_text(mode.width/2,mode.height/4,text='Tv is currently off. Do you want to turn it on?',font='Arial 26 bold', fill='white')
        canvas.create_rectangle(mode.width/5,mode.height/2,mode.width*2/5,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width*3/10,mode.height*5/8,text='Yes',font='Arial 26')
        canvas.create_rectangle(mode.width*3/5,mode.height/2,mode.width*4/5,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width*7/10,mode.height*5/8,text='No',font='Arial 26')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class tvSubMode(Mode):
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.livingRoomMode.hintCount += 1
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('livingroom',mode.app.livingRoomMode.complete,mode.app.livingRoomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height, fill='black')
        canvas.create_text(mode.width/2,mode.height/2,text='There is nothing special about the channels.\nBut digging through the watching history you found \neveryday at 3 pm someone in the house watches the \nweather report.',font='Arial 26 bold', fill='white')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class computerMode(Mode):
    def appStarted(mode):
        mode.app.livingRoomMode.complete += 1
        mode.app.checkpoint += 1
        mode.computerLockRaw = mode.loadImage('lockscreen.png')
        mode.computerLock = mode.scaleImage(mode.computerLockRaw,1/2)
        mode.hintPage = False

    def mousePressed(mode,event):
        possiblePassward = ['OYGBIV','VIBGYO']
        correct = random.choice(possiblePassward)
        passward = mode.getUserInput('Enter 6 digit passward')
        if (passward == None):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif(passward == correct) or (passward == correct.lower()):
            mode.app.setActiveMode(mode.app.desktopMode)
        else:
            mode.hintPage = True
            
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.livingRoomMode.hintCount += 1
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('livingroom',mode.app.livingRoomMode.complete,mode.app.livingRoomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2, image=ImageTk.PhotoImage(mode.computerLock))
        canvas.create_rectangle(mode.width/2-80,mode.height/2+30,mode.width/2+80,mode.height/2+60,fill='lightgray',outline='white')
        canvas.create_text(mode.width/2,mode.height/2+45,text='Click to enter password!',font='Arial 12')
        if mode.hintPage == True:
            canvas.create_rectangle(mode.width/2-80,mode.height/2+30,mode.width/2+80,mode.height/2+60,fill='lightgray',outline='white')
            canvas.create_text(mode.width/2,mode.height/2+45,text='Hint: Secret of the rug!',font='Arial 12')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class desktopMode(Mode):
    def appStarted(mode):
        mode.desktopRaw = mode.loadImage('desktop.png')
        mode.desktop = mode.scaleImage(mode.desktopRaw,5/11)   

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2, image=ImageTk.PhotoImage(mode.desktop))
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class table1Mode(Mode):
    def appStarted(mode):
        mode.app.livingRoomMode.complete += 1
        mode.app.checkpoint += 1

    def mousePressed(mode,event):
        if (mode.width*3/5<event.x<mode.width*4/5) and (mode.height/2<event.y<mode.height*3/4):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif(mode.width/5<event.x<mode.width*2/5) and (mode.height/2<event.y<mode.height*3/4):
            mode.app.setActiveMode(mode.app.notesMode)
    
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width, mode.height,fill='white')
        for n in range(1,13):
            canvas.create_line(0,mode.height*n/12,mode.width,mode.height*n/12)
        canvas.create_text(mode.width/2,mode.height/4,text ='You found a paper that has nothing written on it.\nDo you want to investigate more?',font='Arial 26 bold')
        canvas.create_rectangle(mode.width/5,mode.height/2,mode.width*2/5,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width*3/10,mode.height*5/8,text='Yes',font='Arial 26')
        canvas.create_rectangle(mode.width*3/5,mode.height/2,mode.width*4/5,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width*7/10,mode.height*5/8,text='No',font='Arial 26')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold')

class notesMode(Mode):
    def appStarted(mode):
        mode.message = 'Click the mouse to enter your action!'
        mode.secret = False

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.livingRoomMode.hintCount += 1
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('livingroom',mode.app.livingRoomMode.complete,mode.app.livingRoomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def mousePressed(mode,event):
        action = mode.getUserInput('What are you going to do?')
        if (action == None):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif ('sunlight'in action) or ('sun' in action) or ('UVlight' in action):
            mode.message = (f"{mode.app.welcomeMode.code}")
        else:
            mode.message = "Nothing is happening, maybe it's just piece of paper."

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
        for n in range(1,13):
            canvas.create_line(0,mode.height*n/12,mode.width,mode.height*n/12)
        canvas.create_text(mode.width/2,mode.height/2,text=mode.message,font='Arial 26 bold')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold')

class table2Mode(Mode):
    def appStarted(mode):
        mode.app.livingRoomMode.complete += 1
        mode.app.checkpoint += 1
        mode.app.currentMode = mode.app.livingRoomMode
        mode.burgerRaw = mode.loadImage('burger.png')
        mode.burger = mode.scaleImage(mode.burgerRaw, 5/7)
        mode.researchPage = False

    def mousePressed(mode,event):
        if (mode.width*3/4<event.x<mode.width*11/12) and (mode.height/2<event.y<mode.height*3/4):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif(mode.width/12<event.x<mode.width/4) and (mode.height/2<event.y<mode.height*3/4):
            mode.researchPage = True
            if mode.app.welcomeMode.weapon == 'GHB':
                mode.app.lewisStructureMode.chemicalComound = "C4H8O3"
                mode.app.setActiveMode(mode.app.lewisStructureStartMode)

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.livingRoomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.livingRoomMode.hintCount += 1
            mode.app.currentMode = mode.app.livingRoomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('livingroom',mode.app.livingRoomMode.complete,mode.app.livingRoomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='brown')
        canvas.create_image(mode.width/2,mode.height*3/5, image=ImageTk.PhotoImage(mode.burger))
        canvas.create_text(mode.width/2,mode.height/4,text="Uhmmm! unfinished burger, are you going \nto anaylze the burger?",font='Arial 24 bold')
        canvas.create_rectangle(mode.width/12,mode.height/2,mode.width/4,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width/6,mode.height*5/8,text='Yes',font='Arial 26')
        canvas.create_rectangle(mode.width*3/4,mode.height/2,mode.width*11/12,mode.height*3/4,fill='gray')
        canvas.create_text(mode.width*5/6,mode.height*5/8,text='No',font='Arial 26')
        if mode.researchPage == True:
            if mode.app.welcomeMode.weapon != 'GHB':
                canvas.create_rectangle(0,mode.height*9/20,mode.width,mode.height*11/20,fill='gray')
                canvas.create_text(mode.width/2,mode.height/2,text='Nothing special just a burger!',font='Arial 26')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')
