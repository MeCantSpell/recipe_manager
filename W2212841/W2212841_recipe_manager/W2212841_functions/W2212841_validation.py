#Validates the names of recipes and ingredients
def nameValidation(name):
    validity = True
    invalidCharacters = ("!","@","#","$","%","^","&","*","(",")","_","+","=","[","{","]","}","|",";",":","\\","<",",",">",".","/","?","`","~")
    if (3 <= len(name) <= 50) == True:
        validity = True
        if name.isdigit() == True:
            validity = False
        elif name.isspace() == True:
            validity = False
        elif name == False:
            validity = False
        elif any(character in name for character in invalidCharacters) == True:
            validity = False
        else:
            validity = True
    else:
        validity = False
    return validity

#Validates the need to add more inputs from user
def addingValidation(answer):
    validity = False
    while validity == False:
        if (answer in ("y","Y","yes","Yes","YES")):
            isAdding = True
            validity = True
        elif (answer in ("N","n","No","no","NO")):
            isAdding = False
            validity = True
        else:
            print("Please Type in \"Y\" or \'N\"")
            answer = input()
    return isAdding
    
#Validates preparation time
#00:05 to 12:00
def timeValidation(time):
    if (time[0:2].isdigit()) and (time[2] == ":") and (time[3:].isdigit()):
        if int(time[0:2]) == 0:
            if 59 >= int(time[3:]) >= 5:
                validity = True
            else:
                validity = False
        elif int(time[0:2]) == 12:
            if int(time[3:]) == 0:
                validity = True
            else:
                validity = False
        elif int(time[0:2]) < 12:
            if int(time[3:]) < 59:
                validity = True
            else:
                validity = False
        else:
            validity = False
    else:
        validity = False
        
    return validity

def IDValidation(ID, recipeDict):
    if ID not in recipeDict:
        validity = False
    else:
        validity = True
        
    return validity
            
def searchValidation(searchword):
    if len(searchword) < 3:
        validity = False
    else:
        validity = True
    return validity
    
 