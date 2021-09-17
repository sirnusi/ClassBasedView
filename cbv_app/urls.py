from django.urls import path
from .views import Home, SchoolDetailView, SchoolListView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('school_list/', SchoolListView.as_view(), name='list'),
    path('school_detail/<int:pk>/', SchoolDetailView.as_view(), name='detail'),
]