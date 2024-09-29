from django.contrib import admin
from .models import Post

admin.site.register(Post)  #让模型在admin页面上可见