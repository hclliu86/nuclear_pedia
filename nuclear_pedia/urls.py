"""nuclear_pedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from nuclear_pedia import settings
from django.conf.urls import url
from django.contrib import admin
from wm import views as wm_views

urlpatterns = [
    url(r'^wm/$', wm_views.homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^root_images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_STATIC_IMAGES})
]
