from django.contrib import admin
import datetime

from .models import AdvUser, Post, Comment, Consult


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author', 'pubdate','tags', 'image','stoim','mesta', 'file', 'video', 'audio','eventtime','eventdate')
    list_display_links = ('content',)
    search_fields = ('content', 'author','tags','eventtime','eventdate','stoim','mesta', 'image', 'file', 'video', 'audio','zapisi')
    date_hierarchy = 'pubdate'
    fields = ('author','tags', 'content','eventtime','eventdate', 'image','stoim','mesta', 'file', 'video', 'audio','zapisi')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'pubdate', 'post', 'moderation')
    list_display_links = ('content',)
    search_fields = ('content', 'author')
    date_hierarchy = 'pubdate'
    fields = ('author', 'content', 'post', 'moderation')


admin.site.register(Comment, CommentAdmin)

class ConsultAdmin(admin.ModelAdmin):
    list_display = ('eventdate', 'eventtime','zan')
    search_fields = ('eventdate', 'eventtime','zan')
    fields = ('eventdate', 'eventtime','zan')


admin.site.register(Consult, ConsultAdmin)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('id','__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'avatar', 'email', 'first_name', 'last_name','phone_num','faculty','group')
    fields = (('username', 'email', 'avatar','phone_num'), ('first_name', 'last_name'),('faculty','group'),
              ('is_active', 'is_activated'), ('is_staff', 'is_superuser'),
              'groups', 'user_permissions', ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(AdvUser, AdvUserAdmin)
