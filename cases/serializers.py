from rest_framework import serializers
from cases.models import Case, JobTemplate, InputTemplate, ScriptTemplate


class ScriptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptTemplate
        fields = ('source_uri', 'destination_path', 'action')


class InputTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputTemplate
        fields = ('source_uri', 'destination_path')


class JobTemplateSerializer(serializers.ModelSerializer):
    scripts = ScriptTemplateSerializer(many=True, read_only=True)
    inputs = InputTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = JobTemplate
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


class CaseSerializer(serializers.ModelSerializer):
    job = JobTemplateSerializer(many=False, read_only=True)

    class Meta:
        model = Case
        fields = (
            'uri',
            'label',
            'thumbnail',
            'description',
            'job'
            )
