from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Bottle


class BottlePage(LoginRequiredMixin, TemplateView):
    template_name = 'rand_bottle.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['bottle'] = Bottle.pick_random_bottle(self.request.user.pk)
        return context


class CreateBottlePage(LoginRequiredMixin, CreateView):
    template_name = 'bottle_form.html'
    model = Bottle
    fields = ['content']
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)
