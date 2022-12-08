from django.contrib import admin
from blog.models import Post, New
# from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Post)
admin.site.register(New)

# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# # Обновите поля и сохраните их снова
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()