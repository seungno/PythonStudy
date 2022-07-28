import random
def listCreate(listCount):
    returnList = []
    for valueCreate in range(listCount):
        randomValue=random.randint(1,100)
        returnList.append(randomValue)
    return returnList
def valueSort(targetList,maxAttr=True):
    returnList=[]
    for t in range(len(targetList)):
        max = targetList[0] 
        for i in range(1, len(targetList)): 
            if maxAttr == True:
                if max <= targetList[i]: 
                    max = targetList[i]  
            if maxAttr == False:
                if max >= targetList[i]: 
                    max = targetList[i]  
            
        targetList.remove(max) 
        returnList.append(max) 
                  
    return returnList

targetList = listCreate(5)
outputList = valueSort(targetList,maxAttr=True)
print (outputList)


