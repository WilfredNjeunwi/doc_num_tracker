from django.urls import path
from .views import download_file, get_num_download

urlpatterns = [
    path('download/', download_file, name='download_file'),
    path('download_count/', get_num_download, name='get_num_download'),
]