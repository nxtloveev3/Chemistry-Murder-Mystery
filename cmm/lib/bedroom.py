from cmu_112_graphics import *

#citation tv image from https://www.clipart.email/download/1453998.html
#furniture images from https://www.shutterstock.com/image-vector/icons-set-interior-furniture-top-view-699488854
# pillow images from https://www.overstock.com/guides/how-to-arrange-pillows-on-a-bed
########################################################
#bedroom
class bedroomMode(Mode):
    def appStarted(mode):
        mode.app.currentMode = mode.app.bedroomMode
        mode.playerx=mode.width*19/20
        mode.playery=mode.height*6/14
        mode.bedRaw=mode.loadImage('bed.png')
        mode.bed=mode.scaleImage(mode.bedRaw,5/4)
        mode.tv=mode.loadImage('tv2.png')
        mode.chairRightRaw=mode.loadImage('chairRight.png')
        mode.chairRight=mode.scaleImage(mode.chairRightRaw,3/2)
        mode.chairLeftRaw=mode.loadImage('chairLeft.png')
        mode.chairLeft=mode.scaleImage(mode.chairLeftRaw,3/2)
        mode.questionmarkRaw=mode.loadImage('questionmark.png')
        mode.questionmark=mode.scaleImage(mode.questionmarkRaw,1/25)
        mode.compound = None
        mode.hintCount = 0
        mode.complete = 0

    def makePlayerInteractive(mode):
        if mode.app.hardMode == True:
            if (mode.width*5/6-20<mode.playerx<mode.width*5/6+20) and (mode.height*5/6-20<mode.playery<mode.height*5/6+20) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect2Mode']:
                mode.app.setActiveMode(mode.app.suspect2Mode)
            elif (mode.width/2-40<mode.playerx<mode.width/2+40) and (mode.height-30<mode.playery<mode.height) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['tvDrawerMode']:
                mode.app.playSound('drawer')
                mode.app.setActiveMode(mode.app.tvDrawerMode)
            elif (mode.width*3/8<mode.playerx<mode.width*5/8) and (0<mode.playery<mode.height/2) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['bedMode']:
                mode.app.setActiveMode(mode.app.bedMode)
        else:
            if (mode.width*5/6-20<mode.playerx<mode.width*5/6+20) and (mode.height*5/6-20<mode.playery<mode.height*5/6+20):
                mode.app.setActiveMode(mode.app.suspect2Mode)
            elif (mode.width/2-40<mode.playerx<mode.width/2+40) and (mode.height-30<mode.playery<mode.height):
                mode.app.hintAI.recordEnterTime('bedroom','tvDrawer')
                mode.app.playSound('drawer')
                mode.app.setActiveMode(mode.app.tvDrawerMode)
            elif (mode.width*3/8<mode.playerx<mode.width*5/8) and (0<mode.playery<mode.height/2):
                mode.app.hintAI.recordEnterTime('bedroom','bed')
                mode.app.setActiveMode(mode.app.bedMode)
        if (mode.width*77/80<mode.playerx<mode.width) and (mode.height*2/7<mode.playery<mode.height*4/7):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.livingRoomMode)
        if mode.app.welcomeMode.weapon == "knife" and mode.app.welcomeMode.location  == "bedroom":
            if (mode.width*4/5-20<mode.playerx<mode.width*4/5+20) and (mode.height/4-20<mode.playery<mode.height/4+20):
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
        elif (event.key == 'n'): mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.hintCount += 1
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('bedroom',mode.complete,mode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill='#FFE4C4')
        canvas.create_rectangle(mode.width*77/80,mode.height*2/7,mode.width,mode.height*4/7,fill='white')
        canvas.create_text(mode.width-15,mode.height*3/7,text='l\ni\nv\ni\nn\ng\nr\no\no\nm')
        canvas.create_image(mode.width/2,mode.height-450, image=ImageTk.PhotoImage(mode.bed))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['bedMode']:
                canvas.create_image(mode.width/2,mode.height-450, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width/2,mode.height-450, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width/2,mode.height-20, image=ImageTk.PhotoImage(mode.tv))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['tvDrawerMode']:
                canvas.create_image(mode.width/2,mode.height-20, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width/2,mode.height-20, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width/6,mode.height*5/6, image=ImageTk.PhotoImage(mode.chairRight))
        canvas.create_image(mode.width/6,mode.height*5/6, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width*5/6,mode.height*5/6, image=ImageTk.PhotoImage(mode.chairLeft))
        if mode.app.welcomeMode.location  == 'bedroom' and mode.app.welcomeMode.weapon == "knife":
            canvas.create_image(mode.width*4/5,mode.height/4, image=ImageTk.PhotoImage(mode.questionmark))
        if (mode.width/6-50<mode.playerx<mode.width/6+50) and (mode.height*5/6-50<mode.playery<mode.height*5/6+50):
            if mode.app.welcomeMode.location == "bedroom" and mode.app.welcomeMode.killer != "Molly Bernett":
                canvas.create_rectangle(mode.width/6-100,mode.height*5/6-20,mode.width/6+150,mode.height*5/6,fill="gray")
                canvas.create_text(mode.width/6+25,mode.height*5/6-10,text=f"You found a hair belong to {mode.app.welcomeMode.killer}")
            else:
                canvas.create_rectangle(mode.width/6-80,mode.height*5/6-20,mode.width/6+120,mode.height*5/6,fill="gray")
                canvas.create_text(mode.width/6+25,mode.height*5/6-10,text="You found some Molly's hair")  

        #Suspect2
        canvas.create_oval(mode.width*5/6-20,mode.height*5/6-20,mode.width*5/6+20,mode.height*5/6+20,fill='red')
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect2Mode']:
                canvas.create_image(mode.width*5/6,mode.height*5/6, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*5/6,mode.height*5/6, image=ImageTk.PhotoImage(mode.questionmark))

        #player
        canvas.create_oval(mode.playerx-20,mode.playery-20,mode.playerx+20,mode.playery+20,fill='black')     

        #timer
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold')

