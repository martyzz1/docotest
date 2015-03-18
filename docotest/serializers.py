from models.resolution import Resolution
from models.user import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers


#don't forget the api namespace, if decide to user hyperlinked serialiser later e.g. view_name='api:resolution-list' 

class ResolutionSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Resolution
        read_only_fields = ('created', 'last_modified',)
        fields = ('author', 'description', 'created', 'last_modified')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('user')
        fields = ('dob')


class UserSerializer(serializers.ModelSerializer):
    resolutions = ResolutionSerializer(many=True, read_only=True)
    user_profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'resolutions', )
