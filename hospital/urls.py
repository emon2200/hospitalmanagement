"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from hospital import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', include('doctors.urls')),  # Include URLs for the doctors app
  #  path('patients/', include('patients.urls')),  # Include URLs for the patients app
    path('appointments/', include('appointments.urls')),  # Include URLs for the appointments app
    path('', views.home, name='home'),  # Home app for the main page (optional)
    path('contacts', views.contacts, name='contacts'), 
    path('generalcheckup_examiantions/', views.gec, name='gec'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])