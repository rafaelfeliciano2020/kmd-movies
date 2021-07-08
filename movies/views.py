import ipdb
from django.shortcuts import render

import movies.models
from .models import MovieModels, ReviewModels, CommentModels
from .serializers import MovieSerializer, ReviewSerializer, CommentSerializer
from .permissions import AdminCreateOnlyPermisson, ReviewCreateOnlyPermission, CommentCreateOnlyPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView,UpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist



#mixin personalizado
class FilterMovieMixin():
    def get_queryset(self):
        queryset = self.queryset
        movie_filter = {}
        for movie_field in self.movie_fields:
            if self.request.data.get(movie_field):
                movie_filter[f'{movie_field}__icontains'] = self.request.data.get(movie_field)

        queryset = queryset.filter(**movie_filter)
        return queryset

    #GET , POST
class ListCreateMoviesView(FilterMovieMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminCreateOnlyPermisson]
    queryset = MovieModels.objects.all()
    serializer_class = MovieSerializer
    movie_fields = ["title"] #para a filtragem

# GET com id
class RetrieveUpdateDestroyMoviesView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminCreateOnlyPermisson]
    queryset = MovieModels.objects.all()
    serializer_class = MovieSerializer


#Critica
class ListCreateReviewView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewCreateOnlyPermission]

    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializer


    def post(self, request, pk=''):
        #verifica se ja possui um areview deste critico para este filme
        try:
            movie = MovieModels.objects.get(id=pk)  #retorna o filme pelo id passado na url
            review = ReviewModels.objects.filter(movie=movie, critic=request.user)

            #verifica se ja possui alguma critica
            if not len(review):
                review = ReviewModels.objects.get_or_create(**request.data, movie=movie, critic=request.user)[0]  # instancia
                serializer = ReviewSerializer(data=request.data)

                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                serializer = ReviewSerializer(review)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            #se ja possuir uma critica
            else:
                return Response({"detail": "You already made this review."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except ObjectDoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk=''):

        try:
            review = ReviewModels.objects.get(movie_id=pk, critic_id=request.user.id)
        #caso não encontre a critica
        except ObjectDoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        review.stars = request.data['stars']
        review.review = request.data["review"]
        review.spoilers = request.data["spoilers"]
        review.save()

        serializer = ReviewSerializer(review)
        return Response(serializer.data)



class ListCreateCommentView(GenericAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = CommentModels.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, pk=''):
        if not request.user.is_superuser and not request.user.is_staff:
            try:
                movie = MovieModels.objects.get(id=pk)

            except ObjectDoesNotExist:
                return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

            comment = CommentModels.objects.get_or_create(**request.data, movie=movie, user=request.user)[0]
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)
    def put(self,request, pk=''):
        if not request.user.is_superuser and not request.user.is_staff:
            try:
                comment = CommentModels.objects.get(movie_id=pk, id=request.data["comment_id"])
            except ObjectDoesNotExist:
                return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


            comment.comment = request.data["comment"]
            comment.save()
            serializer = CommentSerializer(comment)

            return Response(serializer.data)







