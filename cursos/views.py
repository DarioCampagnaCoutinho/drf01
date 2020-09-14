from rest_framework.views import APIView
from rest_framework.response import Response

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
