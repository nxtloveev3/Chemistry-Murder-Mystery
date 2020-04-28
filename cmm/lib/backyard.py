from cmu_112_graphics import *

#citation backyard image used from https://www.clipart.email/download/1453998.html
# nico image from https://www.pinclipart.com/pindetail/iTiiRwR_call-3231-tied-up-man-cartoon-clipart/
########################################################
#backyard
class backyardMode(Mode):
    def appStarted(mode):
        mode.app.currentMode = mode.app.backyardMode
        mode.playerx=mode.width*13/18
        mode.playery=mode.height*14/15
        mode.outsideChairRaw = mode.loadImage('outdoorChair.png')
        mode.outsideChair = mode.scaleImage(mode.outsideChairRaw,1/2)
        mode.questionmarkRaw = mode.loadImage('questionmark.png')
        mode.questionmark = mode.scaleImage(mode.questionmarkRaw, 1/25)
        mode.compound = None
        mode.hintCount = 0
        mode.complete = 0
        
    def makePlayerInteractive(mode):
        if mode.app.hardMode == True:
            if (mode.width*3/4-10<mode.playerx<mode.width*3/4+10) and (mode.height/3-10<mode.playery<mode.height/3+10) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect3Mode']:
                mode.app.setActiveMode(mode.app.suspect3Mode)
            elif (0<mode.playerx<mode.width/3) and (mode.height*2/3<mode.playery<mode.height) and mode.app.checkpoint == mode.app.welcomeMode.checkpointList['storageMode']:
                mode.app.playSound('door')
                mode.app.setActiveMode(mode.app.storageMode)
        else:
            if (mode.width*3/4-10<mode.playerx<mode.width*3/4+10) and (mode.height/3-10<mode.playery<mode.height/3+10):
                mode.app.setActiveMode(mode.app.suspect3Mode)
            elif (0<mode.playerx<mode.width/3) and (mode.height*2/3<mode.playery<mode.height):
                mode.app.playSound('door')
                mode.app.hintAI.recordEnterTime('backyard','storage')
                mode.app.setActiveMode(mode.app.storageMode)
        if (mode.width*5/9<mode.playerx<mode.width*8/9) and (mode.height*19/20<mode.playery<mode.height):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.livingRoomMode)
        if mode.app.welcomeMode.weapon == "knife" and mode.app.welcomeMode.location  == "backyard":
            if (mode.width/2-20<mode.playerx<mode.width/2+20) and (mode.height*3/4-20<mode.playery<mode.height*3/4+20):
                mode.app.lewisStructureMode.chemicalCompound = "H2O2"
                mode.compound = "H2O2"
                mode.app.setActiveMode(mode.app.lewisStructureStartMode)

    def movePlayer(mode,dx,dy):
        mode.playerx += dx
        mode.playery += dy
        mode.makePlayerInteractive()

    def keyPressed(mode, event):
        if (event.key == 'Up' and mode.playery > 20): mode.movePlayer(0,-30)
        elif (event.key == 'Down' and mode.playery < mode.height-10): mode.movePlayer(0,30)
        elif (event.key == 'Left' and mode.playerx > 20): mode.movePlayer(-30,0)
        elif (event.key == 'Right' and mode.playerx < mode.width-10): mode.movePlayer(30,0)
        elif (event.key == 's'): mode.app.setActiveMode(mode.app.caseSolvedMode)
        elif (event.key == 'n'): 
            mode.app.currentMode = mode.app.backyardMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.hintCount += 1
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('backyard',mode.complete,mode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill='green')
        canvas.create_rectangle(mode.width*5/9,mode.height*19/20,mode.width*8/9,mode.height,fill='white')
        canvas.create_text(mode.width*13/18,mode.height*39/40,text='livingroom')
        canvas.create_rectangle(0,mode.height*2/3,mode.width/3,mode.height,fill='peachpuff4')
        canvas.create_text(mode.width/6,mode.height*5/6,text='Storage')
        if mode.app.hardMode == True:
            if mode.app.checkpoint == mode.app.welcomeMode.checkpointList['storageMode']:
                canvas.create_image(mode.width/6,mode.height*3/4, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width/6,mode.height*3/4, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width/4,mode.height/3, image=ImageTk.PhotoImage(mode.outsideChair))
        canvas.create_image(mode.width*3/4,mode.height/3, image=ImageTk.PhotoImage(mode.outsideChair))
        canvas.create_image(mode.width/2,mode.height/3, image=ImageTk.PhotoImage(mode.outsideChair))
        if mode.app.welcomeMode.location  == 'backyard' and mode.app.welcomeMode.weapon == "knife":
            canvas.create_image(mode.width/2,mode.height*3/4, image=ImageTk.PhotoImage(mode.questionmark))

        #suspect3
        canvas.create_oval(mode.width*3/4-10,mode.height/3-10,mode.width*3/4+10,mode.height/3+10,fill='green')
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect3Mode']:  
                canvas.create_image(mode.width*3/4,mode.height/3, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*3/4,mode.height/3, image=ImageTk.PhotoImage(mode.questionmark))

        #player
        canvas.create_oval(mode.playerx-10,mode.playery-10,mode.playerx+10,mode.playery+10,fill='black')     

        #timer
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

#interactive screen in backyard
########################################################
class storageMode(Mode):
    def appStarted(mode):
        mode.app.backyardMode.complete += 1
        mode.passward = mode.app.welcomeMode.code
        mode.userInput = [0,0,0,0,0,0]
        mode.input = ''

    def mousePressed(mode,event):
        information = mode.getUserInput('Enter Digit')
        for n in range(6):
            if (mode.width/7*(n+1)-20<event.x<mode.width/7*(n+1)+20) and (mode.height/2-30<event.y<mode.height/2+30):
                if (information != None) and (len(information) < 2) and information.isdigit:
                    mode.userInput[n] = information
                elif information == None:
                    mode.app.setActiveMode(mode.app.backyardMode)
                else: 
                    mode.mousePressed(event) 
            
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.backyardMode)
        elif(event.key == 'Enter'):
            for elem in mode.userInput:
                mode.input += str(elem)
            if mode.passward == mode.input:
                mode.app.setActiveMode(mode.app.nicoMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.backyardMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.backyardMode.hintCount += 1
            mode.app.currentMode = mode.app.backyardMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('backyard',mode.app.backyardMode.complete,mode.app.backyardMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return
    
    def redrawAll(mode,canvas): 
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="brown")
        canvas.create_rectangle(mode.width/10,mode.height/2-50,mode.width*9/10,mode.height/2+50,fill='gray')
        canvas.create_text(mode.width/2,mode.height/8,text="You found a lock. Press 'Enter' to open.",font="Arial 24 bold")
        for n in range(1,7):
            canvas.create_rectangle(mode.width/7*n-20,mode.height/2-30,mode.width/7*n+20,mode.height/2+30,fill='white')
        for i in range(6):   
            canvas.create_text(mode.width/7*(i+1),mode.height/2,text =f'{mode.userInput[i]}',font='Arial 24 bold')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')
