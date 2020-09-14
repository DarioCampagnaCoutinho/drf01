from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
       Curso de Api
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)#Muitos cursos
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
       Avaliação de Api
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)#Muitos cursos
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
