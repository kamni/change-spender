from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context(self):
        return {}

# Faked view. Remove later
import simplejson as json
from django.http import HttpResponse
from django.views.generic import View
class KitchenSink(View):
    def get(self, request, *args, **kwargs):
        context = None
