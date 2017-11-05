from django.contrib import admin
from .models import Folder;

# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(Folder, FolderAdmin);
