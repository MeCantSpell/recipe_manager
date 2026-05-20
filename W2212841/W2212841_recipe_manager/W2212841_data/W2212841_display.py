#Importing Modules
import W2212841_data.W2212841_read as read
import W2212841_data.W2212841_save as save
import time

#Code was Obtained from Reddit
#Used to aesthetically display code
#Not entirely sure of how it works
def run(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
 
 #For Printing Welcome Message
def welcomeMessage():
    welcomeMessage = "Welcome To Your Digital Recipe Manager!\nPress enter to continue."
    run(welcomeMessage)

#For Printing Exit Message
def exitMessage():
    exitMessage = """Thank You For Using The Digital Recipe Manager!
Closing the Application Now!
:)"""
    run(exitMessage)
 
#For Displaying the Menus
#This function runs by reading data off a text file and converting it to the relevant data,
#instead of storing it in the system itself (read.readMenu(menu)),
#allowing easy editing access without having to work with individual data structures
def displayMenu(menu):
    print(f"\n{menu}")
    print("=" * len(menu)+"\n")
    print("Please choose an option from this menu by typing in the correct number.\n")
    currentMenu = read.readMenu(menu)
    i = len(currentMenu)
    for x in range(0,i-1):
        print(f"{x+1}. {currentMenu[x]}")

#Message Prompting the User to Input a Valid Name for Recipes and Ingredients
#name takes in "recipe" or "ingredient"
#if retry is true, meaning a user has been prompt again, a warning message is also displayed
def namingRule(name, retry):
    print(f"\nThe Name of Your {name} Must be At Least 3 Characters And Cannot Exceed 50 Characters")
    print("It Should Also Have At Least 1 Letter")
    print("Only Special Characters of \"'\", \"-\" and \" \" are Allowed")
    
    if bool(retry) == True:
        print("Please Read the Naming Criteria Carefully and Try Again")
    else:
        pass
        
def ingredientRule():
    print("\nEvery Recipe Must Have At Least 3 Ingredients.")
    
def timeRule(recipe, retry):
    print(f"\nEnter the Preparation Time For {recipe}")
    print("Preparation Time Should be Entered in \"HH:MM\" format")
    print("Preparation Time Should be Between 00:05 and 12:00\n")
    
    if bool(retry) == True:
        print("Please Read the Timing Criteria Carefully and Try Again")
    else:
        pass

def recipe(recipe):
    print("Name : ",recipe["name"])
    print("Category : ",recipe["category"])
    print("Time : ",recipe["time"])
    if len(recipe["tags"]) != 0:
        print("Tags : ",recipe["tags"])
    else:
        print("Tags : None")
    print("Ingredients :")
    for x in recipe["ingredients"]:
        print (f"{x[0]} - {str(x[1])} {x[2]}")

def IDRule(retry):
    print("\nEnter the Recipe ID for the recipe you want to select.")
    print("The Recipe ID should be in the \"RCPXXX\" format.")
    print("The values XXX range from 001 to 999.")
    
    if bool(retry) == True:
        print("Please Read the ID Criteria Carefully and Try Again")
        print("If ID Criteria is Correct, Perhaps Recipe ID Does Not Exist")
    else:
        pass

#The function below was generated entirely by Claude (Sonnet 4.6)
#Since this function applies to only a visual aspect I have not worked on it myself.
#I am very bad at making tables in Python
def multipleRecipes(recipeBook):
    if len(recipeBook) == 0:
        print("No recipes found.")
        return
    col_widths = [8, 20, 12, 8, 20, 15]
    headers = ["ID", "Name", "Category", "Time", "Ingredient", "Tag"]
    header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(header_row)
    print("-" * len(header_row))
    for recipeID, recipe in recipeBook.items():
        ingredients = [i[0] for i in recipe["ingredients"]]
        tags = list(recipe["tags"]) if recipe["tags"] else [""]
        rows = max(len(ingredients), len(tags))
        for i in range(rows):
            if i == 0:
                id_col, name_col, cat_col, time_col = recipeID, recipe["name"], recipe["category"], recipe["time"]
            else:
                id_col = name_col = cat_col = time_col = ""
            ing_col = ingredients[i] if i < len(ingredients) else ""
            tag_col = tags[i] if i < len(tags) else ""
            row = [id_col, name_col, cat_col, time_col, ing_col, tag_col]
            print(" | ".join(f"{row[j]:<{col_widths[j]}}" for j in range(len(row))))
        print("-" * len(header_row))
        
def filteredRecipes(recipeDict, filterCategory, minimumTime, maximumTime, minIng, maxIng):
    if filterCategory == minimumTime == maximumTime == minIng == maxIng == None:
        multipleRecipes(recipeDict)
    
    tempDict = {}
    for x in recipeDict:
        recipe = recipeDict[x]
        
        condition1 = ((filterCategory is None) or (recipe["category"] == filterCategory)) == True
        condition2 = ((minimumTime is None) or (minimumTime <= recipe["time"] <= maximumTime)) == True
        condition3 = ((minIng is None) or (minIng <= len(recipe["ingredients"]) <= maxIng)) == True
        
        if (condition1 and condition2 and condition3) == True:
            tempDict[x] = recipe
    
    multipleRecipes(tempDict)
            
def searchRule(retry):
    print("\nEnter your searchword.")
    print("Searchword must contain at least 3 letters")
    print("Search occurs across name, category, tags, ingredients")
    
    if bool(retry) == True:
        print("Please Read the Search Criteria Carefully and Try Again")
    else:
        pass
            
def searchedRecipes(recipeDict, searchword):
    
    def searching(recipeDict,searchword):
        for x in recipeDict:
            recipe = recipeDict[x]
            
            condition1 = (searchword in recipe["name"])
            condition2 = (searchword in recipe["category"])
            condition3 = any(searchword in tag.lower() for tag in recipe["tags"])
            condition4 = any(searchword in ing[0].lower() for ing in recipe["ingredients"])
            
            if (condition1 or condition2 or condition3 or condition4) == True:
                tempDict[x] = recipe
                
        return tempDict
    
    tempDict = {}
    tempDict = searching(recipeDict,searchword)
        
    if len(tempDict) == 0:
        if len(searchword) != 3:
            searchword = searchword[:-1]
    tempDict = searching(recipeDict,searchword)
    
    if len(tempDict) ==0:
        if len(searchword) != 3:
            searchword = searchword[:-1]
    tempDict =searching(recipeDict,searchword)
    
    multipleRecipes(tempDict)

def categoryStatistics(recipeDict):
    categories = read.readMenuClean("Recipe Categories")
    categories = categories[:-1]
    print("Number of Recipes by Category :")
    for x in categories:
        count = 0
        for y in recipeDict:
            if x == recipeDict[y]["category"]:
                count += 1
        print(f"{x} - {count}")

def timeStatistics(recipeDict):
    print("\nNumber of Recipes by Cooking Time :")
    quick, medium, long = 0, 0, 0
    for x in recipeDict:
        if recipeDict[x]["time"] < "00:30":
            quick += 1
        elif "00:30" <= recipeDict[x]["time"] <= "00:60":
            medium += 1
        else:
            long += 1
    
    print(f"Quick (Under 30 Minutes) - {quick}")
    print(f"Medium (30 to 60 Minutes) - {medium}")
    print(f"Long (Over an Hour) - {long}\n")

def ingredientStatistics(recipeDict):
    ingredientCount = []
    totalIngredients = [0]
    for x in recipeDict:
        recipe = recipeDict[x]
        totalIngredients.append(len(recipe["ingredients"]))
        for y in recipe["ingredients"]: 
            if y[0] not in ingredientCount:
                ingredientCount.append(y[0])
                ingredientCount.append(1)
            else:
                adj = ingredientCount.index(y[0])
                ingredientCount[adj + 1] += 1
    print("Most Used Ingredients :")
    justCount = ingredientCount[1: :2]
    for x in range(1,4):
        target = max(justCount)
        targetIndex = ingredientCount.index(target)
        targetName = ingredientCount[targetIndex - 1]
        print(f"{x}.{targetName} - {target} times")
        justCount.remove(target)
    print(f"Average Number of Ingredients Used Per Recipe - {sum(totalIngredients)/len(recipeDict)}")
    mostIngredients = max(totalIngredients)
    leastIngredients = 3
    mostID = "RCP" + str(totalIngredients.index(mostIngredients)).zfill(3)
    leastID = "RCP" + str(totalIngredients.index(leastIngredients)).zfill(3)
    largestRecipe = recipeDict[mostID]
    smallestRecipe = recipeDict[leastID]
    print(f"{mostID} : {largestRecipe['name']} is the recipe with the most ingredients; {mostIngredients} ingredients")
    print(f"{leastID} : {smallestRecipe['name']} is the recipe with the least ingredients; {leastIngredients} ingredients")

def timeStatistics(startSessionTime):
    
    def calculate(time):
        hours = time//3600
        minutes = (time - (3600*hours))//60
        seconds = ((time - (3600*hours)-(60*minutes))//1)
        return [int(hours), int(minutes), int(seconds)]

    currentSessionTime, totalTime = save.saveTime(startSessionTime)
    currentHMS = calculate(currentSessionTime)
    totalHMS = calculate(totalTime)
    print(f"Current Session - {currentHMS[0]}:{currentHMS[1]}:{currentHMS[2]}")
    print(f"All Time Usage - {totalHMS[0]}:{totalHMS[1]}:{totalHMS[2]}")
    
def allStatistics(recipeDict, sessionStartTime):
    print("\nRECIPE BOOK SUMMARY")
    print("===================")
    if len(recipeDict) != 0:
        print()
        print(f"Total Recipes Added: {len(recipeDict)}")
        print()
        categoryStatistics(recipeDict)
        ingredientStatistics(recipeDict)
    else:
        print("No Recipes Have Been Added Yet. Go Ahead and Add Some Recipes!")
    timeStatistics(sessionStartTime)
    
    
    
    
        
        
    
    

    
    
                