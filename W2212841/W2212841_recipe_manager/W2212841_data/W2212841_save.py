import json
import os
import time
import W2212841_functions.W2212841_prompts as prompt
import W2212841_data.W2212841_display as display

recipes = "W2212841_data/W2212841_program_data/recipes.json"
userTime = "W2212841_data/W2212841_program_data/userTime.txt"
menus = "W2212841_data/W2212841_program_data/menuData.txt"
menuData = """Main Menu
Add Recipes
Edit Recipes
Duplicate Recipes
View Recipes
Export Recipes
Delete Recipes
View Statistics
Exit

View Menu
View All Recipes
View A Specific Recipe
View Filtered Recipe/s
Search
Return to Main Menu

Export Multiple Recipes As:
A Single File
Multiple Files

Delete Menu
Delete Specific Recipes
Delete All Recipes
Return to Main Menu

Valid Measuring Units
g
kg
ml
l
cup
tbsp
tsp
piece

Recipe Categories
BREAKFAST
LUNCH
DINNER
DESSERT
SNACK
BEVERAGE

"""
def saveRecipes(recipeDict):
    
    for x in recipeDict:
        recipeDict[x]["tags"] = list(recipeDict[x]["tags"])
        
    try:
        with open(recipes, "w") as fo:
            json.dump(recipeDict, fo, indent=2, sort_keys = True)
    except:
        print("There is something wrong with the file.")
    
def singleExport(recipeDict, ID):
    
    recipe = recipeDict[ID]
    
    if not os.path.exists(f"W2212841_exported_recipes/{recipe['name']}.txt"):
        with open(f"W2212841_exported_recipes/{recipe['name']}.txt","w") as fo:
            fo.write(f"Name : {recipe['name']}"+"\n")
            fo.write(f"Category :  {recipe['category']}"+"\n")
            fo.write(f"Time Taken: {recipe['time']}"+"\n")
            if len(recipe["tags"]) != 0:
                fo.write(f"Tags :  {recipe['tags']}"+"\n")
            fo.write("Ingredients :"+"\n")
            for x in recipe["ingredients"]:
                fo.write(f"{x[0]} - {str(x[1])} {x[2]}"+"\n")
    else:
        print(f"{recipe['name']} has already BEEN EXPORTED. Skipping export.")
    
            
def multipleExport(recipeDict, single):
    
    if single == False:
        for x in recipeDict:
            tempDict = {}
            tempDict[x] = recipeDict[x]
            
            singleExport(tempDict, x)
            
    else:
        existence = True
        while existence == True:
            fileName = prompt.promptName(False, "File", 0)
            if os.path.exists(f"W2212841_exported_recipes/{fileName}.txt"):
                display.run("This file already EXISTS. Please try with another name.")
                existence = True
            else:
                existence = False
        
        with open(f"W2212841_exported_recipes/{fileName}.txt","w") as fo:
            count = 0
            for x in recipeDict:
                recipe = recipeDict[x]
                count += 1
                fo.write(f"Recipe {count} :  {recipe['name']}"+"\n")
                fo.write(f"Category :  {recipe['category']}"+"\n")
                fo.write(f"Time Taken: {recipe['time']}"+"\n")
                if len(recipe["tags"]) != 0:
                    fo.write(f"Tags :  {recipe['tags']}"+"\n")
                fo.write("Ingredients :")
                for x in recipe["ingredients"]:
                    fo.write(f"{x[0]} - {str(x[1])} {x[2]}"+"\n")
                fo.write("\n\n")
                
def saveTime(sessionTime):
    if os.path.exists(userTime):
        with open(userTime,"r+") as fo:
            totalTime = fo.read()
            if totalTime == "":
                totalTime = "0"
            sessionTotalTime = round((time.time() - sessionTime),3)
            totalTime = float(totalTime) + sessionTotalTime
            fo.seek(0,0)
            fo.write(str(totalTime))
    else:
        with open(userTime,"w") as fo:
            totalTime = sessionTotalTime = round((time.time() - sessionTime),3)
            fo.write(str(sessionTotalTime))
    
    return sessionTotalTime, totalTime
        
def saveMenu():
    if os.path.exists(menus):
        fo = None
        fo = open(menus,"r")
        menuActualData = fo.read()
        if menuData == menuActualData:
            pass
        else:
            fo.close()
            os.remove(menus)
            with open(menus,"w") as fo:
                fo.write(menuData)
            
    else:
        with open(menus,"w") as fo:
            fo.write(menuData)
        
        
    
        
