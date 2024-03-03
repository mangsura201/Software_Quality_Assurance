from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('excerpt', )

<<<<<<< HEAD

=======
    def excerpt(self, obj):
        return obj.get_excerpt(5)

admin.site.register(Post, PostAdmin)
>>>>>>> 62615bc1b85e5176a07671444b0786e27d168e66
