from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.


class SoloPostView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        result = request.session.get("result", False)
        ctx = {}

        return render(request, 'solo/solo.html', {"result": result})


    def post(self, request):
        ctx = request.POST

        newfield1 = ctx['field1'].strip()
        newfield1 = newfield1[::-1].title()

        newfield2 = ctx['field2'].strip()
        newfield2 = newfield2[::-1].title()
        return render(request, 'solo/solo.html', {'field1': newfield2, 'field2': newfield1})
