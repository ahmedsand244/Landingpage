from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Category
from services.models import Technology

class PortfolioView(ListView):
    model = Project
    template_name = "projects/portfolio.html"
    context_object_name = "projects"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # 1. Search Query
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(title__icontains=q) | queryset.filter(summary__icontains=q) | queryset.filter(overview__icontains=q)
            
        # 2. Project Type Filter ('graduation' / 'commercial')
        project_type = self.request.GET.get('type', '').strip()
        if project_type:
            queryset = queryset.filter(project_type=project_type)
            
        # 3. Category Filter (slug)
        category_slug = self.request.GET.get('category', '').strip()
        if category_slug:
            queryset = queryset.filter(technologies__category__slug=category_slug).distinct()
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # Keep track of active query parameters
        context['active_category'] = self.request.GET.get('category', '')
        context['active_type'] = self.request.GET.get('type', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Suggest related projects (excluding current project)
        current_project = self.get_object()
        context['related_projects'] = Project.objects.filter(
            project_type=current_project.project_type
        ).exclude(id=current_project.id)[:3]
        return context
