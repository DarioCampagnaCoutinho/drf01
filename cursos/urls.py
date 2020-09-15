from django.urls import path
from .views import (
                    CursosAPIView,
                    AvaliacoesAPIView,
                    CursoAPIView,
                    AvaliacaoAPIView)


urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]