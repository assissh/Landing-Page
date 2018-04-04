from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to Image


class ImageAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


<<<<<<< HEAD:image/admin.py
admin.site.register(models.Image, helpsubcategoryAdmin)
=======
admin.site.register(models.Image, ImageAdmin)
>>>>>>> 8a8098a0a1f7fea1c7b39cdad80a72ddb848582b:Images/admin.py
admin.site.register(models.Comment)
