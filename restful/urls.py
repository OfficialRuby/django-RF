from django.contrib import admin
from django.urls import path, include
from rest.views import userDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest.urls', namespace='rest')),
    path('rest-auth/', include('rest_auth.urls'))


]
