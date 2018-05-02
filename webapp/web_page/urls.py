# web_page/urls.py
from django.conf.urls import url
from web_page import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^draw/$', views.DrawPageView.as_view()), # Add this /draw/ route
]
