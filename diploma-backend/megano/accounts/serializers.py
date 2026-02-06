from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Image



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'src', 'alt'
        ]



class ProfileeSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'avatar', 'email', 'phone', 'fullName'
        ]


    def get_avatar(self, obj):
        image = obj.avatar
        if image:
            return ImageSerializer(image).data
        return None