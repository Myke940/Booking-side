from django.urls import path
from bookingapp import views

urlpatterns = [
    path('', views.problemslist, name = 'problemslist'),
    path('book/', views.bookmeeting, name = 'bm' ),
    path('list', views.meetinghistory, name = 'history'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.login_user, name = 'login'),
    path('register/', views.register_user, name = 'register'),
]

