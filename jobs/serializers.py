from rest_framework import serializers
from jobs.models import Job, Script, Input, Family, Parameter


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('source_uri', 'destination_path', 'action')


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ('source_uri', 'destination_path')


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
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
            'value',
            )


class FamilySerializer(serializers.ModelSerializer):
    parameters = ParameterSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = ('label', 'name', 'parameters')


class JobSerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True, read_only=True)
    inputs = InputSerializer(many=True, read_only=True)
    families = FamilySerializer(many=True, read_only=True)

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
            'families',
            )
