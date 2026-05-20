#Importing Modules
import W2212841_data.W2212841_display as display
import W2212841_data.W2212841_read as read
import W2212841_data.W2212841_save as save
import W2212841_functions.W2212841_prompts as prompt
import W2212841_functions.W2212841_validation as validation

#Adds a Recipe, prompts for name
def addRecipe(recipeBook, edit):
    add = True
    while add == True:
        recipeName = prompt.promptName(False,"Recipe",0)
        ingredientsList = addIngredientsList()
        recipeTime = prompt.promptTime(recipeName, False, 0)
        recipeCategory = addCategory(recipeName)
        recipeTags = addTag(recipeName)
        newID = addID(recipeBook)

        recipeBook[newID] = {"name": recipeName,
                             "ingredients": ingredientsList,
                            "time": recipeTime,
                            "category": recipeCategory,
                            "tags": recipeTags}
        display.recipe(recipeBook[newID])
        
        isSaving = validation.addingValidation(input("\nDo you want to save this recipe?\nAnswer with \"Y\" or \"N\"\n"))
        if isSaving == True:
            save.saveRecipes(recipeBook)
            display.run("Auto-saving recipe.\n")
        else:
            del recipeBook[newID]
        
        if edit == True: break
        
        isAdding = validation.addingValidation(input("Do you want to add another recipe?\nAnswer with \"Y\" or \"N\"\n"))
        if isAdding == True:
            pass
        else:
            break

#Adds an Ingredient as a tuple with its data, prompts for name
def addIngredient(ingredientName):
    print(f"\nEnter Measuring Unit of {ingredientName}.\n")
    unitChoice = prompt.promptMenu("Valid Measuring Units")
    units = read.readMenuClean("Valid Measuring Units")        
    quantity = 0
    while quantity <= 0:
        print(f"\nEnter the Quantity of {ingredientName} in {units[unitChoice-1]}.")
        print("Please Use a Suitable Input (Numeric Value)")
        quantity = input()
        try:
            quantity = float(quantity)
        except ValueError:
            quantity = 0
    ingredientData = (ingredientName,quantity,units[unitChoice-1])
    
    return ingredientData

#Adds all ingredient tuples to one ingredients list which can be linked to a recipe
def addIngredientsList():
    count = 0
    isAddingIngredient = True
    ingredientsList = []
    
    display.ingredientRule()
    
    while (count < 20) and (isAddingIngredient == True):
        count += 1
        if (count < 3) or (count == 20):
            ingredientName = prompt.promptName(False,"Ingredient",0)
            ingredientData = addIngredient(ingredientName)
            ingredientsList.append(ingredientData)
        else:
            ingredientName = prompt.promptName(False,"Ingredient",0)
            ingredientData = addIngredient(ingredientName)
            ingredientsList.append(ingredientData)
            isUserAdding = input("Are You Adding Another Ingredient?\nEnter Y/N\n")
            isAddingIngredient = validation.addingValidation(isUserAdding)
        
    return ingredientsList   

def addCategory(recipe):
    print(f"\n Select the Recipe/Meal Category for {recipe}.\n")
    categoryChoice = prompt.promptMenu("Recipe Categories")
    categories = read.readMenuClean("Recipe Categories")
    category = categories[categoryChoice-1]
    return category

def addTag(recipe):
    isAddingTag = True
    recipeTagsSet = set()
    while isAddingTag == True:
        print(f"\nAre There Any Tags to be Added for {recipe}?\nEnter Y/N\n")
        isUserAdding = input()
        isAddingTag = validation.addingValidation(isUserAdding)
        if isAddingTag == False:
            break
        tag = prompt.promptName(False, "Tag", 0)
        recipeTagsSet.add(tag)
    return recipeTagsSet

def addID(recipeBook):
    count = 1
    while True:
        newID = "RCP" + str(count).zfill(3)
        if newID not in recipeBook:
            break
        count += 1
    
    return newID
    
def delRecipe(recipeDict):
    delStatus = True
    if len(recipeDict) == 0:
            print("There are no recipes to delete")
            delStatus = False
    
    while delStatus == True:
        
        ID = prompt.promptID(recipeDict, False, 0)
        print()
        display.recipe(recipeDict[ID])
        print()
        isDeleting = validation.addingValidation(input("Do you want to delete this recipe?\nAnswer with \"Y\" or \"N\"\n"))

        if isDeleting == True:
            del recipeDict[ID]
            save.saveRecipes(recipeDict)
            display.run("Recipe successfully deleted.")
        else:
            pass
        
        isDeletingMore = validation.addingValidation(input("Do you want to delete another recipe?\nAnswer with \"Y\" or \"N\"\n"))
        if isDeletingMore == True:
            pass
        else:
            break
        
        if len(recipeDict) == 0:
            print("There are no recipes to delete")
            delStatus = False
    
