from rest_framework import serializers
from .models import MovieModels, GenreModels, ReviewModels, CommentModels
from django.contrib.auth.models import User
import ipdb



class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # read_only=True ignora o id no post e usa no get
    name = serializers.CharField()


class UserSerlializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewModels
        exclude = ["movie"]
        # depth = 1

    stars = serializers.IntegerField(min_value=1, max_value=10)
    critic = UserSerlializer(read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModels
        fields = ["id", "user", "comment"]
    user = UserSerlializer(read_only=True)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModels
        fields = ["id", "title", "duration", "genres", "launch", "classification", "synopsis", "criticism_set", "comment_set"]


    criticism_set = ReviewSerializer(read_only=True, many=True, source='reviewmodels_set')
    comment_set = CommentSerializer(read_only=True, many=True, source='commentmodels_set')

    genres = GenreSerializer(many=True) # many=True para lista
    def create(self, validated_data):
        data = validated_data
        genres = data.pop("genres")
        movies = MovieModels.objects.get_or_create(**data)[0]
        for genre in genres:
            genre_created = GenreModels.objects.get_or_create(**genre)[0]
            movies.genres.add(genre_created)

        return movies













