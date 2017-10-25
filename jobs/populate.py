from models import Job
from serializers import JobSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

job = Job(name="Test")
print(job)
# job.save()
