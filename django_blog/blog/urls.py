from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('logout/', views.signout_user, name="logout"),
    path('login/', UserLoginView.as_view(template_name='login.html'), name='login'),

    path('profile/', views.profile_view, name="profile"),


    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]