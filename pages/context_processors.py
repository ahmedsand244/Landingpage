from .models import SiteSetting, StudioMetric

def site_context(request):
    site_settings, _ = SiteSetting.objects.get_or_create(id=1)
    studio_metrics = StudioMetric.objects.filter(is_active=True).order_by('order', 'id')
    return {
        'site_settings': site_settings,
        'studio_metrics': studio_metrics,
    }
