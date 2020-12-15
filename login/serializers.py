from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import MyUser


class MyUserCreateSerializer(serializers.ModelSerializer):
    """
    Miniserializer for user creation purposes only
    """
    class Meta:
        model = MyUser
        fields = ('username', 'password',)


class MyUserLoginSerializer(serializers.ModelSerializer):
    """
    General purpose user serializer
    """
    avatar = serializers.ImageField(required=False)

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        if not user.is_authenticated or instance.pk != user.pk:
            raise ValidationError('You can only change your user', code=401)
        return super(MyUserLoginSerializer, self).update(instance, validated_data)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'avatar', 'email', 'first_name', 'last_name', 'pk')
