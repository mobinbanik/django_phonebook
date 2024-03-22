from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'number', 'address', 'user')
    search_fields = ('first_name', 'last_name', 'number', 'address', )
    list_filter = ('user', )

