from django.shortcuts import render
from .models import *
from rest_framework import viewsets
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
class CommitViewSet(viewsets.ModelViewSet):
    queryset = Commit.objects.all().order_by('created') # TODO add filtering by author and project
    serializer_class = CommitSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('name') # TODO add filtering by project and commit
    serializer_class = PropertySerializer
class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('name')
    serializer_class = MetricSerializer
