from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = models.users
       fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movie
        fields = '__all__'