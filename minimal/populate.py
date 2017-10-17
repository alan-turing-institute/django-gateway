# from jobs.models import Job, Script
# from jobs.serializers import JobSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
#
# job = Job.objects.create(description='job description')
# Script.objects.create(job=job, description="script description")
# Script.objects.create(job=job, description="another description")
#
# serializer = JobSerializer(instance=job)
# content = JSONRenderer().render(serializer.data)



from jobs.models import Job, Script
from jobs.serializers import JobSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

script = Script(source_uri='source 1', destination_path='path 1', action='RUN')
script.save()

job = Job(description='job description')
job.save()

job.scripts.add(script)
# job.save()

serializer = JobSerializer(instance=job)
content = JSONRenderer().render(serializer.data)
