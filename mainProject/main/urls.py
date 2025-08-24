from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # ← маршрут главной страницы
    path('about/', views.about, name='about'),
]
