
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Image : Image_list

    path('', views.ImageListView.as_view(), name='Image_list'),

    # Path to create new Image : Image_new

    path('new/', views.ImageCreateView.as_view(), name='Image_new'),

    # Path to edit Image : edit_list

    path('<int:pk>/edit', views.ImageUpdateView.as_view(), name='Image_edit'),

    # Path to delete Image : Image_delete

    path('<int:pk>/delete', views.ImageDeleteView.as_view(), name='Image_delete'),

    # Path to detail view of Image : Image_details

    path('<int:pk>', views.ImageDetailView.as_view(), name='Image_details')
]
