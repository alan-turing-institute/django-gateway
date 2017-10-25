from django.core.management.base import BaseCommand
from jobs.models import Job, Script, Input

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


        job.save()



    def handle(self, *args, **options):
        self._create_jobs()
