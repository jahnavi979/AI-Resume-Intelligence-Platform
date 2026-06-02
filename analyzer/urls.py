from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .auth_views import signup_view

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('analyze/', views.analyze_resume, name='analyze_resume'),
    path('history/', views.history, name='history'),
    path('report/<int:analysis_id>/', views.report, name='report'),

    path('signup/', signup_view, name='signup'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='analyzer/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]