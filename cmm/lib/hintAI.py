from cmu_112_graphics import*
import random

# Hint generator
########################################################

class hintAI(Mode):
    def appStarted(mode):
        mode.roomAndObjects = {'livingroom':['tv','computer','table1','table2'],
                                'bedroom':['tvDrawer','bed'],
                                'kitchen':['sink','counter','dinning'],
                                'backyard':['storage']}
        mode.hintLib = {'level1Hint':{'tv':['Weather Report could that be the lead?','There is a trend but cannot make judgement too quick.'],
                                    'computer':['Color of the rug?','The orientation of the colors on rug?'],
                                    'table1':['Maybe the paper has special ink?','Could it be any colorless chemicals?'],
                                    'table2':['C4H8O3 is called GHB'],
                                    'tvDrawer':['Passcode often hides in the room','Nico loves hide passward in furnture'],
                                    'bed':['Stain looks strange','Be aware of the conditions of everything'],
                                    'sink':['Maybe question who cut themselves','Could this connect to the knife missing'],
                                    'counter':['Check all the drawers','Notice anything missing or stange?'],
                                    'dinning':['Could this be why he went missing','Maybe this is why they want him dead.'],
                                    'storage':['The passcode should be somewhere in this house','6 digits password where have I seen it?']},
                        'level2Hint':{'tv':['Weather Report could that be the lead?','There is a trend but cannot make judgement too quick.'],
                                    'computer':['Maybe flip the color orientation around?','The orientation of the colors can be other way around.'],
                                    'table1':['What kind of light that shines to it that will show?','Think about light that is not in visual color range.'],
                                    'table2':['C4H8O3 is called GHB'],
                                    'tvDrawer':['Check the kitchen floor.','What is the shape that created on the floor'],
                                    'bed':['Why is there other material on the pillow?'],
                                    'sink':['Maybe the blood is from people who hide the knife.','Maybe knife user is involved in this missing case?'],
                                    'counter':['Maybe this is the weapon?','Who knows it in this house?'],
                                    'dinning':['This is the motive of the suspect.','The killing motive'],
                                    'storage':['Check out the paper on the table in livingroom.','Maybe it is the number on the paper in livingroom']},
                        'level3Hint':{'tv':['TV is not really important.','Nothing strange about the TV'],
                                    'computer':['Maybe flip the color orientation around?','The orientation of the colors can be other way around.'],
                                    'table1':['Sunlight is a UV light that often reveal invisible ink','UVlight is useful for this kind of situation'],
                                    'table2':['C4H8O3 is called GHB'],
                                    'tvDrawer':['The location of lamda in the greek letters is 11 and chi is 22'],
                                    'bed':[f'The reason why unusuall substance on pillow is because the crime location is in {mode.app.welcomeMode.location}'],
                                    'sink':['Maybe the blood is from people who hide the knife.','Maybe knife user is involved in this missing case?'],
                                    'counter':[f'The weapon is {mode.app.welcomeMode.weapon}'],
                                    'dinning':['This is the motive of the suspect.','The killing motive'],
                                    'storage':['Check out the paper on the table in livingroom.','Maybe it is the number on the paper in livingroom']}}
        mode.modesRecording = {'livingroom':{'tv':0,
                                             'computer':0,
                                             'table1':0,
                                             'table2':0},
                                'bedroom':{'tvDrawer':0,
                                           'bed':0},
                                'kitchen':{'sink':0,
                                           'counter':0,
                                           'dinning':0},
                                'backyard':{'storage':0}}
        mode.curRoom = 'livingroom'
        mode.winNum = 0
        mode.winMode = None
        mode.hint = None

    def recordEnterTime(mode,room,curMode):
        mode.modesRecording[room][curMode] += 1

    def determineHintMessage(mode,room,completePoint,hintCount):
        if room != mode.curRoom:
            mode.winNum = 0
            mode.winMode = None
        for modes in mode.modesRecording[room]:
            print(mode.modesRecording[room][modes],mode.winNum)
            if mode.modesRecording[room][modes] >= mode.winNum and mode.modesRecording[room][modes] != 0:
                mode.winNum = mode.modesRecording[room][modes]
                if modes != mode.winMode:
                    mode.app.currentMode.hintCount = 1
                mode.winMode = modes
        message = mode.hintMessageGeneration(room,completePoint,mode.winMode,hintCount)
        return message

    def hintMessageGeneration(mode,room,completePoint,winMode,hintCount):
        numOfCheckpoint = len(mode.roomAndObjects[room])
        if completePoint < numOfCheckpoint:
            hint = random.choice(["You gotta check all the question marks!","Not all evidences are collected right now.","Try to find all the clues."])
        else:
            if hintCount <= 2:
                hint = random.choice(mode.hintLib['level1Hint'][winMode])
            elif 2 < hintCount <= 4:
                hint = random.choice(mode.hintLib['level2Hint'][winMode])
            else:
                hint = random.choice(mode.hintLib['level3Hint'][winMode])
                mode.app.currentMode.hintCount = 1  
                mode.modesRecording[room][winMode] = 1
        return hint

    def keyPressed(mode,event):
        mode.app.setActiveMode(mode.app.currentMode)

    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='cyan')
        if mode.winMode != None:
            canvas.create_text(mode.width/2,mode.height/5,text='Seems like you are struggling. Let me help!',fill='red',font='Arial 30 bold') 
            canvas.create_text(mode.width/2,mode.height/2,text=f'{mode.hint}',font='Arial 26 bold')
        else:
            canvas.create_text(mode.width/2,mode.height/2,text="Hi, I am your hint bot you can always\n call me when you want some hint!\n       Press any key back to the game.",font='Arial 32')
