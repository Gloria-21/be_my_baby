from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('admin/', admin.site.urls),
]