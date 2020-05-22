from django.db import models
from rest_framework import serializers
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField('time user created')

class Commit(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hash = models.BinaryField(max_length=49, unique=True) #SHA1 is 160 bits or 49 decimal digits
    created = models.DateTimeField('time commit created')
    file = models.FileField(blank=True) #django docs suggest using ModelFormWithFileField in views

class BaseMetric(models.Model):
    class Meta:
        abstract = True
    parent_file = models.ForeignKey(Commit, related_name="metrics", on_delete=models.CASCADE) #now Commit has a field called metrics
    title = models.CharField(max_length=128)
    value = models.CharField(max_length=128, blank=True)
class Metric(BaseMetric):
    isNumeric = models.BooleanField(default=True)
    #numericValue = models.FloatField(null=True) #should only be null when isNumeric is False
#class NumericMetric(BaseMetric): #for now this model is not used, instead isNumeric is added to the Metric class
#    value = models.FloatField() #we could later avoid floating point problems by switching to DecimalField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        exclude = ['file', ] # for now, until we figure out how to deal with uploads
    metrics = serializers.HyperlinkedRelatedField(many=True, queryset=Metric.objects.all(), view_name='metric-detail') #all the metrics related to this commit
#TODO: metrics can get added to each commit. when showing in a table, how to handle too many columns? Edit metrics through API?
