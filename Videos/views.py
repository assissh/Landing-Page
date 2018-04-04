# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Video Here

class VideoCreateView(LoginRequiredMixin, CreateView):
    model = models.Video
    template_name = 'Video/Video_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Video_My_Video','Video_Owned_By']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Video_Owned_By = self.request.user
        return super().form_valid(form)

# Video Details Here


class VideoDetailView(LoginRequiredMixin, DetailView):
    model = models.Video
    template_name = 'Video/Video_details.html'
    login_url = 'login'

# Video ListView Here


class VideoListView(ListView):
    model = models.Video
    template_name = 'Video/Video_list.html'
    login_url = 'login'

# Video Update Here


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Video

    # Decide fields for editing Here

    fields = ['Video_My_Video','Video_Owned_By']
    template_name = 'Video/Video_update.html'
    login_url = 'login'

# Video Delete here


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Video
    template_name = 'Video/Video_delete.html'
    success_url = reverse_lazy('Video_list')
    login_url = 'login'





# Create your views here.
