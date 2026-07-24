from django.views.generic import TemplateView, ListView
from projects.models import Category
from .models import Technology

class ServicesView(TemplateView):
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('technologies').all()
        context['technologies'] = Technology.objects.all()
        return context


class TechnologiesView(ListView):
    model = Technology
    template_name = "services/technologies.html"
    context_object_name = "technologies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass categories to let template group technologies by category
        context['categories'] = Category.objects.prefetch_related('technologies').all()
        return context
