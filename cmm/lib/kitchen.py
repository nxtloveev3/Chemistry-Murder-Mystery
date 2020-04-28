from cmu_112_graphics import*
import random

#citation furniture images from https://www.clipart.email/download/1453998.html
#butler image from https://pixabay.com/illustrations/concierge-thei-japanese-business-1184853/
#newspaper image from https://thehungryjpeg.com/product/3627139-newspaper-with-coffee-cup-magazine-or-newspaper-press-cover-top-view
########################################################
#kitchen
class kitchenMode(Mode):
    def appStarted(mode):
        mode.app.currentMode = mode.app.kitchenMode
        mode.playerx = mode.width/20
        mode.playery = mode.height/2
        mode.rows = 15
        mode.cols = 40
        mode.dinningRaw = mode.loadImage('dinningTable.png')
        mode.dinning = mode.scaleImage(mode.dinningRaw,5/7)
        mode.stoveRaw = mode.loadImage('stove.png')
        mode.stove = mode.scaleImage(mode.stoveRaw,5/7)
        mode.sinkRaw = mode.loadImage('sink.png')
        mode.sink = mode.scaleImage(mode.sinkRaw,5/7)
        mode.counter = mode.loadImage('counter.png')
        mode.fridgeRaw = mode.loadImage('fridge.png')
        mode.fridge = mode.scaleImage(mode.fridgeRaw,1/2)
        mode.chairUp = mode.loadImage('chairUp.png')
        mode.chairLeft = mode.loadImage('chairLeft.png')
        mode.chairRight = mode.loadImage('chairRight.png')
        mode.questionmarkRaw = mode.loadImage('questionmark.png')
        mode.questionmark = mode.scaleImage(mode.questionmarkRaw, 1/25)
        mode.compound=None
        mode.hintCount = 0
        mode.complete = 0

    def makePlayerInteractive(mode):
        if mode.app.hardMode == True:
            if (mode.width*3/10-20<mode.playerx<mode.width*3/10+20) and (mode.height/2-20<mode.playery<mode.height/2+20) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect1Mode']:
                mode.app.setActiveMode(mode.app.suspect1Mode)
            elif (mode.width-80<mode.playerx<mode.width) and (mode.height/3-250<mode.playery<mode.height/3+250) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['counterMode']:
                mode.app.setActiveMode(mode.app.counterMode)
            elif (mode.width*3/7-60<mode.playerx<mode.width*3/7+60) and (mode.height*2/5-100<mode.playery<mode.height*2/5+100) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['dinningMode']:
                mode.app.setActiveMode(mode.app.dinningMode)
            elif (mode.width*23/28-60<mode.playerx<mode.width*23/28+60) and (0<mode.playery<mode.height/16+50) and mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['sinkMode']:
                mode.app.setActiveMode(mode.app.sinkMode)
                mode.app.playSound('sink')
        else:
            if (mode.width*3/10-20<mode.playerx<mode.width*3/10+20) and (mode.height/2-20<mode.playery<mode.height/2+20):
                mode.app.setActiveMode(mode.app.suspect1Mode)
            elif (mode.width-80<mode.playerx<mode.width) and (mode.height/3-250<mode.playery<mode.height/3+250):
                mode.app.hintAI.recordEnterTime('kitchen','counter')
                mode.app.setActiveMode(mode.app.counterMode)
            elif (mode.width*3/7-60<mode.playerx<mode.width*3/7+60) and (mode.height*2/5-100<mode.playery<mode.height*2/5+100):
                mode.app.hintAI.recordEnterTime('kitchen','dinning')
                mode.app.setActiveMode(mode.app.dinningMode)
            elif (mode.width*23/28-60<mode.playerx<mode.width*23/28+60) and (0<mode.playery<mode.height/16+50):
                mode.app.hintAI.recordEnterTime('kitchen','sink')
                mode.app.setActiveMode(mode.app.sinkMode)
                mode.app.playSound('sink')
        if (0<mode.playerx<mode.width/40) and (mode.height*2/5<mode.playery<mode.height*3/5):
            mode.app.playSound('door')
            mode.app.setActiveMode(mode.app.livingRoomMode)
        if mode.app.welcomeMode.weapon == "knife" and mode.app.welcomeMode.location  == "kitchen":
            if (mode.width*4/5-10<mode.playerx<mode.width*4/5+10) and (mode.height/4-10<mode.playery<mode.height/4+10):
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
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.hintCount += 1
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('kitchen',mode.complete,mode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill='white')
        for row in range(mode.rows):
            for col in range(mode.cols):
                if row == col:
                    canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk2')
                elif row < col:
                    if row == col-15:
                        canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk2')
                    elif row + col == 30:
                        canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk2')
                    else:
                        canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk3')
                elif (row+col) == 15:
                    canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk2')
                else:
                    canvas.create_rectangle(0+mode.width/mode.cols*col,0+mode.height/mode.rows*row,mode.width/mode.cols+mode.width/mode.cols*col,mode.height/mode.rows+mode.height/mode.rows*row,fill='cornsilk3')
        canvas.create_rectangle(0,mode.height*2/5,mode.width/40,mode.height*3/5,fill='white')
        canvas.create_text(15,mode.height/2,text='l\ni\nv\ni\nn\ng\nr\no\no\nm',font='Arial 10')
        canvas.create_image(mode.width*3/7,mode.height*2/5, image=ImageTk.PhotoImage(mode.dinning))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['dinningMode']:
                canvas.create_image(mode.width*3/7,mode.height*2/5, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*3/7,mode.height*2/5, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width*23/28,mode.height/16, image=ImageTk.PhotoImage(mode.sink))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['sinkMode']:
                canvas.create_image(mode.width*23/28,mode.height/16, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*23/28,mode.height/16, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width-30,mode.height/3, image=ImageTk.PhotoImage(mode.counter))
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['counterMode']:
                canvas.create_image(mode.width-30,mode.height/3, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width-30,mode.height/3, image=ImageTk.PhotoImage(mode.questionmark))
        canvas.create_image(mode.width-30,mode.height*7/8, image=ImageTk.PhotoImage(mode.fridge))
        canvas.create_image(mode.width*5/7,mode.height/13, image=ImageTk.PhotoImage(mode.stove))
        canvas.create_image(mode.width*3/7,mode.height*13/20, image=ImageTk.PhotoImage(mode.chairUp))
        canvas.create_image(mode.width*11/20,mode.height*5/16, image=ImageTk.PhotoImage(mode.chairLeft))
        canvas.create_image(mode.width*11/20,mode.height/2, image=ImageTk.PhotoImage(mode.chairLeft))
        canvas.create_image(mode.width*3/10,mode.height/2, image=ImageTk.PhotoImage(mode.chairRight))
        canvas.create_image(mode.width*3/10,mode.height*5/16, image=ImageTk.PhotoImage(mode.chairRight))
        if mode.app.welcomeMode.location  == 'kitchen' and mode.app.welcomeMode.weapon == "knife":
            canvas.create_image(mode.width*4/5,mode.height/4, image=ImageTk.PhotoImage(mode.questionmark))

        #suspect 1(Butler John Patrick)
        canvas.create_oval(mode.width*3/10-10,mode.height/2-10,mode.width*3/10+10,mode.height/2+10,fill='blue')
        if mode.app.hardMode == True:
            if mode.app.checkpoint >= mode.app.welcomeMode.checkpointList['suspect1Mode']:
                canvas.create_image(mode.width*3/10,mode.height/2, image=ImageTk.PhotoImage(mode.questionmark))
        else:
            canvas.create_image(mode.width*3/10,mode.height/2, image=ImageTk.PhotoImage(mode.questionmark))
        
        #player
        canvas.create_oval(mode.playerx-10,mode.playery-10,mode.playerx+10,mode.playery+10,fill='black')     

        #timer
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

