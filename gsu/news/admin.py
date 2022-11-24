from django.contrib import admin
import datetime

from .models import AdvUser, Post, Comment, Consult, Section, Tvor, Trud,Volant , Vist, Event


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'content', 'author', 'pubdate','tags', 'image','stoim','mesta', 'file', 'video', 'audio','eventtime','eventdate')
    list_display_links = ('content','name',)
    search_fields = ('name','content', 'author','tags','eventtime','eventdate','stoim','mesta', 'image', 'file', 'video', 'audio','zapisi')
    date_hierarchy = 'pubdate'
    fields = ('name','author','tags', 'content','eventtime','eventdate', 'image','stoim','mesta', 'file', 'video', 'audio','zapisi')


admin.site.register(Post, PostAdmin)

class VistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'content', 'author', 'pubdate', 'image','stoim', 'file', 'video', 'audio')
    list_display_links = ('content','name',)
    search_fields = ('name', 'content', 'author', 'image','stoim', 'file', 'video', 'audio','event')
    date_hierarchy = 'pubdate'
    fields = ('name', 'content', 'author', 'image','stoim', 'file', 'video', 'audio','event')


admin.site.register(Vist, VistAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','eventtime','eventdate','zan')
    search_fields = ('id','eventtime','eventdate','zan','zapisi')
    fields = ('eventtime','eventdate','zan','zapisi')

admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'pubdate', 'post','vist', 'moderation')
    list_display_links = ('content',)
    search_fields = ('content', 'author')
    date_hierarchy = 'pubdate'
    fields = ('author', 'content', 'post','vist', 'moderation')


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


class SectionAdmin(admin.ModelAdmin):
    list_display= ('name','otobr')
    search_fields = ('name','otobr')
    fields = ('name','otobr')

admin.site.register(Section, SectionAdmin)

class TvorAdmin(admin.ModelAdmin):
    list_display= ('name','otobr')
    search_fields = ('name','otobr')
    fields = ('name','otobr')

admin.site.register(Tvor, TvorAdmin)

class TrudAdmin(admin.ModelAdmin):
    list_display= ('name','otobr')
    search_fields = ('name','otobr')
    fields = ('name','otobr')

admin.site.register(Trud, TrudAdmin)

class VolantAdmin(admin.ModelAdmin):
    list_display= ('name','otobr')
    search_fields = ('name','otobr')
    fields = ('name','otobr')

admin.site.register(Volant, VolantAdmin)
