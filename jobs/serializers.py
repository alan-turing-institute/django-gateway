from rest_framework import serializers
from jobs.models import Job, Script, Input


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('source_uri', 'destination_path', 'action')


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ('source_uri', 'destination_path')


class JobSerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True, read_only=True)
    inputs = InputSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = (
            'name',
            'backend_identifier',
            'description',
            'status',
            'uri',
            'user',
            'creation_datetime',
            'start_datetime',
            'end_datetime',
            'scripts',
            'inputs',
            )
