from django.urls import include, path, re_path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='book_list'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='author_list'),
    re_path(r'^authors/add/$', views.AuthorAddView.as_view(), name='author_add'),
    re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book_detail'),
    re_path(r'^books/delete/(?P<pk>\d+)/$', views.delete_book, name='book_delete'),
    re_path(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    re_path(r'^authors/delete/(?P<pk>\d+)/$', views.delete_author, name='author_delete'),
    re_path(r'^mybooks/(?P<pk>\d+)$', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
]