#interactive screen in kitchen
########################################################
class dinningMode(Mode):
    def appStarted(mode):
        mode.app.kitchenMode.complete += 1
        mode.app.checkpoint += 1
        mode.newspaperRaw = mode.loadImage('newspaper.png')
        mode.newspaper = mode.scaleImage(mode.newspaperRaw,1/2)

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.kitchenMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.kitchenMode.hintCount += 1
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('kitchen',mode.app.kitchenMode.complete,mode.app.kitchenMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='salmon3')
        canvas.create_image(mode.width/2,mode.height/2, image=ImageTk.PhotoImage(mode.newspaper))
        canvas.create_rectangle(0,mode.height*9/20,mode.width,mode.height*11/20,fill='white')
        canvas.create_text(mode.width/2,mode.height/2,text='You found a newspaper report about STA pan customers \ncharge the company for unhealthy effect from using the non-sticking pan.',font='Arial 22')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class sinkMode(Mode):
    def appStarted(mode):
        mode.app.kitchenMode.complete += 1
        mode.app.checkpoint += 1
        mode.questionmarkRaw = mode.loadImage('questionmark.png')
        mode.questionmark = mode.scaleImage(mode.questionmarkRaw, 1/25)
        mode.bloodTest = False

    def mousePressed(mode,event):
        if (mode.width*3/4-40<event.x<mode.width*3/4+40) and (mode.height-70<event.y<mode.height-50):
            mode.bloodTest = True
        elif (mode.width*3/4-40<event.x<mode.width*3/4+40) and (mode.height-40<event.y<mode.height-20):
            mode.app.setActiveMode(mode.app.kitchenMode)

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.kitchenMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.kitchenMode.hintCount += 1
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('kitchen',mode.app.kitchenMode.complete,mode.app.kitchenMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='silver')
        canvas.create_oval(mode.width/2-50,mode.height/2-50,mode.width/2+50,mode.height/2+50,fill='black')
        canvas.create_line(mode.width/2-50,mode.height/2,mode.width/2+50,mode.height/2,fill='silver')
        canvas.create_line(mode.width/2,mode.height/2-50,mode.width/2,mode.height/2+50,fill='silver')
        if mode.app.welcomeMode.weapon == 'knife':
            canvas.create_image(mode.width/2-51,mode.height/2-51, image=ImageTk.PhotoImage(mode.questionmark))
            canvas.create_rectangle(0,mode.height*3/4,mode.width,mode.height,fill='gray',outline='white')
            canvas.create_text(mode.width/2,mode.height*4/5,text='You found some light redness on the rim of the drain.',font='Arial 24')
            canvas.create_text(mode.width*3/4,mode.height-60, text='Quick, investigate the red substence.',font='Arial 18',fill='orange')
            canvas.create_text(mode.width*3/4,mode.height-30, text="Hummm, it's probably just ketchup. :)" ,font='Arial 18',fill='orange')
        else:
            canvas.create_text(mode.width/2,mode.height/5,text='Seems like just a normal sink.',font='Arial 26')
        if mode.bloodTest == True:
            if mode.app.welcomeMode.killer != 'Molly Barnett':
                canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
                canvas.create_text(mode.width/2,mode.height/2,text="The result shows that it's actually indeed blood. \nHowever, it's not Nico's blood but belong to a male.",font='Arial 26 bold')
            else:
                canvas.create_rectangle(0,0,mode.width,mode.height,fill='white')
                canvas.create_text(mode.width/2,mode.height/2,text="The result shows that it's actually indeed blood. \nHowever, it's not Nico's blood but belong to a female.",font='Arial 26 bold')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

