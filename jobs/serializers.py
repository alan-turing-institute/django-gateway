from rest_framework import serializers
from jobs.models import Job, Script

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('source_uri', 'destination_path', 'action')


class JobSerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ('creation_datetime', 'description', 'scripts')
