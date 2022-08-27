from django.contrib import admin
from .models import Posts

# Register your models here.
# admin.site.register(Posts)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['my_name', 'posts_main_img']