from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username','first_name', 'last_name', 'password', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}} # extra_kwargs para sobrescrever o comportamento padrão, para não aparecer o password no return

    # password = serializers.CharField(read_only=True)

    #sobrescrever o metodo create, validated_data como se fosse o request.data
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
