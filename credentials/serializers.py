from rest_framework import serializers
from .models import Folder
from .models import Credentials

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'name', 'user','created_at','updated_at')

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ('url', 'user', 'password','folder','created_at','updated_at','last_viewed','password_updated')
