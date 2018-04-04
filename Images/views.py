# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Image Here

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = models.Image
    template_name = 'Image/Image_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Image_My_Image','Image_Owned_By']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Image_Owned_By = self.request.user
        return super().form_valid(form)

# Image Details Here


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = models.Image
    template_name = 'Image/Image_detail.html'
    login_url = 'login'

# Image ListView Here


class ImageListView(ListView):
    model = models.Image
    template_name = 'Image/Image_list.html'
    login_url = 'login'

# Image Update Here


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Image

    # Decide fields for editing Here

    fields = ['Image_My_Image','Image_Owned_By']
    template_name = 'Image/Image_update.html'
    login_url = 'login'

# Image Delete here


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Image
    template_name = 'Image/Image_delete.html'
    success_url = reverse_lazy('Image_list')
    login_url = 'login'





# Create your views here.
