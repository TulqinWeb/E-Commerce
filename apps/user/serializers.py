from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
        ]

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Parollar mos emas!"})

        phone_number = attrs.get('phone_number')
        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({"phone_number": "Ushbu telefon raqam orqali ro'yxatdan o'tilgan!"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            **validated_data,
            password=password,
        )
        return user


class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if not phone_number:
            raise serializers.ValidationError("Telefon raqam kiriting!")

        user = User.objects.filter(phone_number=phone_number).first()

        if not user:
            raise serializers.ValidationError("Foydalanuvchi topilmadi!")

        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto'g'ri")

        attrs['user'] = user
        return attrs


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True, help_text="Refresh Token")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'role',
        ]