class counterMode(Mode):
    def appStarted(mode):
        mode.app.kitchenMode.complete += 1
        mode.app.checkpoint += 1
        mode.cols=random.randint(3,6)
        mode.rows=random.randint(2,3)
        mode.drawer=False
        mode.font=int(24*mode.findportion())
        mode.portion=int(1/mode.findportion())
        mode.col=random.randint(1,mode.cols)
        mode.row=random.randint(1,mode.rows)
        mode.x,mode.y = mode.drawingCord(mode.width/mode.cols*(mode.col-1),mode.width/mode.cols*mode.col,mode.height/mode.rows*(mode.row-1),mode.height/mode.rows*mode.row)
        print(mode.col,mode.row)

    def findportion(mode):
        portion=(mode.width/mode.cols)/(mode.width/3)
        return portion
    
    def mousePressed(mode,event):
        if (mode.width/mode.cols*(mode.col-1)<event.x<mode.width/mode.cols*mode.col) and (mode.height/mode.rows*(mode.row-1)<event.y<mode.height/mode.rows*mode.row):
            mode.drawer=True        

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.kitchenMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        elif (event.key == 'h') and mode.app.easyMode == True: 
            mode.app.kitchenMode.hintCount += 1
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.hintAI.hint = mode.app.hintAI.determineHintMessage('kitchen',mode.app.kitchenMode.complete,mode.app.kitchenMode.hintCount)
            mode.app.setActiveMode(mode.app.hintAI)
        else: return

    def drawingCord(mode,x1,x2,y1,y2):
        x = (x1+x2)/2
        y = (y1+y2)/2
        return (x,y)
    
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='sandy brown')
        for row in range(mode.rows):
            for col in range(mode.cols):
                canvas.create_line(0,mode.height/mode.rows*row,mode.width,mode.height/mode.rows*row,fill='salmon4')
                canvas.create_line(mode.width/mode.cols*col,0,mode.width/mode.cols*col,mode.height,fill='salmon4')
                canvas.create_oval((mode.width/mode.cols*col+mode.width/mode.cols*(col+1))/2-20*mode.portion,(mode.height/mode.rows*row+mode.height/mode.rows*(row+1))/2-20*mode.portion,(mode.width/mode.cols*col+mode.width/mode.cols*(col+1))/2+20*mode.portion,(mode.height/mode.rows*row+mode.height/mode.rows*(row+1))/2+20*mode.portion,fill='gainsboro')
        if mode.drawer==True:
            canvas.create_rectangle(mode.width/mode.cols*(mode.col-1),mode.height/mode.rows*(mode.row-1),mode.width/mode.cols*mode.col,mode.height/mode.rows*mode.row,fill='gray')
            if mode.app.welcomeMode.weapon=='knife':
                canvas.create_text(mode.x,mode.y,text='You found a large knife \nmissing in the sets',font=f'Arial {mode.font}')
            elif mode.app.welcomeMode.weapon=='GHB':
                canvas.create_text(mode.x,mode.y,text='You found suspecious \ndrug called GHB',font=f'Arial {mode.font}')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

