from django.contrib import admin
from .models import Post

admin.site.register(Post)   #为了让我们的模型在admin页面上可见，我们需要使用admin.site.register(Post)来注册模型.