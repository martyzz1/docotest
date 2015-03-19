from models.resolution import Resolution
from models.user import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers

#don't forget the api namespace, if decide to user hyperlinked serialiser later e.g. view_name='api:resolution-list'


class UserProfileSerializer(serializers.ModelSerializer):

    #resolutions = ResolutionSerializer(read_only=True)
    class Meta:
        model = UserProfile
        exclude = ('user')
        fields = ('dob')


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'user_profile', )


class ResolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resolution
        read_only_fields = ('author', 'created', 'last_modified',)
        fields = ('id', 'author', 'description', 'created', 'last_modified')
