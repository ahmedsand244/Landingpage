from django.core.cache import cache
from .models import SiteSetting, StudioMetric

def site_context(request):
    site_settings = cache.get('codeplus_site_settings')
    if site_settings is None:
        try:
            site_settings, _ = SiteSetting.objects.get_or_create(id=1)
            cache.set('codeplus_site_settings', site_settings, 300)
        except Exception:
            site_settings = None

    studio_metrics = cache.get('codeplus_studio_metrics')
    if studio_metrics is None:
        try:
            studio_metrics = list(StudioMetric.objects.filter(is_active=True).order_by('order', 'id'))
            cache.set('codeplus_studio_metrics', studio_metrics, 300)
        except Exception:
            studio_metrics = []

    return {
        'site_settings': site_settings,
        'studio_metrics': studio_metrics,
    }
