from django.shortcuts import render
from catalog import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import AuthorAddForm, AuthorDetailForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect


# Book

class BookListView(ListView):
    model = models.Book
    paginate_by = 1
    template_name = 'catalog/book_list.html'


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'catalog/book_detail.html'


def delete_book(request, pk):
    book = models.Book.objects.get(id=pk)
    book.delete()
    return redirect('catalog:book_list')


# Author

class AuthorListView(ListView):
    model = models.Author
    paginate_by = 3
    template_name = 'catalog/author_list.html'


class AuthorDetailView(UpdateView):
    model = models.Author
    form_class = AuthorDetailForm
    template_name = 'catalog/author_detail.html'

    def get_success_url(self):
        return reverse_lazy('catalog:author_detail', args=(self.object.id,))


class AuthorAddView(SuccessMessageMixin, CreateView):
    model = models.Author
    form_class = AuthorAddForm
    template_name = 'catalog/author_add.html'
    success_url = reverse_lazy('catalog:author_list')
    success_message = 'Успешно зарегестрирован!'


def delete_author(request, pk):
    author = models.Author.objects.get(id=pk)
    author.delete()
    return reverse_lazy('catalog:author_list')


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


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.
    """
    model = models.BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 3

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(status='2').order_by('due_back')
