from django.contrib import admin
from .models import User, CustomerUser, ShopUser

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
    'username', 'phone_num', 'is_shop', 'is_active', 'is_staff' ,'is_superuser', 'image',
    ]

admin.site.register(CustomerUser)
admin.site.register(ShopUser)