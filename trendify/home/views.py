from django.views.generic import ListView

from contents.models import Content


class IndexView(ListView):
    template_name = 'home/index.html'

    def get_queryset(self):
        return Content.objects.order_by('-creator__rating')[:30]