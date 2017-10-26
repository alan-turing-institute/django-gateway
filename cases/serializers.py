from rest_framework import serializers
from cases.models import (
    Case, JobTemplate, InputTemplate, ScriptTemplate,
    FamilyTemplate, ParameterTemplate
    )


class ScriptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptTemplate
        fields = ('source_uri', 'destination_path', 'action')


class InputTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputTemplate
        fields = ('source_uri', 'destination_path')


class ParameterTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterTemplate
        fields = (
            'enabled',
            'help',
            'label',
            'max_value',
            'min_value',
            'step',
            'name',
            'type',
            'type_value',
            'units',
            'value'
            )


class FamilyTemplateSerializer(serializers.ModelSerializer):
    parameters = ParameterTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = FamilyTemplate
        fields = (
            # 'collapse',
            'label',
            'parameters')


class JobTemplateSerializer(serializers.ModelSerializer):
    scripts = ScriptTemplateSerializer(many=True, read_only=True)
    inputs = InputTemplateSerializer(many=True, read_only=True)
    families = FamilyTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = JobTemplate
        fields = (
            'name',
            'backend_identifier',
            'description',
            'status',
            'uri',
            'creation_datetime',
            'start_datetime',
            'end_datetime',
            'scripts',
            'inputs',
            'families'
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
