from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required

# from myapp.models import Hotel, Review, ContactMessage, User
from myapp.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password


# Create your views here.
# INDEX PAGE
def index(request):
    data = Review.objects.all()
    return render(request, "myapp/index.html", {"review_data": data})
    # return HttpResponse("this is homepage")


def tickets(request):
    return render(request, "myapp/others/tickets.html")


def tickets(request):
    return render(request, "myapp/others/tickets.html")


def tourplan(request):
    return render(request, "myapp/others/tour_plan.html")


def restrurent(request):
    return render(request, "myapp/info/restrurent.html")


def hospital(request):
    return render(request, "myapp/info/hospital.html")


def medicine(request):
    return render(request, "myapp/info/medicine.html")


def atm(request):
    return render(request, "myapp/info/atm.html")


def pump(request):
    return render(request, "myapp/info/pump.html")


def places(request):
    return render(request, "myapp/place/places.html")


def terms(request):
    return render(request, "myapp/others/terms.html")


def privasy(request):
    return render(request, "myapp/others/privasy.html")


def review(request):
    return render(request, "myapp/others/review.html")


def murshidabad(request):
    data = Hotel.objects.all()
    data1 = Murshidabad_place.objects.all()
    return render(
        request,
        "myapp/place/murshidabad.html",
        {"hotel_data": data, "murshidabad_place": data1},
    )


def nadia(request):
    data = Hotel.objects.all()
    return render(
        request,
        "myapp/place/nadia.html",
        {"hotel_data": data},
    )


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        ContactMessage.objects.create(name=name, email=email, message=message)

    return render(request, "myapp/contact.html")


def about(request):
    return render(request, "myapp/about.html")


# def admin_login(request):
#     return render(request, 'myapp/admin/admin_login.html')
def admin_panel(request):
    return render(request, "myapp/admin/adminpanel.html")


# USER
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/user_profile")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/user_profile")
    return render(request, "myapp/user/user_login.html")


def user_panel(request):
    return render(request, "myapp/user/userpanel.html")


@login_required(login_url="/")
def user_profile(request):
    user = request.user
    print(user.email)

    context = {"name": user.name, "email": user.email}
    return render(request, "myapp/user/user_profile.html", context=context)


def order(request):
    return render(request, "myapp/user/order.html")


def status(request):
    return render(request, "myapp/user/status.html")


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        picture = request.FILES.get("picture")
        gender = request.POST["gender"]
        country = request.POST["country"]

        User.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=make_password(password),
            picture=picture,
            gender=gender,
            country=country,
        )
        # return render(request, "myapp/success.html",{"user": User})

    return render(request, "myapp/user/register.html")


def hotel_booking(request):
    return render(request, "myapp/hotel/booking page.html")


def all_images(request):
    return render(request, "myapp/hotel/all_images.html")


def hotel(request):
    data = Hotel.objects.all()
    print("data comes")
    return render(
        request,
        "myapp/hotel/hotel.html",
        {"hotel_data": data},
    )


def car(request):
    return render(request, "myapp/car/car.html")


# def hotel(request):
#     return render(request, 'myapp/hotel/hotel.html')
