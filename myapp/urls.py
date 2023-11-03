from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


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
    # CAR END
    # HOTEL
    path("hotel", views.hotel, name="hotel"),
    path("booking_page", views.booking_page, name="booking_page"),
    path("payment_page", views.payment_page, name="payment_page"),
    path("all_images", views.all_images, name="all_images"),

    # HOTEL END
    # path('admin_login',views.admin_login, name='admin_login'),
    # path("admin_panel", views.admin_panel, name="admin_panel"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
