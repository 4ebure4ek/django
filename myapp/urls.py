from django.urls import path
from .views import home, admin_only

urlpatterns = [
    path('', home, name='home'),
    path('admin-page/', admin_only, name='admin_page'),
]
