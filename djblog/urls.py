# coding=utf8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'blog.views.home'),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
