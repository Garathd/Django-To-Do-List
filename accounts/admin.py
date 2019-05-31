# Code basis for this came from tutorial at: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import UserProfile


# INLINES, FOR EDITING ONE MODEL WITHIN ANOTHER ADMIN PAGE:
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'


# CUSTOM USER ADMIN:
class UserAdmin(BaseUserAdmin):

	inlines = (UserProfileInline,)
	list_display = ('username', 'first_name', 'last_name', 'date_joined', 'last_login')


# ADMIN FOR USER PROFILE:
class UserProfileAdmin(admin.ModelAdmin):
    
	list_display = ('user',)
	

# REGISTER ALL CUSTOM ADMINS:
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)