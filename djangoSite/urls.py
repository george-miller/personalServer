from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r"^$", TemplateView.as_view(template_name="index.html")),
    (r"^phoenix/", TemplateView.as_view(template_name="phoenix.html")),
    (r"^george/.*", TemplateView.as_view(template_name="badLink.html")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^icarus/', include('icarus.urls', namespace="icarus")),
#    url(r'^is/', include('intellectualSharing.urls', namespace="is")),
#    url(r'^regex/', include('regex.urls', namespace="regex"))
) 
