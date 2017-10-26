from django.db import models

# define base abstract model classes, to be inherited


class Case(models.Model):
    uri = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    job = models.OneToOneField(
        'JobTemplate',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='case'
    )

    class Meta:
        pass


class JobBase(models.Model):
    backend_identifier = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    uri = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True


class ScriptBase(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)
    action = models.CharField(max_length=20)

    class Meta:
        abstract = True


class InputBase(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)

    class Meta:
        abstract = True


class FamilyBase(models.Model):
    # collapse = models.BooleanField()
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class ParameterBase(models.Model):
    enabled = models.BooleanField()
    help = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    max_value = models.FloatField()
    min_value = models.FloatField()
    step = models.FloatField()

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    type_value = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    value = models.FloatField()

    class Meta:
        abstract = True


class JobTemplate(JobBase):
    creation_datetime = models.DateTimeField(
        auto_now_add=False, null=True)
    start_datetime = models.DateTimeField(
        auto_now_add=False, null=True)
    end_datetime = models.DateTimeField(
        auto_now_add=False, null=True)


class ScriptTemplate(ScriptBase):
    job = models.ForeignKey(JobTemplate, related_name='scripts', on_delete=models.CASCADE, null=True)


class InputTemplate(InputBase):
    job = models.ForeignKey(JobTemplate, related_name='inputs', on_delete=models.CASCADE, null=True)


class FamilyTemplate(FamilyBase):
    job = models.ForeignKey(JobTemplate, related_name='families', on_delete=models.CASCADE, null=True)


class ParameterTemplate(ParameterBase):
    family = models.ForeignKey(FamilyTemplate, related_name='parameters', on_delete=models.CASCADE, null=True)
