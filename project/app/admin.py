from django.contrib import admin
from.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'pk',)


admin.site.register(User, UserAdmin)


admin.site.register(Task)

