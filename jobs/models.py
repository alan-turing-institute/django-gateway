from django.db import models


class Job(models.Model):
    backend_identifier = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    uri = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    creation_datetime = models.DateTimeField(
        auto_now_add=True)
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


class Script(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)
    action = models.CharField(max_length=20)

    job = models.ForeignKey(Job, related_name='scripts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " ".join([self.source_uri, self.destination_path, self.action])

    class Meta:
        pass


class Input(models.Model):
    source_uri = models.CharField(max_length=200)
    destination_path = models.CharField(max_length=200)

    job = models.ForeignKey(Job, related_name='inputs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " ".join([self.source_uri, self.destination_path])

    class Meta:
        pass
