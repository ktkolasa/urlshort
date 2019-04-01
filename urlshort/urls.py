from django.urls import path

from . import views

urlpatterns = [
    path('results', views.results, name='results'),
    path('', views.index, name='index'),
    path('<short_url>', views.redirect_to_full_url, name='redirect_to_full_url')
]