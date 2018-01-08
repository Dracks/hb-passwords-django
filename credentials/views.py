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

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_list_queryset()
        return viewsets.ModelViewSet.list(self, request, args, kwargs)

    def get_list_queryset(self):
        credentials = Credentials.objects.all()
        folder = self.request.query_params.get('folder', None)
        if folder is not None:
            credentials = credentials.filter(folder=folder)
        return credentials