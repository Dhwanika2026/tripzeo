from django.contrib import admin
from django.urls import path
from tours import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('holiday/', views.holiday, name='holiday'),

    path('flight/', views.flight, name='flight'),

    path('cruise/', views.cruise, name='cruise'),

    path('hotel/', views.hotel, name='hotel'),

    path('blog/', views.blog, name='blog'),

    path('contact/', views.contact, name='contact'),

    path('t-and-c/', views.terms_conditions, name='terms_conditions'),

    path('policy/', views.policy, name='policy'),

    # IMPORTANT
    path(
        'search-destination/',
        views.search_destination,
        name='search_destination'
    ),

    path(
        'package/<slug:slug>/',
        views.package_detail,
        name='package_detail'
    ),

    # KEEP THIS ALWAYS AT LAST
    path(
        '<str:location>/',
        views.destination_packages,
        name='destination_packages'
    ),

    path(
        'booking/<int:pk>/',
        views.package_booking,
        name='package_booking'
    ),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)