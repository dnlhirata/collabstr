from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView

from contents.models import Content


class IndexView(ListView):
    template_name = 'home/index.html'

    def dispatch(self, request, *args, **kwargs):
        self.platform = request.GET.get('platform', None)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Content.objects.all().select_related('creator')
        if self.platform:
            qs = qs.filter(creator__platform=self.platform)
        
        return qs[:30]

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()

        if self.platform is not None:
            template_names = ['home/content_list.html']
        
        return template_names