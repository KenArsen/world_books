from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='book_list'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='author_list'),
    re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
]
