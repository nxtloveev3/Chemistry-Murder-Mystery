from cmu_112_graphics import*
from lib.conversation import*

# citation image adopted from https://pixabay.com/illustrations/concierge-thei-japanese-business-1184853/
########################################################
#suspect 1

class suspect1Mode(Mode):
    def appStarted(mode):
        mode.app.checkpoint += 1
        mode.butlerRaw = mode.loadImage('butler.png')
        mode.butler = mode.scaleImage(mode.butlerRaw, 1/2)
        mode.x,mode.y=mode.textlocation(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3)
        mode.response = None
        if mode.app.welcomeMode.killer == 'John Patrick':
            mode.nervous = True
        else: mode.nervous = False

    def textlocation(mode,x,y,x1,y1):
        xLoc=(x+x1)/2
        yLoc=(y+y1)/2
        return (xLoc,yLoc)

    def mousePressed(mode,event):
        mode.question = mode.getUserInput('Your question')
        if mode.question != None:
            mode.response = conversationGeneration(mode.question,mode.app.welcomeMode.weapon,mode.nervous)
        else:
            mode.app.setActiveMode(mode.app.kitchenMode)

    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.kitchenMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.kitchenMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='lightgray')
        canvas.create_rectangle(0,mode.height*3/5,mode.width,mode.height,fill='cornsilk2',outline='white')
        canvas.create_image(mode.width/7,mode.height/2, image=ImageTk.PhotoImage(mode.butler))
        canvas.create_rectangle(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3,fill='white')
        canvas.create_text(mode.width/2,mode.height*5/6,text='Click to interact with him.',font='Arial 22 bold')
        if mode.response == None:
            canvas.create_text(mode.x,mode.y,text="Hi, detective. My Name is John Patrick. \nI worked for Nico for roughly 2 months. \nWhen he went missing I was working in the kitchen.\nWhat can I help you?",font='Arial 18')
        else:
            canvas.create_text(mode.x,mode.y,text=f'{mode.response}',font='Arial 22')
        if mode.app.welcomeMode.weapon == 'knife' and mode.nervous == True:
            canvas.create_text(mode.width/3,mode.height*2/3,text='You noticed a fresh cut on his hand') 
        elif mode.app.welcomeMode.weapon == 'pillow' and mode.nervous == True:
            canvas.create_text(mode.width/3,mode.height*2/3,text='You noticed multiple red bruise on his arm') 
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

# citation image adopted from https://www.pngfind.com/mpng/hmhxwo_free-png-download-angry-woman-animated-gif-png/
########################################################
#suspect 2
class suspect2Mode(Mode):
    def appStarted(mode):
        mode.app.checkpoint += 1
        mode.wifeRaw = mode.loadImage('woman.png')
        mode.wife = mode.scaleImage(mode.wifeRaw, 1/2)
        mode.x,mode.y=mode.textlocation(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3)
        mode.response = None
        if mode.app.welcomeMode.killer == 'Molly Barnett':
            mode.nervous = True
        else: mode.nervous = False

    def textlocation(mode,x,y,x1,y1):
        xLoc=(x+x1)/2
        yLoc=(y+y1)/2
        return (xLoc,yLoc)

    def mousePressed(mode,event):
        mode.question = mode.getUserInput('Your question')
        if mode.question != None:
            mode.response = conversationGeneration(mode.question,mode.app.welcomeMode.weapon,mode.nervous)
        else:
            mode.app.setActiveMode(mode.app.bedroomMode)
    
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.bedroomMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.bedroomMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return
    
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='lightgray')
        canvas.create_rectangle(0,mode.height*3/5,mode.width,mode.height,fill='cornsilk2',outline='white')
        canvas.create_image(mode.width/7,mode.height/2, image=ImageTk.PhotoImage(mode.wife))
        canvas.create_rectangle(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3,fill='white')
        if mode.response == None:
            canvas.create_text(mode.x,mode.y,text="Hi, detective. My Name is Molly Barnett. Nico and I just got \nmarried. I cannot believe he just went missing after I \nwent on a work trip. I got back as soon as I could. \nWhat are you going to question me?",font='Arial 18')
        else:
            canvas.create_text(mode.x,mode.y,text=f'{mode.response}',font='Arial 22')
        canvas.create_text(mode.width/2,mode.height*5/6,text='Click to interact with her.',font='Arial 22 bold')
        if mode.app.welcomeMode.weapon == 'knife' and mode.nervous == True:
            canvas.create_text(mode.width/3,mode.height*2/3,text='You noticed a fresh cut on his hand') 
        elif mode.app.welcomeMode.weapon == 'pillow' and mode.nervous == True:
            canvas.create_text(mode.width/3,mode.height*2/3,text='You noticed multiple red bruise on his arm') 
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

