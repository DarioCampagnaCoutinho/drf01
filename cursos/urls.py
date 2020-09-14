from django.urls import path
from .views import CursoAPIView


urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
]