import json
import os
import W2212841_data.W2212841_display as display

tags = "W2212841_data/W2212841_program_data/tags.json"
menus = "W2212841_data/W2212841_program_data/menuData.txt"
recipes = "W2212841_data/W2212841_program_data/recipes.json"

#Reads Menu Data Stored in menuData.txt
#This is so that menus can be easily edited in a text file and,
#do not have to be stored in individual data structures ,
#that have to be edited in code.
def readMenu(menu):
    try:
        with open(menus, "r") as fo:
            allMenus = fo.readlines()
    except:
        print("Something wrong with the file")
 
    if (f"{menu}\n") in allMenus:
        i = allMenus.index(f"{menu}\n")
        currentMenu = []
 
        while allMenus[i] != "\n":
            i += 1
            currentMenu.append(allMenus[i])
    else:
        currentMenu = []
        print("Menu Data is Corrupted, Please Check Menu Data")
 
    return(currentMenu)
 
#The menus that are easily editable in the menuData.txt come with
#the caveat that each menu item is followed by "\n" (escape character)
#this function returns the menu items without "\n" when
#the item is required instead of the choice number
def readMenuClean(menu):
    uncleanMenu = readMenu(menu)
    cleanMenu = []
    for x in range(0, len(uncleanMenu)):
        temp = 0
        temp = uncleanMenu[x].strip("\n")
        cleanMenu.append(temp)
    return cleanMenu
 
def readTags():
    try:
        with open(tags, "r") as fo:
            tagsSet = json.load(fo)
    except:
        print("There is something wrong with the file")
 
    tagsSet = set(tagsSet)
    return tagsSet
 
def readRecipes():
    if os.path.exists(recipes):
        try:
            with open(recipes, "r") as fo:
                recipesDict = json.load(fo)
        except:
            print("There is something wrong with the file.")
            display.run("Deleting file and creating a new save file.\n")
            os.remove(recipes)
            try:
                with open(recipes, "w") as fo:
                    recipesDict = {}
                    json.dump(recipesDict, fo, indent=4)
            except:
                print("Could not create a new file.")
    else:
        try:
            display.run("No save file detected. Creating a new save file.\n")
            with open(recipes, "w") as fo:
                recipesDict = {}
                json.dump(recipesDict, fo, indent=4)
        except:
            print("Could not create a new file.")
 
    return recipesDict

def readRecipesCorrect():
    recipeDict = readRecipes()
    for x in recipeDict:
        recipeDict[x]["ingredients"] = tuple(recipeDict[x]["ingredients"])
        recipeDict[x]["tags"] = set(recipeDict[x]["tags"])
    return recipeDict
    