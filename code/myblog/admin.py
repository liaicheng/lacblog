from django.contrib import admin
from myblog.models import Tag,BlogPost,Paragraph

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    """docstring for BlogPostAdmin"""
    list_display = ( 'title','id', 'author', 'timestamp')

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Tag)
admin.site.register(Paragraph)

