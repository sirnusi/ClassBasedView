from django.urls import path
from .views import Home, SchoolDetailView, SchoolListView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('school_list/', SchoolListView.as_view(), name='list'),
    path('school_detail/<int:pk>/', SchoolDetailView.as_view(), name='detail'),
    path('create_school/', SchoolCreateView.as_view(), name='create'),
    path('update_school/<int:pk>/', SchoolUpdateView.as_view(), name='update'),
    path('delete_school/<int:pk>/', SchoolDeleteView.as_view(), name='delete'),
]