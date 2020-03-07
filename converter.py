ingredient = {"flour": 120,
              "OO flour": 106,
              "whole wheat flour": 113,
              "sugar": 198,
              "brown sugar": 213,
              "butter tbsp": 14.125,
              "butter": 227,
              "brown butter": 182,
              "powdered sugar": 230,
              "water": 230,
              "milk": 230,
              "cream": 230,
              "graham crackers": 142,
              "corn syrup": 312,
              "eggs": 57,
              "cocoa": 85,
              "oats": 99,
              "shortening": 184,
              "chocolate chips": 170,
              "coconut": 85,
              "coconut oil": 156}

recipe = open('recipe.txt', 'w')
recipe.truncate()
num = int(input("How many ingredients would you like to convert? "))
i = 0
for i in range(num):
    ing = input("Enter an ingredient: ")
    
    
    if ing in ingredient:
        try:     
            amount = float(input("Enter amount in cups (tbsp if butter): "))
            value = ingredient[ing]
            converted = amount * value
            new_recipe = f"{round(converted, 2)} grams of {ing}."
            recipe.write(new_recipe + "\n")
            print(new_recipe)
        except:
            print("Not an amount in cups.")
    else:
        print("I can't convert that.")

recipe.close()