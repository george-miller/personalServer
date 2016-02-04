from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r"^$", TemplateView.as_view(template_name="index.html")),
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^icarus/', include('icarus.urls', namespace="icarus"))
) + static('/static/', document_root=settings.STATIC_FOLDER) 
