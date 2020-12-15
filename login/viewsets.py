from rest_framework import viewsets, permissions, mixins

from .models import MyUser

from .serializers import MyUserLoginSerializer


class MyUserViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    MyUser model viewset: Does not allow deleting or creating /api/users/
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = MyUser.objects.all()
    serializer_class = MyUserLoginSerializer


class MyUserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Viewset for creating users /api/singup/
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserLoginSerializer

