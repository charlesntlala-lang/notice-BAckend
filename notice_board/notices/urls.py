from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', views.admin_dashboard, name='admin'),
    path('create/', views.notice_create, name='create'),
    path('<int:pk>/update/', views.notice_update, name='update'),
    path('<int:pk>/delete/', views.notice_delete, name='delete'),
]
