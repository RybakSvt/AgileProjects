from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path, include


urlpatterns = [
    path('tags/', include('projects.urls.tag')),
    path('tasks/', include('projects.urls.task')),
    path('projects/', include('projects.urls.project')),
    path('project_files/', include('projects.urls.project_file')),
    path('users/', include('users.urls')),
    path('login/', obtain_auth_token),
    path('jwt_login/', TokenObtainPairView.as_view()),
    path('jwt_refresh/', TokenRefreshView.as_view()),


]
