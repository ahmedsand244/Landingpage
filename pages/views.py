from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from projects.models import Project
from services.models import Technology
from .models import FAQ, Testimonial

class HomeView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Load featured projects for the hero/overview section
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:3]
        # Load testimonials & FAQs for quick preview sections
        context['testimonials'] = Testimonial.objects.all()[:3]
        context['faqs'] = FAQ.objects.all()[:4]
        context['technologies'] = Technology.objects.all()[:6]
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"

    def post(self, request, *args, **kwargs):
        # Handle contact submission form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # In a real app we might save this or send mail. Here we show success context.
        context = {
            'success': True,
            'client_name': name,
        }
        return render(request, self.template_name, context)


class FAQView(ListView):
    model = FAQ
    template_name = "pages/faq.html"
    context_object_name = "faqs"


class TestimonialsView(ListView):
    model = Testimonial
    template_name = "pages/testimonials.html"
    context_object_name = "testimonials"
