from django.urls import path, re_path
from .views import MainView, SingleView, NewArticle

urlpatterns = [
    path('', MainView.as_view()),
    path('create/', NewArticle.as_view()),
    re_path("(?P<article_link>[^/]*)/?", SingleView.as_view()),
]

