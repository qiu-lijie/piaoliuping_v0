from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from .models import Bottle


class BottlePage(LoginRequiredMixin, TemplateView):
    template_name = 'rand_bottle.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['bottle'] = Bottle.pick_random_bottle(self.request.user.pk)
        return context
