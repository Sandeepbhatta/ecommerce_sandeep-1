from django.urls import path
from .views import index1, about
urlpatterns = [
    path('', index1),
    path('about', about),

]
