from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from shows.models import Show, Genre



class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Genre.objects.all().count()
        al = Show.objects.all()

        ctx = {'genre_count': mc, 'show_list': al}
        return render(request, 'shows/show_list.html', ctx)


class GenreView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Genre.objects.all()
        ctx = {'genre_list': ml}
        return render(request, 'shows/genre_list.html', ctx)

#For Show
class ShowCreate(LoginRequiredMixin, CreateView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


#For Genre
class GenreCreate(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


class GenreDelete(LoginRequiredMixin, DeleteView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('shows:all')