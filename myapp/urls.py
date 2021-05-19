from django.conf.urls import url, re_path
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(\d+)$', views.BookDetailView.as_view(), name='book-detail'),]