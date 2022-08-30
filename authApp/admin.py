from django.contrib import admin
from .models.account import Account
from .models.user import User

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
