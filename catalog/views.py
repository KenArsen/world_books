from django.shortcuts import render
from catalog import models
from django.views import generic


class BookListView(generic.ListView):
    model = models.Book
    paginate_by = 1
    template_name = 'catalog/book_list.html'


class AuthorListView(generic.ListView):
    model = models.Author
    paginate_by = 3
    template_name = 'catalog/author_list.html'


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'catalog/book_detail.html'


class AuthorDetailView(generic.DetailView):
    model = models.Author
    template_name = 'catalog/author_detail.html'


def index(request):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter(status__exact=1).count()
    num_authors = models.Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instance': num_instances,
        'num_instance_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context=context)
