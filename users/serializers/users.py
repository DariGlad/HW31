from rest_framework import serializers

from users.models import Location, User
from users.validators import CheckBirthDate


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )
    total_ads = serializers.IntegerField(default=0)

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )
    birth_date = serializers.DateField(validators=[CheckBirthDate(age=9)])

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc_name in self._location:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(loc)

        return user

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.age = validated_data.get("age", instance.age)
        instance.role = validated_data.get("role", instance.role)
        for loc_name in self._location:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            instance.location.add(loc)

        return instance

    class Meta:
        model = User
        fields = "__all__"


class UserAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username"
        ]
