from django.shortcuts import render, HttpResponse
from myapp.models import Hotel, Review, ContactMessage, User


# Create your views here.
def index(request):
    data = Review.objects.all()
    return render(request, "myapp/index.html", {"review_data": data})
    # return HttpResponse("this is homepage")


def car(request):
    return render(request, "myapp/car/car.html")


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
    return render(request, "myapp/place/murshidabad.html",{"hotel_data": data},)


def nadia(request):
    data = Hotel.objects.all()
    return render(request, "myapp/place/nadia.html",{"hotel_data": data},)


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


def user_login(request):
    return render(request, "myapp/user/user_login.html")


def user_panel(request):
    return render(request, "myapp/user/userpanel.html")


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone =request.POST["phone"]
        password= request.POST["password"]
        picture = request.FILES.get("picture")
        gender = request.POST["gender"]
        country = request.POST["country"]


    
        User.objects.create(name=name, email=email, phone=phone, password=password,picture=picture,gender=gender, country=country)
        # return render(request, "myapp/success.html",{"user": User})
    
    return render(request, "myapp/user/register.html")


def all_images(request):
    return render(request, "myapp/hotel/all_images.html")


def hotel_booking(request):
    return render(request, "myapp/hotel/booking page.html")


def hotel(request):
    data = Hotel.objects.all()
    print("data comes")
    return render(
        request,
        "myapp/hotel/hotel.html",
        {"hotel_data": data},
    )


# def hotel(request):
#     return render(request, 'myapp/hotel/hotel.html')
