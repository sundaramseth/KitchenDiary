from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^kitchen/',include('kitchen.urls')),
    path('accounts/', include('accounts.urls')),
    url(r'^accounts/', include('authtools.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
     url(r'^auth/', include('social_django.urls', namespace='social')),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),

]
