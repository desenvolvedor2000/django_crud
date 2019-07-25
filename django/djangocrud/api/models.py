from django.db import models
from django.db.models.signal import pre_save
from django.shortcuts import rende, get_object_or_404, redirect
from .utils.import unique_slug_generator

from django.contrib.auth.models import User
from django.conf import settings

class Usuario(models.model):
    nome = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    banco = models.CharField(max_length=20)
    agencia = models.CharField(max_length=10)
    conta = models.IntergerField()

def __str__(self):
    return self.name
    
    @property
    def title(self):
        return self.name

def Usuarios_pre_save_receiver(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)        

 pre_save.connect(Usuarios_pre_save_receiver,sender=Usuario)       