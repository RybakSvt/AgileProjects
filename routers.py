from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('tags/', include('projects.urls.tag')),
    path('tasks/', include('projects.urls.task')),
    path('projects/', include('projects.urls.project')),
    path('project_files/', include('projects.urls.project_file')),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
]
