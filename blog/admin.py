from django.contrib import admin

# Register your models here.
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
