from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario
from rest_framework.serializers import(
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField,
    ValidationError,
)
from django.db.models import Q
from django contrib.auth import(
    authencate,
    get_user_model,
    login as login_auth,
    logout as logout_auth,
)
from Usuarios.models import Usuario
User = get_user_model()

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'cep', 'banco','agencia','conta')

class UsuarioCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'nome',
             'email',
              'cep',
               'banco',
               'agencia',
               'conta',
        ]        