from cases.models import Case
from jobs.serializers import JobSerializer
from cases.serializers import CaseSerializer

from rest_framework import generics
from django.shortcuts import get_object_or_404

from utilities.converters import case_to_job


class CaseList(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseConversionMixin(object):
    def get_object(self):
        case = get_object_or_404(Case, pk=self.kwargs['pk'])
        return case_to_job(case)


class CaseToJob(CaseConversionMixin, generics.RetrieveAPIView):
    queryset = Case.objects.filter()
    serializer_class = JobSerializer
