from django.db import models
from django.contrib.auth.models import User


class GenreModels(models.Model):
    name = models.CharField(max_length=255)


class MovieModels(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    genres = models.ManyToManyField(GenreModels) # relaçao N x N
    launch = models.CharField(max_length=255)
    classification = models.IntegerField()
    synopsis = models.TextField()



# 1 filme varias criticas
# 1 critica esta relacionado a apenas 1 filme
class ReviewModels(models.Model):
    stars = models.IntegerField()  # intervelo de 1 a 10 ?
    review = models.TextField()
    spoilers = models.BooleanField()
    movie = models.ForeignKey(MovieModels, on_delete=models.CASCADE) # relação de 1 x N
    critic = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentModels(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(MovieModels, on_delete=models.CASCADE)  # relação de 1 x N
    user = models.ForeignKey(User, on_delete=models.CASCADE)




