from django.shortcuts import render
from .models import Team
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors},
    )


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    
    context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.all()
    #print(queryset)
    
    def get_queryset(self):
        return Book.objects.all() # Get 5 books containing the title war
    
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        #ontext['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
