#Importing Modules
import W2212841_functions.W2212841_validation as validation
import W2212841_data.W2212841_display as display
import W2212841_data.W2212841_read as read

#Prompt for name of recipes and ingredients
#Uses nameValidation function to validate
def promptName (validity,name,count):
    while validity == False:
        display.namingRule(name,count)
        checkingName = input(f"Your {name} Name : ")
        count += 1
        validity = validation.nameValidation(checkingName)
    return checkingName

#Prompts the User to Select a Menu Option
def promptMenu(menu):
    choice = 0
    currentMenu = read.readMenu(menu)
    i = len(currentMenu)
    while (1<= choice <= i-1) == False:
        display.displayMenu(menu)
        choice = input("Your Choice : ")
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
    return choice

def promptTime(recipe, validity, count):
    while validity == False:
        display.timeRule(recipe, count)
        checkingTime = input(f"Preparation Time for {recipe} : ")
        count += 1
        validity = validation.timeValidation(checkingTime)
    return checkingTime
    
def promptID(recipeDict, validity, count):
    while validity == False:
        display.IDRule(count)
        checkingID = input(f"Recipe ID of desired recipe : ")
        count += 1
        validity = validation.IDValidation(checkingID, recipeDict)
    return checkingID

def promptSearch(validity, count):
    while validity == False:
        display.searchRule(count)
        checkingSearch = input(f"Your searchword : ")
        count += 1
        validity = validation.searchValidation(checkingSearch)
    return checkingSearch
    
    