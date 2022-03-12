from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        match_present_get_request = MatchRequest.objects.filter(getter = request.user.username)
        match_request = []
        accepted_request = []
        for x in match_present_get_request:
            count = 0
            for y in MatchRequest.objects.filter(sender = request.user.username):
                if x.sender == y.getter:
                    count = count + 1
            if count == 0:
                match_request.append(x)
        match_request_num = len(match_request)

        for x in match_present_get_request:
            count = 0
            for y in MatchRequest.objects.filter(sender = request.user.username):
                if x.sender == y.getter:
                    count = count + 1
            if count == 1:
                accepted_request.append(x)
        accepted_request_num = len(accepted_request)

        context = {
            'match_request_num': match_request_num,
            'match_request': match_request,
            'accepted_request_num': accepted_request_num,
            'accepted_request': accepted_request,
        }
        return render(request, "index.html", context)
    else:
        return render(request, "login.html")    

@csrf_exempt
def login_my(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username= username, password= password)
    if user is not None:
        login(request, user)
        print("User Authenticated") 
        response_data = {
        'authenticated': 'yes',
        } 
    else:
        print("User Not Authenticated") 
        response_data = {
        'authenticated': 'no',
        }    
    return JsonResponse(response_data)

def register_page(request):
    context = {}
    return render(request, "register.html", context)

def profile_page(request):
    if request.user.is_authenticated:
        details = Detail.objects.get(username = request.user)
        print(details.phone)
        context = {
            'details': details,
        }
        return render(request, "profile.html", context)
    else: 
        return render(request, "login.html")

def login_page(request):
    context = {}
    return render(request, "login.html", context)

def logout_my(request):
    logout(request)
    response_data = {
        'logout': 'yes',
    }
    return JsonResponse(response_data)

def profile_page_other(request, username):
    if request.user.is_authenticated:
        if Detail.objects.filter(username = username).count() != 0:
            details_my = Detail.objects.get(username = request.user.username)
            details = Detail.objects.get(username = username)
            match_sent = MatchRequest.objects.filter(sender = request.user.username, getter = username).count()
            match_get = MatchRequest.objects.filter(sender = username, getter = request.user.username).count()
            count = 0
            if details.hobby == details_my.hobby:
                count = count + 1
            if details.food == details_my.food:
                count = count + 1
            if details.hangout == details_my.hangout:
                count = count + 1
            if details.music == details_my.music:
                count = count + 1
            if match_sent != 0:
                match_is_sent = True
            else:
                match_is_sent = False
    
            if match_get != 0:
                match_is_get = True
            else:
                match_is_get = False             
    
            context = {
                'details': details,
                'match_is_get': match_is_get,
                'match_is_sent': match_is_sent,
                'count': count,
            }
            return render(request, "profileuser.html",context)
    else:
        return render(request, "login.html")      

def feed(request):
    if request.user.is_authenticated:
        username_my = request.user.username
        details_my = Detail.objects.get(username = username_my)
        gender_my = details_my.gender
        if gender_my == "Male":
            details = Detail.objects.filter(gender = "Female")
            details_tag4 = []
            details_tag3 = []
            details_tag2 = []
            details_tag1 = []
            details_tag0 = []
            for detail in details:
                count = 0
                if detail.hobby == details_my.hobby:
                    count = count + 1
                if detail.food == details_my.food:
                    count = count + 1
                if detail.hangout == details_my.hangout:
                    count = count + 1
                if detail.music == details_my.music:
                    count = count + 1
                if count == 0:
                    details_tag0.append(detail)
                if count == 1:
                    details_tag1.append(detail)
                if count == 2:
                    details_tag2.append(detail)
                if count == 3:
                    details_tag3.append(detail)
                if count == 4:
                    details_tag4.append(detail)
            context = {
                'details_tag0': details_tag0,
                'details_tag1': details_tag1,
                'details_tag2': details_tag2,
                'details_tag3': details_tag3,
                'details_tag4': details_tag4,
            }
        else:
            details = Detail.objects.filter(gender = "Male")
            details_tag4 = []
            details_tag3 = []
            details_tag2 = []
            details_tag1 = []
            details_tag0 = []
            for detail in details:
                count = 0
                if detail.hobby == details_my.hobby:
                    count = count + 1
                if detail.food == details_my.food:
                    count = count + 1
                if detail.hangout == details_my.hangout:
                    count = count + 1
                if detail.music == details_my.music:
                    count = count + 1
                if count == 0:
                    details_tag0.append(detail)
                if count == 1:
                    details_tag1.append(detail)
                if count == 2:
                    details_tag2.append(detail)
                if count == 3:
                    details_tag3.append(detail)
                if count == 4:
                    details_tag4.append(detail)
            context = {
                'details_tag0': details_tag0,
                'details_tag1': details_tag1,
                'details_tag2': details_tag2,
                'details_tag3': details_tag3,
                'details_tag4': details_tag4,
            }
        return render(request, "feed.html", context)
    else:
        return render(request, "login.html") 

@csrf_exempt
def register_my(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    address = request.POST.get("address")
    bhawan = request.POST.get("bhawan")
    country = request.POST.get("country")
    state = request.POST.get("state")
    zipcode = request.POST.get("zip")
    phone = request.POST.get("number")
    branch = request.POST.get("branch")
    about = request.POST.get("about")
    hobby = request.POST.get("hobby")
    hangout = request.POST.get("hangout")
    music = request.POST.get("music")
    food = request.POST.get("food")
    user = User.objects.create_user(username, None , password)
    user.save()
    detail = Detail.objects.create(username = username, firstname = firstname, lastname = lastname, gender = gender, email = email, address = address, bhawan = bhawan, country = country, state = state, zipcode = zipcode, phone = phone, branch = branch, bio = about, hobby = hobby, hangout = hangout, music = music, food = food)
    detail.save()
    response_data = {
        'created': 'yes',
    }
    login(request, user) 
    return JsonResponse(response_data)

@csrf_exempt
def update_profile(request):
    username = request.POST.get("username")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    bhawan = request.POST.get("bhawan")
    country = request.POST.get("country")
    state = request.POST.get("state")
    zipcode = request.POST.get("zip")
    phone = request.POST.get("number")
    branch = request.POST.get("branch")
    about = request.POST.get("about")
    insta = request.POST.get("insta")
    facebook = request.POST.get("facebook")
    twitter = request.POST.get("twitter")
    
    user = Detail.objects.get(username = username)
    print(user)
    user.firstname = firstname
    user.lastname = lastname
    user.email = email
    user.bhawan = bhawan
    user.country = country
    user.state = state
    user.zipcode = zipcode
    user.phone = phone
    user.branch = branch
    user.bio = about
    user.insta = insta
    user.facebook = facebook
    user.twitter = twitter
    user.save()

    response_data = {
        'created': 'yes',
    }
    return JsonResponse(response_data)

@csrf_exempt
def match_yes(request):
    sender = request.POST.get("sender")
    getter = request.POST.get("getter")
    match_is_present = MatchRequest.objects.filter(sender = sender, getter = getter).count()
    if match_is_present == 1:
        match = MatchRequest.objects.get(sender = sender, getter = getter)
        match.status = "yes"
        match.save()

        response_data = {
            'done': 'yes'
        }

        return JsonResponse(response_data)
    else:
        match = MatchRequest.objects.create(sender = sender, getter = getter, status = "no")
        match.save()

        response_data = {
            'done': 'yes'
        }

        return JsonResponse(response_data)

def picture_upload(request):
    detail = Detail.objects.get(username = request.user.username)
    detail.image = request.FILES.get('image')
    detail.save()
    return JsonResponse("done", safe=False)