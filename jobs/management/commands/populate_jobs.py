from django.core.management.base import BaseCommand
from jobs.models import Job, Script, Input, Family, Parameter


class Command(BaseCommand):
    args = ''
    help = 'Populate jobs database with test data'

    def _create_jobs(self):

        # create a job
        job = Job(
            name='test job',
            description='test description',
            status='test status',
            uri='test uri',
            user='test user',
            )
        job.save()

        # create a script
        script = Script(
            source_uri='test source_uri',
            destination_path='test destination_path',
            action='test action',
        )
        script.save()

        # add the script to the job
        job.scripts.add(script)

        input_ = Input(
            source_uri='test source_uri',
            destination_path='test destination_path',
        )
        input_.save()
        job.inputs.add(input_)

        # create a family
        family = Family(
            # collapse=True,
            label='test_label',
            name='test_name'
        )
        family.save()

        # create a parameter
        parameter = Parameter(
            enabled=False,
            help='test help',
            label='test label',
            max_value=10.0,
            min_value=0.0,
            step=0.1,
            name='test name',
            type='test type',
            type_value='test type_value',
            units='test units',
            value=3.0,
        )
        parameter.save()

        family.parameters.add(parameter)
        family.save()
        job.families.add(family)

        job.save()


    def handle(self, *args, **options):
        self._create_jobs()
