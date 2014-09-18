from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.views.generic.base import RedirectView, TemplateView

urlpatterns = patterns('',
    # Core URLs
    url(r'^', include('core.urls', namespace='core')),

    # Root-level redirects for common browser requests
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # Authtools URLs
    # https://github.com/fusionbox/django-authtools/blob/master/authtools/urls.py
    url(r'^', include('authtools.urls', namespace='authtools')),

    # Admin URLs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)))

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