# citation image adopted from https://www.pngguru.com/free-transparent-background-png-clipart-mfwdx/download
########################################################
#suspect 3
class suspect3Mode(Mode):
    def appStarted(mode):
        mode.app.checkpoint += 1
        mode.gardenerRaw = mode.loadImage('gardener.png')
        mode.gardener = mode.scaleImage(mode.gardenerRaw, 1/2)
        mode.x,mode.y=mode.textlocation(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3)
        mode.response = None
        if mode.app.welcomeMode.killer == 'Marlin Walter':
            mode.nervous = True
        else: mode.nervous = False

    def textlocation(mode,x,y,x1,y1):
        xLoc=(x+x1)/2
        yLoc=(y+y1)/2
        return (xLoc,yLoc)

    def mousePressed(mode,event):
        mode.question = mode.getUserInput('Your question')
        if mode.question != None:
            mode.response = conversationGeneration(mode.question,mode.app.welcomeMode.weapon,mode.nervous)
        else:
            mode.app.setActiveMode(mode.app.backyardMode)
    
    def keyPressed(mode,event):
        if(event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.backyardMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.backyardMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return 
    
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='lightgray')
        canvas.create_rectangle(0,mode.height*3/5,mode.width,mode.height,fill='lightgreen',outline='white')
        canvas.create_image(mode.width/7,mode.height/2, image=ImageTk.PhotoImage(mode.gardener))
        canvas.create_rectangle(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3,fill='white')
        if mode.response == None:
            canvas.create_text(mode.x,mode.y,text="Hi, my name is Marlin Walter. I am only \nhere to take care of the garden. I don't really \nspend time in the house. What can I help \nyou detective?",font='Arial 18')
        else:
            canvas.create_text(mode.x,mode.y,text=f'{mode.response}',font='Arial 22')
        canvas.create_text(mode.width/2,mode.height*5/6,text='Click to interact with him.',font='Arial 22 bold')
        if mode.app.welcomeMode.weapon == 'knife' and mode.nervous == True:
            canvas.create_text(mode.width/2,mode.height*2/3,text='You noticed a fresh cut on his hand') 
        elif mode.app.welcomeMode.weapon == 'pillow' and mode.nervous == True:
            canvas.create_text(mode.width/3,mode.height*2/3,text='You noticed multiple red bruise on his arm') 
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')

# citation image adopted from https://www.pinclipart.com/pindetail/iTiiRwR_call-3231-tied-up-man-cartoon-clipart/
########################################################
#Nico
class nicoMode(Mode):
    def appStarted(mode):
        mode.nicoStatus = 'dead'
        if mode.app.welcomeMode.weapon == 'GHB':
            mode.nicoStatus = 'alive'
        mode.nicoRaw = mode.loadImage('nico.png')
        mode.nico = mode.scaleImage(mode.nicoRaw,1/2)
        mode.x,mode.y=mode.textlocation(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3)
        mode.tideUp=True

    def keyPressed(mode,event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.backyardMode)
        elif (event.key=='n'):
            mode.app.currentMode = mode.app.backyardMode
            mode.app.setActiveMode(mode.app.userNotesMode)
        else: return

    def mousePressed(mode,event):
        if mode.nicoStatus == 'alive':
            if (mode.height/8-80<event.x<mode.width/8+80) and (mode.height/2-100<event.y<mode.height/2-60):
                mode.tideUp = False

    def textlocation(mode,x,y,x1,y1):
        xLoc=(x+x1)/2
        yLoc=(y+y1)/2
        return (xLoc,yLoc)

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='lightgray')
        canvas.create_rectangle(0,mode.height*3/5,mode.width,mode.height,fill='cornsilk2',outline='white')
        if mode.nicoStatus == 'alive': 
            canvas.create_image(mode.width/7,mode.height/2, image=ImageTk.PhotoImage(mode.nico))
            canvas.create_rectangle(mode.width*3/14,mode.height/6,mode.width*6/7,mode.height/3,fill='white')
            if mode.tideUp == True:   
                canvas.create_text(mode.x,mode.y,text="......",font='Arial 22 bold')
            else: canvas.create_text(mode.x,mode.y,text=f"Oh, Thank god! After my burger \nI just lost my conscious in {mode.app.welcomeMode.location} and \nwoke up to tide up.",font='Arial 20')
        else: 
            if mode.app.welcomeMode.weapon == 'knife':
                canvas.create_text(mode.width/2,mode.height/2,text=f"You found Nico's dissected dead body in the freezer. \nAfter a close examination on fingers you noticed {mode.app.welcomeMode.killer}'s hair.",font='Arial 22')
            else:
                canvas.create_text(mode.width/2,mode.height/2,text=f"You found Nico's body peacefully laying on the ground. \nHe is dead due to lack of oxygen and you found scratched body fiber \nof {mode.app.welcomeMode.killer}",font='Arial 22')
        canvas.create_text(50,30,text=f'{mode.app.hourCount:02d}:{mode.app.minCount:02d}:{mode.app.secCount:02d}',font='Arial 18 bold',fill='white')
