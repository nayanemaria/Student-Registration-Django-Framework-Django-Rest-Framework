from msilib.schema import Patch
from django.urls import path

from . import views

urlpatterns = [
    path('', views.form, name='cadastrar_aluno'),
    path('delete/<int:id>', views.delete_aluno, name='delete'),
    path('update/<int:id>', views.update_aluno, name='update'),
]