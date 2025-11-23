from django.urls import path
from bookingapp import views

urlpatterns = [
    path('', views.problemslist, name = 'problemslist'),
    path('book/', views.bookmeeting, name = 'bm' ),
    path('list', views.meetinghistory, name = 'history'),
    


]