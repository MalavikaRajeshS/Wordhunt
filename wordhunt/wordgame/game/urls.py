from django.urls import path
from .views import home, get_word, check_answers

urlpatterns = [
    path('', home, name='home'),
    path('get_word/<str:level>/', get_word, name='get_word'),
    path('check_answers/', check_answers, name='check_answers'),
]
