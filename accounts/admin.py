from django.contrib import admin
from .models import Account, MyAccountManager, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name')#clicking on this fields we can see respective user details 
    readonly_fields=('last_login','date_joined')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=() #make password read only
    
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radious:50%">'.format(object.profile_picture.url))

    thumbnail.short_description='Profile Picture'

    list_display=('thumbnail','user','city','state','country')
    
    
    
    
