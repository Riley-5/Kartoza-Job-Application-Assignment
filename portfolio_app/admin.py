from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from portfolio_app.models import User

# Register your models here.
admin.site.register(User, UserAdmin)