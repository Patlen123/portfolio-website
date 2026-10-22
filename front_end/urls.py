from django.contrib import admin
from django.urls import path, include
from front_end import views

urlpatterns = [
    path('', views.show_index, name=''),
    #path('about', views.show_about, name="about"),
    #path('committee', views.show_com, name='committee'),

    #path('admin/', admin.site.urls),
    #path('', include('back_end.urls')),
    # Use this if something breaks
    #path('', views.show_construction)
]