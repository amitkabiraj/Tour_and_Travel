from django.shortcuts import redirect, render, HttpResponse
from datetime import date,datetime
from django.contrib.auth.decorators import login_required


# from myapp.models import Hotel, Review, ContactMessage, User
from myapp.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password


# Create your views here.
# INDEX PAGE
def index(request):
    data = Review.objects.order_by('-created_at')[:3]
    return render(request, "myapp/index.html", {"review_data": data})
    # return HttpResponse("this is homepage")


def tickets(request):
    return render(request, "myapp/others/tickets.html")


def tourplan(request):
    return render(request, "myapp/others/tour_plan.html")

def restrurent(request):
    murshidabad_restaurants = Restaurants.objects.filter(Dist='Murshidabad')
    nadia_restaurants = Restaurants.objects.filter(Dist='Nadia')

    return render(
        request,
        "myapp/info/restrurent.html",
        {
            "murshidabad_restaurants": murshidabad_restaurants,
            "nadia_restaurants": nadia_restaurants,
        }
    )


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
    murshidabad_place = place.objects.filter(Dist='Murshidabad')
    return render(
        request,
        "myapp/place/murshidabad.html",
        {"hotel_data": data, "murshidabad_place": murshidabad_place},
    )


def nadia(request):
    # data = Hotel.objects.all()
    nadia_place = place.objects.filter(Dist='Nadia')
    return render(
        request,
        "myapp/place/nadia.html",
        { "nadia_place": nadia_place},
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
#USER LOGIN
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


@login_required(login_url="/")
def user_profile(request):
    user = request.user
    print(user.email)

    context = {"name": user.name, "email": user.email}
    return render(request, "myapp/user/user_profile.html", context=context)

def user_panel(request):
    return render(request, "myapp/user/userpanel.html")

# USER REGISTER
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
        return redirect("user_login")

    return render(request, "myapp/user/register.html")


def order(request):
    return render(request, "myapp/user/order.html")


def status(request):
    return render(request, "myapp/user/status.html")


# HOTEL

def booking_page(request):
    initial=date.today()
    return render(request, "myapp/hotel/booking_page.html",{'d':initial})

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
#Payment page
def payment_page(request):
    text=''
    initial=date.today()
    if request.method == 'POST':
        date_str1 = request.POST.get('startdatetime')
        date_str2 = request.POST.get('enddatetime')
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        day_difference = (date2 - date1).days
        if day_difference<0:
            text="Please enter correct data"
            return render(request, "myapp/hotel/booking_page.html",{'d':initial,'error':text})
    return render(request, "myapp/hotel/hotel_payment.html",{'day_difference':day_difference,'error':text})

def car(request):
    return render(request, "myapp/car/car.html")


# def hotel(request):
#     return render(request, 'myapp/hotel/hotel.html')
