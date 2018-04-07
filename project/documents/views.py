from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from project.dashboard.views import DashboardMixin
from django.http import Http404, HttpResponse, JsonResponse
from .forms import DocumentForm


class HomeView(DashboardMixin, TemplateView):
    """docstring for ClassName"""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = DocumentForm(self.request.POST or None)  # instance= None
        context["form"] = form
        print("xD")
        return context

    def post(self, request, *args, **kwargs):
        data = {'message': True}
        context = self.get_context_data()
        print("POST")
        print(context["form"])
        if request.is_ajax():
            form = context["form"]
            if form.is_valid():
                data["ok"] = 1
        return JsonResponse({'status': 'false', 'message': "No hay palabra"}, status=404)


def obtener_pdf(request):
    """ Función para obtener todas las palabras del diccionario"""
    if request.is_ajax() and request.method == 'GET':
        palabras = []
        return JsonResponse(list(palabras), safe=False)
    else:
        raise Http404
