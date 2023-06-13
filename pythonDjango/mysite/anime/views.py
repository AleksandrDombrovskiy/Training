from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Anime
from .form import ReviewForm


class AnimeView(View):
    """Список аниме"""
    def get(self, request):
        anime = Anime.objects.all()
        return render(request, 'anime/animes.html', {'anime_list': anime})


class AnimeDeteil(View):
    """Представление одной картины"""
    def get(self, request, slug):
        anime = Anime.objects.get(url=slug)
        return render(request, 'anime/anime_detel.html', {'anime': anime})


class AddReview(View):
    """Добавление отзыва"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        anime = Anime.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.anime = anime
            form.save()
        return redirect(anime.get_absolute_url())