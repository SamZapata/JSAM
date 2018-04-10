from django.contrib import admin

from .models import Post, Comment

# Registro de modelos

admin.site.register(Post)
admin.site.register(Comment)
