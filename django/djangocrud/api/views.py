from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
   
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
