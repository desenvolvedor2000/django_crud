from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.urls import include, path
from rest_framework. import routers
from rest_framework.authtoken import views
from djangocrud.api import views
from .router import router

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)


urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/include('router.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
