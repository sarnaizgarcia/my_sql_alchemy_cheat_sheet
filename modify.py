from models import User

user = User.find_by_id(2)
user.name = 'Ya no soy jose'
user.save()
print(user)
user.delete_user()