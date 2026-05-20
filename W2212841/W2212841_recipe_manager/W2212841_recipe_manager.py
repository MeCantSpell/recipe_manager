#Importing Modules
import os
import time
import traceback
import W2212841_data.W2212841_read as read
import W2212841_data.W2212841_display as display
import W2212841_data.W2212841_save as save
import W2212841_functions.W2212841_validation as validation
import W2212841_functions.W2212841_tasks as task
import W2212841_functions.W2212841_prompts as prompt

#This is required for the program to run when double clicked
os.chdir(os.path.dirname(os.path.abspath(__file__)))

save.saveMenu()
sessionStartTime = time.time()
#Initializing Variables
main = True
recipeDict = read.readRecipesCorrect()
display.run(f"Loaded {len(recipeDict)} recipes.\n")

#Displaying Welcome Message
display.welcomeMessage()

input()
#This Loop Ensures When Users Exit a Sub-Menu,
#they return to the Main Menu
while main == True:
    #Displaying Main Menu
    choice = prompt.promptMenu("Main Menu")
    #Selection to Other Menus
    match choice:
        #Adding Recipe
        case 1:
            task.addRecipe(recipeDict, False)
            recipeDict = read.readRecipesCorrect()
        #Edit Recipe
        case 2:
            if len(recipeDict) != 0:
                task.editRecipe(recipeDict)
                recipeDict = read.readRecipesCorrect()
            else:
                print("There are no Recipes to Edit!")
        #Duplicate Recipe
        case 3:
            if len(recipeDict) != 0:
                task.duplicateRecipe(recipeDict)
                recipeDict = read.readRecipesCorrect()
            else:
                print("There are no Recipes to Duplicate!")
        #View Recipe
        case 4:
            choice4 = prompt.promptMenu("View Menu")
            match choice4:
                #View All Recipes
                case 1:
                    display.multipleRecipes(recipeDict)
                #View a Specific Recipe
                case 2:
                    if len(recipeDict) != 0:
                        task.viewRecipe(recipeDict)
                    else:
                        print("There are no Recipes to View")
                #View Filtered Recipes
                case 3:
                    category,minTime,maxTime,minIng,maxIng = task.filterRecipe()
                    display.filteredRecipes(recipeDict,category,minTime,maxTime,minIng,maxIng)
                #Search for a Particular Recipe
                case 4:
                    task.searchRecipe(recipeDict)
                case 5:
                    pass
        #Export Recipe
        case 5:
            if recipeDict != 0:
                task.exportRecipe(recipeDict)
                display.run("Recipe/s exported succesfully")
            else:
                print("There are no Recipes to Export!")
        #Deleting Recipe
        case 6:
            choice6 = prompt.promptMenu("Delete Menu")
            match choice6:
                #Delete Some Recipes
                case 1:
                    task.delRecipe(recipeDict)
                #Delete All Recipes
                case 2:
                    isNuclear = validation.addingValidation(input("Are you sure you want to DELETE ALL recipes?\nAnswer with \"Y\" or \"N\".\n"))           
                    if isNuclear == True:
                        os.remove("W2212841_data/W2212841_program_data/recipes.json")
                        display.run("ALL RECIPES HAVE BEEN DELETED!\n")
                        recipeDict = read.readRecipesCorrect()
                case 3:
                    pass
        #View Statistics
        case 7:
            display.allStatistics(recipeDict, sessionStartTime)
        #Exit Application
        case 8:
            display.exitMessage()
            unwanted, unwanted2 = save.saveTime(sessionStartTime)
            exit()

