from django.conf.urls import patterns, include, url
from django.contrib import admin
from shop.views import *
from django.conf.urls.static import static
import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', ItemListView.as_view()),
    url(r'^$', RedirectView.as_view(url='cat/termopasta/', permanent=False), name='index'),
    # url(r'^about/$', TemplateView.as_view(template_name="shop/about.html"), name='about'),
    # url(r'^contacts/$', TemplateView.as_view(template_name="shop/contacts.html"), name='contacts'),


    # url(r'^item/(?P<pk>\d+)$', ItemDetailView.as_view(), name='item_view'),
    url(r'^add_order/(\d+)$', add_order),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^cat/(?P<slug>\w+)/$', ItemListView.as_view(), name='category_url'),
    url(r'^cat/(?P<slug>\w+)/item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_view'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )