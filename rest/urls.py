from django.urls import path
from rest.views import (userDetailsView, UserGenericView, UserCreateView,
                        UserListCreateView)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'rest'

urlpatterns = [
    path('', userDetailsView.as_view(), name='user-detail'),
    path('api/token', obtain_auth_token, name='get-token'),
    path('api/generic', UserGenericView.as_view(), name='generic'),
    path('api/create', UserCreateView.as_view(), name='create'),
    path('api/list-create', UserListCreateView.as_view(), name='list-create'),






]
