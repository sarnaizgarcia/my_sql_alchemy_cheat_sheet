from models import User, Recipes, session


def find_this_model_by_id(model, id):
    return session.query(model).filter(model.id == 1).first()

user = find_this_model_by_id(User, 1)
recipe = find_this_model_by_id(Recipes, 6)

print(user)
print(recipe)
