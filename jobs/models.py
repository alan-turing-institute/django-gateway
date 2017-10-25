from django.db import models

class Job(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('creation_datetime', 'description',)


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


# If `related_name` is absent, then the reverse attribute is called `script_set`
