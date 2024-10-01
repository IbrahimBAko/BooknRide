from django.contrib import admin

from .models import User
from .models import UserProfile

class userprofileAdmin(admin.ModelAdmin):

    list_display = ('First_Name', 'Last_Name', 'Nationality', 'id')
    list_display_links = ('id','Nationality',)
    list_editable = ('First_Name', 'Last_Name',)

class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'email',)
    list_editable = ('username',)

# Register your models here.

admin.site.register(User, userAdmin)
admin.site.register(UserProfile, userprofileAdmin)


