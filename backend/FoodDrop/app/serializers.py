from .models import *
from rest_framework import serializers

class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = ('request', 'store', 'latitude', 'longitude', 'time',
                'address', 'desired_fee')

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('opening', 'price', 'latitude', 'longitude')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name='null',
                last_name='null'
        )

        user.set_password(validated_data['passwords'])
        user.save()

        return user
