from django.contrib import admin
from .models import CustomerQna, CustomerQuestion

# Register your models here.

admin.site.register(CustomerQna)
admin.site.register(CustomerQuestion)