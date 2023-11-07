from django.contrib import admin
from django.urls import path
from myapp import views
<<<<<<< HEAD
urlpatterns = [
    path('',views.index, name='index'),
    path('car',views.car, name='car'),
    path('car_details',views.car_details, name='car_details'),
    path('hotel',views.hotel, name='hotel'),
    path('tourplan',views.tourplan, name='tour_plan'),
    path('tickets',views.tickets, name='tickets'),
    path('hospital',views.hospital, name='hospital'),
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
    path('admin_login',views.admin_login, name='admin_login'),
    path('admin_panel',views.admin_panel, name='admin_panel'),
    path('user_login',views.user_login, name='user_login'),
    path('user_pnel',views.user_panel, name='user_panel'),
    path('register',views.register, name='register'),
    
=======
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
>>>>>>> amit


urlpatterns = [
    path("", views.index, name="index"),
    # INFO
    path("tourplan", views.tourplan, name="tour_plan"),
    path("tickets", views.tickets, name="tickets"),
    path("hospital", views.hospital, name="hospital"),
    path("medicine", views.medicine, name="medicine"),
    path("restrurent", views.restrurent, name="restrurent"),
    path("pump", views.pump, name="pump"),
    path("atm", views.atm, name="atm"),
    # INFO END
    # OTHER
    path("terms", views.terms, name="terms"),
    path("privasy", views.privasy, name="privasy"),
    path("review", views.review, name="review"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    # OTHER END
    # PLACE
    path("places", views.places, name="places"),
    path("murshidabad", views.murshidabad, name="murshidabad"),
    path("nadia", views.nadia, name="nadia"),
    # PLACE END
    # USER
    path("user_login", views.user_login, name="user_login"),
    path(
        "logout", auth_views.LogoutView.as_view(next_page="user_login"), name="logout"
    ),
    path("user_pnel", views.user_panel, name="user_panel"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("order", views.order, name="order"),
    path("status", views.status, name="status"),
    path("register", views.register, name="register"),
    # USER END
    # CAR
    path("car", views.car, name="car"),
    path("car_details", views.car_details, name="car_details"),
    path("car_range", views.car_range, name="car_range"),
    path("nadia_car", views.nadia_car, name="nadia_car"),
    path("murshidabad_car", views.murshidabad_car, name="murshidabad_car"),
    path('process_payment/', views.process_payment, name='process_payment'),
    # CAR END
    # HOTEL
    path("hotel", views.hotel, name="hotel"),
    path("booking_page/<str:pk>", views.booking_page, name="booking_page"),
    path("booking_details/<str:pk>", views.booking_details, name="bookimng_details"),
    path("payment_page", views.payment_page, name="payment_page"),
    path("all_images/<str:pk>", views.all_images, name="all_images"),
    path("thank_you", views.thank_you, name="thank_you"),
    # HOTEL END
    # path('admin_login',views.admin_login, name='admin_login'),
    # path("admin_panel", views.admin_panel, name="admin_panel"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
