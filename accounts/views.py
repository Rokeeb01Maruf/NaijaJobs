from django.shortcuts import render

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        terms = request.POST.get("terms")
        if not first_name:
            error = "First name is required"
            return render(request, "accounts/signup.html", {"error": error})
        elif not last_name:
            error = "Last name is required"
            return render(request, "accounts/signup.html", {"error" : error})
        elif terms == "none":
            error = "Please read and accept our terms and condition"
            return render(request, "accounts/signup.html", {"error": error})
        elif not "@" in email or not ".com" in email:
            return render(request, "accounts/signup.html", {"error": "not a valid email"})
        elif not password and password != cpassword:
            error = "Password Mismatch"
            return render(request, "accounts/signup.html", {"error" : error})
        else:
            form = {
                "first_name" : first_name,
                "last_name" : last_name,
                "email" : email,
                "password" : password,
                "terms" : terms
            }
        return render(request, "accounts/signup.html", form)

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not "@" in email or not ".com" in email:
            return render(request, "accounts/signin.html", {"error" : "not a valid email"})
        elif not password:
            return render(request, "accounts/signin.html", {"error" : "please input a password"})
        data = {"email" : email, "password" : password}
        return render(request, "accounts/signin.html", data)
# Create your views here.
