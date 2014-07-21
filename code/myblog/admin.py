from django.contrib import admin
from myblog.models import Tag,BlogPost,Paragraph,Photo,Code

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    """docstring for BlogPostAdmin"""
    list_display = ( 'title','id', 'author', 'timestamp')
    search_fields = ('title', )

class CodeAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', )

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Photo)
admin.site.register(Code)
admin.site.register(Tag,TagAdmin)
admin.site.register(Paragraph)


