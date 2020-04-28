import random
def generateCheckpoint():
    totalCheckpoint = [n for n in range(13)]
    modeDic = {'tvMode':[0], 'computerMode':[0],'table1Mode':[0],'table2Mode':[0],'suspect1Mode':[0],
                'sinkMode':[0],'dinningMode':[0],'counterMode':[0],'suspect2Mode':[0],'tvDrawerMode':[0],
                'bedMode':[0],'suspect3Mode':[0],'storageMode':[0]}
    for mode in modeDic:
        num = random.choice(totalCheckpoint)
        modeDic[mode] = num
        totalCheckpoint.remove(num)
    if modeDic['table1Mode'] > modeDic['storageMode']:
        smallValue = modeDic['storageMode']
        largerValue = modeDic['table1Mode']
        modeDic['table1Mode'] = smallValue
        modeDic['storageMode'] = largerValue
    return modeDic


     
    
    