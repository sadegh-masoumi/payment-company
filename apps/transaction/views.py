import json

from django.http import HttpResponse
from django.views.generic import View


class ReportView(View):

    def post(self):
        return HttpResponse
