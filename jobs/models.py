from django.db import models
from cases.models import JobBase, ScriptBase, InputBase, FamilyBase, ParameterBase


class Job(JobBase):
    user = models.CharField(max_length=200, null=True)
    creation_datetime = models.DateTimeField(
        auto_now_add=True)
    start_datetime = models.DateTimeField(
        auto_now_add=False, null=True)
    end_datetime = models.DateTimeField(
        auto_now_add=False, null=True)


class Script(ScriptBase):
    job = models.ForeignKey(Job, related_name='scripts', on_delete=models.CASCADE, null=True)


class Input(InputBase):
    job = models.ForeignKey(Job, related_name='inputs', on_delete=models.CASCADE, null=True)


class Family(FamilyBase):
    job = models.ForeignKey(Job, related_name='families', on_delete=models.CASCADE, null=True)


class Parameter(ParameterBase):
    family = models.ForeignKey(Family, related_name='parameters', on_delete=models.CASCADE, null=True)
