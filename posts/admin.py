from django.contrib import admin
from .models import Author,Gategory,Post,Comment,PostView
# Register your models here.

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Gategory)
admin.site.register(PostView)