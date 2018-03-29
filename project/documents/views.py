from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from project.dashboard.views import DashboardMixin
from django.http import Http404, HttpResponse, JsonResponse
from .forms import DocumentForm


class HomeView(DashboardMixin, FormView, TemplateView):
    """docstring for ClassName"""
    form_class = DocumentForm
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        data = {}
        if request.is_ajax():
            form = self.get_form()
            if form.is_valid():
                data["ok"] = 1
        return JsonResponse(data)