#interactive screen in bedroom
########################################################
class tvDrawerMode(Mode):
    def appStarted(mode):
        mode.app.bedroomMode.complete += 1
        mode.app.checkpoint += 1
        mode.passward = '1122'
        mode.userInput = [0,0,0,0]
        mode.input = ''

    def mousePressed(mode,event):
        information = mode.getUserInput('Enter Digit')
        for n in range(4):
            if (mode.width/5*(n+1)-30<event.x<mode.width/5*(n+1)+30) and (mode.height/2-40<event.y<mode.height/2+40):
                if (information != None) and (len(information) < 2) and information.isdigit:
                    mode.userInput[n] = information
                elif information == None:
                    mode.app.setActiveMode(mode.app.tvDrawerMode)
                else: 
                    mode.mousePressed(event) 
            
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.bedroomMode)
        elif(event.key == 'Enter'):
            for elem in mode.userInput:
                mode.input += str(elem)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.bedroomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.bedroomMode.hintCount += 1
            mode.app.currentMode = mode.app.bedroomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('bedroom',mode.app.bedroomMode.complete,mode.app.bedroomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas): 
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="orange")
        canvas.create_rectangle(mode.width/8,mode.height/6,mode.width*7/8,mode.height*5/6,fill='gray')
        canvas.create_text(mode.width/2,mode.height/8,text="You found a safe box.Press 'Enter' to open.",font="Arial 24 bold")
        for n in range(1,5):
            canvas.create_rectangle(mode.width/5*n-30,mode.height/2-40,mode.width/5*n+30,mode.height/2+40,fill='white')
        for i in range(4):   
            canvas.create_text(mode.width/5*(i+1),mode.height/2,text =f'{mode.userInput[i]}',font='Arial 26 bold')
        if mode.passward == mode.input:
            canvas.create_rectangle(0,0,mode.width,mode.height,fill="gray")
            canvas.create_rectangle(mode.width/8,mode.height/6,mode.width*7/8,mode.height*5/6,fill="white")
            canvas.create_text(mode.width/2,mode.height/2,text="You found a lot of documents\nthat is pointing the STA company \nhas been selling unhealthy pans that \ncould cause cancer.",font="Arial 22 bold")
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class bedMode(Mode):
    def appStarted(mode):
        mode.app.bedroomMode.complete += 1
        mode.app.checkpoint += 1
        mode.bedImageRaw = mode.loadImage("bedImage.png")
        mode.bed = mode.scaleImage(mode.bedImageRaw,1/2)
        mode.mouseX = 0
        mode.mouseY = 0
        mode.grayPillow = False
        mode.whitePillow = False
        mode.sheet = False

    def mousePressed(mode,event):
        mode.mouseX = event.x
        mode.mouseY = event.y
        if (mode.width/4<event.x<mode.width*3/4) and (mode.height/2-80<event.y<mode.height/2-40):
            mode.grayPillow = True
            mode.whitePillow = False
            mode.sheet = False
        elif (mode.width/4<event.x<mode.width*3/4) and (mode.height/2-40<event.y<mode.height/2):
            mode.whitePillow = True
            mode.grayPillow = False
            mode.sheet = False
        elif (mode.width/4<event.x<mode.width*3/4) and (mode.height/2+20<event.y<mode.height*3/4):
            mode.whitePillow = False
            mode.grayPillow = False
            mode.sheet = True

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.bedroomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.bedroomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.bedroomMode.hintCount += 1
            mode.app.currentMode = mode.app.bedroomMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('bedroom',mode.app.bedroomMode.complete,mode.app.bedroomMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="#FFE4C4")
        canvas.create_image(mode.width/2,mode.height/2, image=ImageTk.PhotoImage(mode.bed))
        canvas.create_text(mode.width/2,mode.height-40,text="Use your mouse to investigate.",font="Arial 18 bold")
        if mode.mouseX != 0 and mode.mouseY != 0:
            if mode.whitePillow == True:
                canvas.create_line(mode.mouseX,mode.mouseY,mode.width*17/20,mode.height*11/120)
                if mode.app.welcomeMode.weapon == "pillow" and mode.app.welcomeMode.location == "backyard":
                    canvas.create_rectangle(mode.width*3/4,10,mode.width-40,mode.height/4,fill='gray')
                    canvas.create_text(mode.width*17/20,mode.height*11/120,text="One pillow has a fade \nwet spot and some \ndirt on the edge.")
                elif mode.app.welcomeMode.weapon == "pillow" and mode.app.welcomeMode.location == "livingroom":
                    canvas.create_rectangle(mode.width*3/4,10,mode.width-40,mode.height/4,fill='gray')
                    canvas.create_text(mode.width*17/20,mode.height*11/120,text="One pillow has a fade \nwet spot and some \nrug fiber on the edge.")
                elif mode.app.welcomeMode.weapon == "pillow" and mode.app.welcomeMode.location == "kitchen":
                    canvas.create_rectangle(mode.width*3/4,10,mode.width-40,mode.height/4,fill='gray')
                    canvas.create_text(mode.width*17/20,mode.height*11/120,text="One pillow has a fade \nwet spot and smells \nlike spices.")
                elif mode.app.welcomeMode.weapon == "pillow":
                    canvas.create_rectangle(mode.width*3/4,10,mode.width-40,mode.height/4,fill='gray')
                    canvas.create_text(mode.width*17/20,mode.height*11/120,text="One pillow has a fade \nwet spot.")
                else:
                    canvas.create_rectangle(mode.width*3/4,10,mode.width-40,mode.height/4,fill='gray')
                    canvas.create_text(mode.width*17/20,mode.height*11/120,text="Fruity flavor shampoo!")
            elif mode.grayPillow == True:
                canvas.create_line(mode.mouseX,mode.mouseY,mode.width*7/80,mode.height/4)
                canvas.create_rectangle(10,mode.height/6,mode.width/6,mode.height*2/6,fill='gray')
                canvas.create_text(mode.width*7/80,mode.height/4,text="Smell of shampoo.\nNothing Special")
            elif mode.sheet == True:
                canvas.create_line(mode.mouseX,mode.mouseY,mode.width*77/80,mode.height*8/9)
                if mode.app.welcomeMode.weapon == "knife" and mode.app.welcomeMode.location == "bedroom":
                    canvas.create_rectangle(mode.width*5/6,mode.height*5/6,mode.width-20,mode.height-20,fill='gray')
                    canvas.create_text(mode.width*77/80,mode.height*8/9,text="Fresh sheet \nsmells good.")
                else:
                    canvas.create_rectangle(mode.width*5/6,mode.height*5/6,mode.width-20,mode.height-20,fill='gray')
                    canvas.create_text(mode.width*73/80,mode.height*8/9,text="Wrinkles, smells \nOkkk not great.")
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold')
