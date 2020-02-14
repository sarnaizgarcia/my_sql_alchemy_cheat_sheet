import csv
from models import User, Recipes

# abrir csv, primera columna nombre, segunda password, save() <- para todos los nombres
with open('./users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        password = row[1]
        user = User(name=name, password=password)
        user.save()
 
# lo mismo para los recipes, primera columna name, segunda columna user_id <- para todos los recipes
with open('./recipes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        user_id = row[1]
        recipe = Recipes(name=name, user_id=user_id)
        recipe.save()



