from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('activities/', views.activity_index, name='activity-index'),
    path('activities/<int:activity_id>/', views.activity_detail, name='activity-detail'),
    path('activities/create/', views.ActivityCreate.as_view(), name='activity-create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity-update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('activities/<int:activity_id>/add-photo/', views.add_photo, name='add-photo'),
]