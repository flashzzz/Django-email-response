from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)