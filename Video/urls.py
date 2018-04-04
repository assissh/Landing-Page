
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of images : images_list

    path('', views.VideoListView.as_view(), name='images_list'),

    # Path to create new images : images_new

    path('new/', views.VideoCreateView.as_view(), name='images_new'),

    # Path to edit images : edit_list

    path('<int:pk>/edit', views.VideoUpdateView.as_view(), name='images_edit'),

    # Path to delete images : images_delete

    path('<int:pk>/delete', views.VideoDeleteView.as_view(), name='images_delete'),

    # Path to detail view of images : images_details

    path('<int:pk>', views.VideoDetailView.as_view(), name='images_details')
]
