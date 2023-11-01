from django.contrib import admin
from django.urls import path
from myapp import views
from django .conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('car',views.car, name='car'),
    path('hotel',views.hotel, name='hotel'),
    path('tourplan',views.tourplan, name='tour_plan'),
    path('tickets',views.tickets, name='tickets'),
    path('hospital',views.hospital, name='hospital'),
    path('medicine',views.medicine, name='medicine'),
    path('restrurent',views.restrurent, name='restrurent'),
    path('pump',views.pump, name='pump'),
    path('atm',views.atm, name='atm'),
    path('terms',views.terms, name='terms'),
    path('privasy',views.privasy, name='privasy'),
    path('places',views.places, name='places'),
    path('review',views.review, name='review'),
    path('murshidabad',views.murshidabad, name='murshidabad'),
    path('nadia',views.nadia, name='nadia'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    # path('admin_login',views.admin_login, name='admin_login'),
    path('admin_panel',views.admin_panel, name='admin_panel'),
    path('user_login',views.user_login, name='user_login'),
    path('user_pnel',views.user_panel, name='user_panel'),
    path('register',views.register, name='register'),
    path('all_images',views.all_images,name='all_images'),
    path('hotel_booking',views.hotel_booking,name='hotel_booking'),

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)