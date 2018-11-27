from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre


class UserData(dict):
    def __init__(self, *args, **kwargs):
        super(UserData, self).__init__(*args, **kwargs)
        self['a'] = 'aaaa'
        self['b'] = 2

def index(request):
    '''View function for home page of site.'''

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'data': UserData(),
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