def viewRecipe(recipeDict):
    viewStatus = True
    
    while viewStatus == True:
        
        ID = prompt.promptID(recipeDict, False, 0)
        print()
        display.recipe(recipeDict[ID])
        print()
        isViewing = validation.addingValidation(input("Do you want to view another recipe?\nAnswer with \"Y\" or \"N\"\n"))

        if isViewing == True:
            pass
        else:
            break
        
def filterRecipe():
    def category():
        categoryChoice = prompt.promptMenu("Recipe Categories")
        categories = read.readMenuClean("Recipe Categories")
        return categories[categoryChoice - 1]
    def time():
        minimumTime = prompt.promptTime("minimum", False, 0)
        maximumTime = prompt.promptTime("maximum", False, 0)
        return minimumTime, maximumTime
    def ingredients():
        userMinimum = int(input("Enter the minimum number of ingredients required. (Max = 20)\n"))
        while (0 < userMinimum <= 20) != True:
            userMinimum = int(input("Enter the minimum number of ingredients required. (Max = 20)\n"))
        userMaximum = int(input(f"Enter the maximum number of ingredients required. (Max = 20, Min = {userMinimum})\n"))
        while (userMinimum <= userMaximum <= 20) != True:
            userMaximum = int(input(f"Enter the maximum number of ingredients required. (Max = 20, Min = {userMinimum})\n"))
        return userMinimum, userMaximum

    filterCategory = minimumTime = maximumTime = minIng = maxIng = None

    filterByCategory = validation.addingValidation(input("Would you like to filter by Category?\nAnswer with \"Y\" or \"N\"\n"))
    if filterByCategory == True:
        filterCategory = category()
    filterByTime = validation.addingValidation(input("Would you like to filter by Time Taken?\nAnswer with \"Y\" or \"N\"\n"))
    if filterByTime == True:
        minimumTime, maximumTime = time()
    filterByIngredients = validation.addingValidation(input("Would you like to filter by Number of Ingredients?\nAnswer with \"Y\" or \"N\"\n"))
    if filterByIngredients == True:
        minIng, maxIng = ingredients()

    return filterCategory, minimumTime, maximumTime, minIng, maxIng
                
def searchRecipe(recipeDict):
    searchword = prompt.promptSearch(False, 0)
    searchword = searchword.lower()
    display.searchedRecipes(recipeDict,searchword)
    
def exportRecipe(recipeDict):
    tempDict = {}
    isAdding = True
    while isAdding == True:
        ID = prompt.promptID(recipeDict, False, 0)
        if ID not in tempDict:
            tempDict[ID] = recipeDict[ID]
        else:
            print("Recipe has already been selected to export")
        isAdding = validation.addingValidation(input("Do you wish to export another Recipe?\nAnswer with \"Y\" or \"N\"\n"))
        
    if len(tempDict) == 1:
        save.singleExport(tempDict, ID)
        
    elif len(tempDict) == 0:
        print("No recipes exported. Returning to main menu")
        
    else:
        exportChoice = prompt.promptMenu("Export Multiple Recipes As:")
        match exportChoice:
            case 1:
                save.multipleExport(tempDict, True)
            case 2:
                save.multipleExport(tempDict, False)
    
def editRecipe(recipeDict):
    tempDict = recipeDict
    ID = prompt.promptID(recipeDict, False, 0)
    display.recipe(recipeDict[ID])
    edit = validation.addingValidation(input("\nDo you wish to edit this recipe?\nAnswer with\"Y\" or\"N\"\n"))
    
    if edit == False:
        pass
    else:
        del recipeDict[ID]
        addRecipe(recipeDict, True)
        if len(tempDict) != len(recipeDict):
            save.saveRecipes(tempDict)
        display.run("Recipe successfully edited")
            
def duplicateRecipe(recipeDict):
    ID = prompt.promptID(recipeDict, False, 0)
    display.recipe(recipeDict[ID])
    duplicate = validation.addingValidation(input("\nDo you wish to duplicate this recipe?\nAnswer with\"Y\" or\"N\"\n"))

    if duplicate == False:
        pass
    else:
        newID = addID(recipeDict)
        recipeDict[newID] = recipeDict[ID]
        save.saveRecipes(recipeDict)
        display.run("Recipe successfully duplicated")
        
def countTime(startTime):
    sessionTime = (time.time() - startTime)
    return sessionTime
    
                    