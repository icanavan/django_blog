from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

    exclude = ('posts')
    pass


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    class Meta:
        model = Post
    # fieldsets = (None, {
    #         'fields': ('url', 'title', 'content', 'categories')
    #     })
    pass

admin.site.register(Post)
admin.site.register(PostAdmin)
admin.site.register(Category)
admin.site.register(CategoryAdmin)