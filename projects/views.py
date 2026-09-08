from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Project, Category
from services.models import Technology

class PortfolioView(ListView):
    model = Project
    template_name = "projects/portfolio.html"
    context_object_name = "projects"
    paginate_by = 12

    def get_queryset(self):
        queryset = Project.objects.all().prefetch_related('technologies', 'gallery')
        
        # 1. Search Query
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(title_en__icontains=q) |
                Q(summary__icontains=q) |
                Q(summary_en__icontains=q) |
                Q(overview__icontains=q) |
                Q(overview_en__icontains=q) |
                Q(client_name__icontains=q) |
                Q(client_name_en__icontains=q) |
                Q(technologies__name__icontains=q) |
                Q(technologies__name_en__icontains=q)
            ).distinct()
            
        # 2. Project Type Filter ('graduation' / 'commercial')
        raw_type = self.request.GET.get('type', '').strip().lower()
        if raw_type in ['commercial', 'business', 'biz']:
            queryset = queryset.filter(project_type='commercial')
        elif raw_type in ['graduation', 'academic', 'acad']:
            queryset = queryset.filter(project_type='graduation')
            
        # 3. Category Filter (slug)
        category_slug = self.request.GET.get('category', '').strip()
        if category_slug:
            queryset = queryset.filter(technologies__category__slug=category_slug).distinct()
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        
        raw_type = self.request.GET.get('type', '').strip().lower()
        if raw_type in ['commercial', 'business', 'biz']:
            normalized_type = 'business'
        elif raw_type in ['graduation', 'academic', 'acad']:
            normalized_type = 'academic'
        else:
            normalized_type = ''
            
        context['current_type'] = normalized_type
        context['active_type'] = normalized_type
        context['search_query'] = self.request.GET.get('q', '').strip()
        context['total_count'] = Project.objects.count()
        context['biz_count'] = Project.objects.filter(project_type='commercial').count()
        context['acad_count'] = Project.objects.filter(project_type='graduation').count()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_project = self.get_object()
        # Suggest related projects (excluding current project)
        context['related_projects'] = Project.objects.filter(
            project_type=current_project.project_type
        ).exclude(id=current_project.id)[:3]
        
        # Previous & Next project navigation
        context['previous_project'] = Project.objects.filter(
            created_at__lt=current_project.created_at
        ).order_by('-created_at').first()
        
        context['next_project'] = Project.objects.filter(
            created_at__gt=current_project.created_at
        ).order_by('created_at').first()
        return context
