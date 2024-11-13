from django.urls import path
from .views import add_comment

urlpatterns = [
    path('tasks/<int:task_id>/add_comment/', add_comment, name='add_comment'),
    # другие пути...
]
