from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from accounts.forms import AccountCreateForm, LoginForm
from accounts.models import User
from accounts.serializers import UserSerializer


def create_account(request):
    if request.method == "GET":
        # GET
        form = AccountCreateForm()
        return render(request, "create_account.html", context={"create_form": form})
    # POST
    if request.method == "POST":
        if not User.objects.filter(username=request.POST.get("username")):
            ## validate that the user doesnt already exist
            user = User(
                username=request.POST.get("username"),
                password=request.POST.get("password"),
                email=request.POST.get("email"),
            )
            password=request.POST.get("password")
            user.set_password(password)
            user.save()
            login_user(request, user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect("home")


def login(request):
    login_form = LoginForm()
    if request.method == "GET":
        return render(request, "login.html", context={"login_form": login_form})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user:
            login_user(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("home")
        else:
            return render(
                request,
                "login.html",
                context={
                    "login_form": login_form,
                    "error": "Invalid login credentials",
                },
            )


def logout(request):
    logout_user(request)
    return redirect("login")


@api_view(["GET"])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def userlist(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
