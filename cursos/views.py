from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


"""
API V1
"""


#Essa função lista e insere(GET e POST)
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


#Essa função deleta e atualiza(DELETE e PUT)
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


#Essa função lista e insere(GET e POST)
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


#Essa função deleta e atualiza(DELETE e PUT)
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

