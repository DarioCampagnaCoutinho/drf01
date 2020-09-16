from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
                    CursosAPIView,
                    AvaliacoesAPIView,
                    CursoAPIView,
                    AvaliacaoAPIView,
                    AvaliacoesDeUmCursoAPIView,
                    UmaAvaliacaoDeUmCursoAPIView,
                    CursoViewSet,
                    AvaliacaoViewSet)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

    path('curso/<int:curso_pk>/avaliacoes/', AvaliacoesDeUmCursoAPIView.as_view(), name='curso_avaliacoes'),
    path('curso/<int:curso_pk>/avaliacao/<int:avaliacao_pk>/', UmaAvaliacaoDeUmCursoAPIView.as_view(), name='curso_avaliacao'),
]