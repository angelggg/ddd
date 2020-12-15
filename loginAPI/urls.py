from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from login.viewsets import MyUserViewSet, MyUserCreateViewSet

"""
API ROUTES
"""
apirouter = DefaultRouter()
apirouter.register(r'users', viewset=MyUserViewSet)
apirouter.register(r'signup', viewset=MyUserCreateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path(r'api/', include(apirouter.urls))]
