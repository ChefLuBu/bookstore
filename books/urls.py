from django.urls import path
from .views import home
from .views import BookListView

app_name = 'books'

#The urlpatterns list is used to map the URL to the view function.
#Each path function takes two arguments: the URL and the view function.
#The route parameter is the URL that the user will type in the browser.
#The view parameter is the view function that will be called when the user
urlpatterns = [
    path('', home),
    path('books/list', BookListView.as_view(), name='book-list')
]


