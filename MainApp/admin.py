from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('excerpt', )

    def excerpt(self, obj):
        return obj.get_excerpt(5)

admin.site.register(Post, PostAdmin)
