from django.contrib import admin
from .models import Post, Comment, Category, Contact


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'date', 'post_view', 'video_url', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'email',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
