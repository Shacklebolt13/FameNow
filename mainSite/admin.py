from django.contrib import admin
from .models import Detail, Friend, Post, User

admin.site.register(User)
admin.site.register(Detail)
admin.site.register(Friend)
admin.site.register(Post)