from django.contrib import admin
from myblog.models import Post, Category

class CategoryInLine(admin.StackedInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
