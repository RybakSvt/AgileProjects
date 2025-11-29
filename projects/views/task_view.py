from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from projects.models import Task
from projects.serializers import (
    TagSerializer,
    AllTasksSerializer,
    CreateTaskSerializer,
)


class AllTasksListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer
        return CreateTaskSerializer








