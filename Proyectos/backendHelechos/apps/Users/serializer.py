from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.Users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('usuario','correo','nombre','apellidos')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['contrasena'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('usuario', 'correo', 'nombre', 'apellidos')

class PasswordSerializer(serializers.Serializer):
    contrasena = serializers.CharField(max_length=128, min_length=6, write_only=True)
    contrasena2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['contrasena'] != data['contrasena2']:
            raise serializers.ValidationError(
                {'contrasena':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombre': instance['nombre'],
            'usuario': instance['usuario'],
            'correo': instance['correo']
        }