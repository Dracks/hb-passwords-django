from django.contrib import admin
from .models import Folder;
from .models import Credentials;

# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')

class CredentialAdmin(admin.ModelAdmin):
    list_display = ('url', 'user', 'password','folder','created_at','updated_at','last_viewed','password_updated')

admin.site.register(Folder, FolderAdmin);
admin.site.register(Credentials, CredentialAdmin);

