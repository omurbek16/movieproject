from datetime import date
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and Directors'
        verbose_name_plural = 'Actors and Directors'


class Genre(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField(max_length=155)
    tagline = models.CharField(max_length=155)
    description = models.TextField()
    poster = models.ImageField(upload_to='movie/')
    year = models.PositiveIntegerField(default=2022)
    country = models.CharField(max_length=155)
    directors = models.ManyToManyField(Actor, verbose_name='Director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actor', related_name='film_actor')
    genres = models.ManyToManyField(Genre, related_name='Genre')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='Submit in US Dollars')
    fees_in_usa = models.PositiveIntegerField(default=0, help_text='Submit in US Dollars')
    fees_in_world = models.PositiveIntegerField(default=0, help_text='Submit in US Dollars')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(unique=True, max_length=155)
    draft = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug':self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shots from Movie'
        verbose_name_plural = 'Shots from Movie'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'

class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=155)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.movie}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
