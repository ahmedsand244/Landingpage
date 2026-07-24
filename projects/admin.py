from django.contrib import admin
from .models import Category, Project, ProjectGallery

class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'client_name', 'country', 'is_featured', 'created_at')
    list_filter = ('project_type', 'is_featured', 'country', 'created_at')
    search_fields = ('title', 'client_name', 'summary', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryInline]
    filter_horizontal = ('technologies',)
