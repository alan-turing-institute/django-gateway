from django.db import models


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


class JobTemplate(models.Model):
    backend_identifier = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True)
    uri = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, null=True)

    creation_datetime = models.DateTimeField(
        auto_now_add=False, null=True)
    start_datetime = models.DateTimeField(
        auto_now_add=False, null=True)
    end_datetime = models.DateTimeField(
        auto_now_add=False, null=True)

    #
    # def __str__(self):
    #     return self.description

    class Meta:
        pass
        # ordering = ('creation_datetime', 'description',)


class ScriptTemplate(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)
    action = models.CharField(max_length=20)

    job = models.ForeignKey(JobTemplate, related_name='scripts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " ".join([self.source_uri, self.destination_path, self.action])

    class Meta:
        pass


class InputTemplate(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)

    job = models.ForeignKey(JobTemplate, related_name='inputs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " ".join([self.source_uri, self.destination_path])

    class Meta:
        pass


class FamilyTemplate(models.Model):

    collapse = models.BooleanField()
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    job = models.ForeignKey(JobTemplate, related_name='families', on_delete=models.CASCADE, null=True)


class ParameterTemplate(models.Model):

    family = models.ForeignKey(FamilyTemplate, related_name='parameters', on_delete=models.CASCADE, null=True)

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
