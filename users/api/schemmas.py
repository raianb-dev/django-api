from rest_framework import viewsets
from users.api import serializers
from users import models


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.users.objects.all()
    
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovieSerializer
    queryset = models.movie.objects.all()