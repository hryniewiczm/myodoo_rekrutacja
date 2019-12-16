from django.urls import path
from . import views

app_name = 'salary_calc'

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
    path('get_salary', views.get_salary, name='get_salary'),
]
