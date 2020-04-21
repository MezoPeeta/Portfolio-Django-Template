from django.contrib import admin
from .models import Post , Contact , Images , Subscribe

admin.site.site_header = 'Mazen'

admin.site.register(Post)

admin.site.register(Contact)

admin.site.register(Images)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title')
    list_filter = ('title')

