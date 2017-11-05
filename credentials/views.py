# Create your views here.

from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Folder
from .serializers import FolderSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer