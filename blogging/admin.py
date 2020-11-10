from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ['posts']



class PostAdmin(admin.ModelAdmin):
    # fields = ('title', 'content', 'category')
    inlines = [
        CategoryInline,
    ]
    # fieldsets = (None, {
    #         'fields': ('url', 'title', 'content', 'categories')
    #     })


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)