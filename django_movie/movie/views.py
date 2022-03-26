from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm



class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movie/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect('/')
