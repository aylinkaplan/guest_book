from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from backend import views

urlpatterns = [
    path('auth/register/', views.UserCreate.as_view(), name='auth-register'),
    path('auth/login/', obtain_auth_token, name='auth-login'),
    path("list/", views.ListAPIView.as_view(), name="guestbook_list"),
    path("list/<int:pk>/", views.RetrieveAPIView.as_view(), name="guestbook_detail"),
    path("create/", views.CreateAPIView.as_view(), name="guestbook_create"),
    path("update/<int:pk>/", views.UpdateAPIView.as_view(), name="guestbook_update"),
    path("delete/<int:pk>/", views.DeleteAPIView.as_view(), name="guestbook_delete")
]
