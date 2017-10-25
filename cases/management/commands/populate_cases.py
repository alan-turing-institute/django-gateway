from django.core.management.base import BaseCommand
from cases.models import Case, JobTemplate, ScriptTemplate, InputTemplate

class Command(BaseCommand):
    args = ''
    help = 'Populate cases database with test data'


    def _create_cases(self):

        # create a script
        script_template = ScriptTemplate(
            source_uri='test source_uri',
            destination_path='test destination_path',
            action='test action',
        )
        script_template.save()

        input_template = InputTemplate(
            source_uri='test source_uri',
            destination_path='test destination_path',
        )
        input_template.save()


        # create a job template
        job_template = JobTemplate(
            name='test job',
            description='test description',
            status='test status',
            uri='test uri',
            user='test user',
            )
        job_template.save()
        job_template.scripts.add(script_template)
        job_template.inputs.add(input_template)
        job_template.save()

        # create a case
        case = Case(
            uri='test uri',
            label='test label',
            thumbnail='test thumbnail',
            description='test description',
            )

        case.save()

        case.job = job_template
        case.save()


    def handle(self, *args, **options):
        self._create_cases()
