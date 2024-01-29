from enum import Enum
import json

def GetSubIngredient(name,recipes):
    temp = []
    print(name)
    if name in recipes:
        if len(recipes[name]['ingredients']) > 0:
            for ingredient in recipes[name]['ingredients']:
                temp.append(ingredient)
        return temp
    else:
        return None

def GetIngredients(item):
    global temp
    temp = []
    temp.append(recipes[item]['products'][0])
    for Ingredient in recipes[item]['ingredients']:
        temp.append(Ingredient)
        if Ingredient['name'] in recipes:
            print(f"   {Ingredient['amount']}x {HumanFriendly(Ingredient['name'])}:{recipes[Ingredient['name']]['energy']}s {NumOfAss(Ingredient['name'])}x {HumanFriendly(recipes[Ingredient['name']]['category'])}")
            if len(recipes[Ingredient['name']]['ingredients']) > 0:
                GetSubIngredient(Ingredient['name'],2)
        else:
            print(f"   {Ingredient['amount']}x {HumanFriendly(Ingredient['name'])}")
    print(temp)

def JsonFriendly(word):
    x = word.replace(" ","-")
    return x

def HumanFriendly(word):
    x = word.replace("-"," ")
    return x

def NumOfAss(item,filepath,ipm,assembler):
    assemblers = GetAssMachines(filepath)
    recipes = GetRecipes(filepath)
    if item in recipes:
        ics = recipes[item]['energy']
        product = recipes[item]['products'][0]['amount']
        x = ((float(ipm)/60)*ics)/assemblers[assembler]["crafting_speed"]
        out = x/product
    else:
        out = 0 
    return out

def NumOfSmel(item,filepath,ipm,smelter):
    furnaces = GetFurnace(filepath)
    recipes = GetRecipes(filepath)
    if item in recipes:
        ics = recipes[item]['energy']
        product = recipes[item]['products'][0]['amount']
        x = ((float(ipm)/60)*ics)/furnaces[smelter]["crafting_speed"]
        out = x/product
    else:
        out = 0 
    return out

def GetAssMachines(filepath):
    AssMachines = json.load(open(fr"{filepath}\assembling-machine.json"))
    temp = AssMachines.copy()
    for i, item in enumerate(AssMachines):
        try: 
            AssMachines[item]["crafting_categories"]['crafting']
        except:
            del temp[item]
    AssMachines = temp
    return AssMachines

def GetFurnace(filepath):
    Furnace = json.load(open(fr"{filepath}\furnace.json"))
    temp = Furnace.copy()
    for i, item in enumerate(Furnace):
        try: 
            Furnace[item]["crafting_categories"]['smelting']
        except:
            del temp[item]
    Furnace = temp
    return Furnace

def GetRatio(item,ipm):
    temp = []
    ratio = []
    temp.append(recipes[item]['products'][0])
    for Ingredient in recipes[item]['ingredients']:
        temp.append(Ingredient)
    a = ipm/temp[0]['amount']
    for item in temp:
        b = a*item['amount']
        ratio.append(b)
    return ratio

def GetRecipes(filepath):
    recipes = json.load(open(fr"{filepath}\recipe.json"))
    return recipes

ipm = 60.0

if __name__ == "__main__":
    filepath = r"C:\Users\rudyb\AppData\Roaming\Factorio\script-output\recipe-lister"
    recipes = GetRecipes(filepath)
    assemblingmachines = GetAssMachines(filepath)
    furnace = GetFurnace(filepath)
    print(f"{len(recipes)} recipes loaded!")
    print(f"{len(assemblingmachines)} Assembly Machines Found!")
    print(f"{len(furnace)} Furnaces Found!\n")

    item = "logistic-science-pack"
    GetSubIngredient(recipes[item]['name'])