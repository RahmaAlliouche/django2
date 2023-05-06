from django.urls import path
from . import views
from .views import RegisterView
from .views import LoginView
from .views import UserView

urlpatterns = [
    
    path('',views.responce),
    #path('up/',views.signUp),
    #path('upp/',views.signin),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
     path('user/', UserView.as_view()),
    
  
]