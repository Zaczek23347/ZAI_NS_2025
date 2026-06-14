from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class BulkImportView(APIView):

    def post(self, request):
        serializer = PersonSerializer(
            data=request.data,
            many=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Import successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )