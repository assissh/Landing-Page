
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of Video : Video_list

    path('', views.VideoListView.as_view(), name='Video_list'),

    # Path to create new Video : Video_new

    path('new/', views.VideoCreateView.as_view(), name='Video_new'),

    # Path to edit Video : edit_list

    path('<int:pk>/edit', views.VideoUpdateView.as_view(), name='Video_update'),

    # Path to delete Video : Video_delete

    path('<int:pk>/delete', views.VideoDeleteView.as_view(), name='Video_delete'),

    # Path to detail view of Video : Video_details

    path('<int:pk>', views.VideoDetailView.as_view(), name='Video_details')
]
