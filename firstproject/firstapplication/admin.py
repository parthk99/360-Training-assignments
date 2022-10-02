from django.contrib import admin
from .models import user
# Register your models here.

# admin.site.register(user)
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ["Name", "Address", "Contact"]