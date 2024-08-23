from django.contrib import admin

from blog.models import BlogPost

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    fields = ('title', 'content',)


admin.site.register(BlogPost, BlogAdmin)