from django.db import models
from django.utils import timezone
from rest_framework import serializers
from hashlib import sha1
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    contributing_users = models.ManyToManyField('User')

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField('time user created', auto_now_add=True)

class Commit(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hash = models.BinaryField(max_length=49, unique=True) #SHA1 is 160 bits or 49 decimal digits
    created = models.DateTimeField('time commit created', auto_now_add=True)
    file = models.FileField(blank=True) #django docs suggest using ModelFormWithFileField in views
    def save(self, *args, **kwargs):
        if not self.pk: # only run before record is first created
            self.created = timezone.now() # the result of auto_now_add field is not present when calculating the hash
        hasher = sha1()
        hasher.update(self.author.username.encode('utf-8'))
        hasher.update(self.project.name.encode('utf-8'))
        hasher.update(str(self.created).encode('utf-8'))
        if self.file:
            hasher.update(self.file.path.encode('utf-8')) # TODO actually hash the file contents, also
        self.hash = hasher.digest()
        super().save(*args, **kwargs)

class BaseAttribute(models.Model):
    class Meta:
        default_related_name = "%(model_name)ss" # used by the CommitSerializer to find metrics/properties pointing back to the commit
        abstract = True
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
class NumericMetric(BaseAttribute):
    value = models.FloatField()
class TextMetric(BaseAttribute):
    value = models.CharField(max_length=128, blank=True)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ['created', ] #TODO how to allow GETting this field but not POSTing it?
class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        exclude = ['file', ] # for now, until we figure out how to deal with uploads
    numericmetrics = serializers.HyperlinkedRelatedField(many=True, view_name='numericmetric-detail', read_only=True) #all the metrics related to this commit
    textmetrics = serializers.HyperlinkedRelatedField(many=True, view_name='textmetric-detail', read_only=True) 
#TODO: metrics can get added to each commit. when showing in a table, how to handle too many columns? Edit metrics through API?
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class NumericMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericMetric
        fields = '__all__'
class TextMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMetric
        fields = '__all__'
