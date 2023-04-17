from django.urls import path

from todolist.views import index, add, edit, delete, update

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit<int:todo_id>/', edit, name='edit'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('update/<int:todo_id>/', update, name='update'),
]