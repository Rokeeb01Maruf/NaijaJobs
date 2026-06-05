from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        terms = request.POST.get("terms")
        role = request.POST.get("role")
        const = [first_name, last_name, username, email, password, cpassword, terms, role]
        if not first_name:
            error = "First name is required"
            return render(request, "accounts/signup.html", {"error": error})
        elif not last_name:
            error = "Last name is required"
            return render(request, "accounts/signup.html", {"error" : error})
        elif not username:
            error = "username is required"
            return render(request, "accounts/signup.html", {"error" : error})
        elif terms != "on":
            error = "Please read and accept our terms and condition"
            return render(request, "accounts/signup.html", {"error": error})
        elif not "@" in email or not "." in email:
            return render(request, "accounts/signup.html", {"error": "not a valid email"})
        elif not password or password != cpassword:
            error = "Password Mismatch"
            return render(request, "accounts/signup.html", {"error" : error})
        elif not role:
            error = "No role selected"
            return render(request, "accounts/signup.html", {"error" : error})
        else:
            try:
                user = User(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    role = role
                )
                user.set_password(password)
                user.save()
                print(const)
                login(request, user)
                return redirect("signin")
            except Exception as e:
                error = "server error"
                return render(request, "accounts/signup.html", {"error": str(e), "message": error})

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')
    elif request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        if not username:
            return render(request, "accounts/signin.html", {"error" : "please input a username"})
        elif not password:
            return render(request, "accounts/signin.html", {"error" : "please input a password"})

        user = authenticate(request, username=username, password=password)
        if user is None:
            error = "Invalid credentials"
            return render(request, "accounts/signin.html",{"error" : error})
        else:
            login(request, user)
            return redirect("home")
# Create your views here.
