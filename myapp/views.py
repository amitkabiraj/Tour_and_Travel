from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')
    # return HttpResponse("this is homepage")
def car(request):
    return render(request, 'myapp/car/car.html')
def car_details(request):
    return render(request, 'myapp/car/car_details.html')
def nadia_car(request):
    return render(request, 'myapp/car/nadia_car.html')
def murshidabad_car(request):
    return render(request, 'myapp/car/murshidabad_car.html')
def hotel(request):
    return render(request, 'myapp/hotel/hotel.html')
def tickets(request):
    return render(request, 'myapp/others/tickets.html')
def tourplan(request):
    return render(request, 'myapp/others/tour_plan.html') 
def restrurent(request):
    return render(request, 'myapp/info/restrurent.html') 
def hospital(request):    
    return render(request, 'myapp/info/hospital.html')
def atm(request):    
    return render(request, 'myapp/info/atm.html')
def pump(request):    
    return render(request, 'myapp/info/pump.html')
def places(request):
    return render(request, 'myapp/place/places.html')
def terms(request):
    return render(request, 'myapp/others/terms.html') 
def privasy(request):
    return render(request, 'myapp/others/privasy.html')
def review(request):
    return render(request, 'myapp/others/review.html') 
def murshidabad(request):
    return render(request, 'myapp/place/murshidabad.html') 
def nadia(request):
    return render(request, 'myapp/place/nadia.html') 
def contact(request):
    return render(request, 'myapp/contact.html') 
def about(request):
    return render(request, 'myapp/about.html') 
def admin_login(request):
    return render(request, 'myapp/admin/admin_login.html')
def admin_panel(request):
    return render(request, 'myapp/admin/adminpanel.html') 
def user_login(request):
    return render(request, 'myapp/user/user_login.html')
def user_panel(request):
    return render(request, 'myapp/user/userpanel.html')
def register(request):
    return render(request, 'myapp/user/register.html')
<<<<<<< HEAD
=======
def all_images(request):
    return render(request, 'myapp/hotel/all_images.html')
def hotel_booking(request):
    return render(request, 'myapp/hotel/booking page.html')
>>>>>>> 9635052f9c39ff31e964b122090e900d29290ff6
