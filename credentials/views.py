# Create your views here.

from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Folder
from .models import Credentials
from .serializers import FolderSerializer
from .serializers import CredentialsSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class CredentialsViewSet(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer