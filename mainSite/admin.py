from django.contrib import admin
from .models import Detail, Friend, User

admin.site.register(User)
admin.site.register(Detail)
admin.site.register(Friend)