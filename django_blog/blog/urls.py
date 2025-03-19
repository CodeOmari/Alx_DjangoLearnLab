from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('logout/', views.signout_user, name="logout"),
    path('login/', UserLoginView.as_view(template_name='login.html'), name='login'),

    path('profile/', views.profile_view, name="profile"),
]