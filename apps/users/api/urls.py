from django.urls import path

from apps.users.api import views

urlpatterns = [
    path('add-user/', views.UserViews.as_view(), name="create-user"),
    path('update-user/', views.UserViews.as_view(), name="update-user"),
    path('delete-user', views.UserViews.as_view(), name="delete-user"),
    path('view-user', views.UserViews.as_view(), name="view-user"),
]
