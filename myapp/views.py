from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from django.views import generic

# Create your views here.
def register(request):
    context = {}
    return render(request, "register.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)


from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.filter(title__iexact='ROmE').count()
    num_instances=BookInstance.objects.all().count()
    num_genre = Genre.objects.filter(name__iexact='fantasy').count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'genre_count':num_genre},
    )



class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.all() # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'myapp/book_list.html'
    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.ListView):
    model = Book

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

            # book_id=get_object_or_404(Book, pk=pk)

        return render(request, 'book_detail.html',context={'book': book_id,})
