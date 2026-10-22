from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import front_end.views
from root_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front_end.urls')),
    path('', include('back_end.urls')),
    path('', front_end.views.show_construction)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)