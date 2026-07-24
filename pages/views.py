from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from projects.models import Project
from services.models import Technology
from .models import FAQ, Testimonial, ContactMessage

class HomeView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Load featured projects for the hero/overview section
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:3]
        # Load real approved testimonials / comments
        context['testimonials'] = Testimonial.objects.filter(is_approved=True).order_by('-created_at', '-id')
        context['faqs'] = FAQ.objects.all()[:4]
        context['technologies'] = Technology.objects.all()[:6]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email', '')
        role_university = request.POST.get('role_university', '')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating', 5)

        if name and review_text:
            try:
                rating = int(rating)
            except ValueError:
                rating = 5
            
            Testimonial.objects.create(
                name=name,
                email=email,
                role_university=role_university or "عميل / طالب",
                review_text=review_text,
                rating=rating,
                is_approved=True
            )

        context = self.get_context_data(**kwargs)
        context['comment_success'] = True
        context['commenter_name'] = name
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and (email or message):
            ContactMessage.objects.create(
                name=name,
                email=email or "غير مدخل",
                subject=subject or "استفسار جديد",
                message=message or "لا تتوفر تفاصيل إضافية"
            )

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

    def get_queryset(self):
        return Testimonial.objects.filter(is_approved=True).order_by('-created_at', '-id')
