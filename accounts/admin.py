from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


#this class is for making password readonly and liting items into the admin page 
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
    #this is for link clicking for the list items in admin panel.we only specifying 3 fields
    list_display_links=('email','first_name','last_name')
    #this is for readonly purpose we cant edit in the admin panbel
    readonly_fields=('last_login','date_joined')
    ordering=('-date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
admin.site.register(Account,AccountAdmin)