from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from . import forms
from .forms import FormName, userForm, user_Profileform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def home(request):
    accessRecord_ins = accessRecord.objects.all()
    dict = {"insert_me": "I'm from fresh_app home function",
            "accessRecord": accessRecord_ins}
    return render(request, "fresh_app/basic.html", context=dict)


def form_view(request):
    form = forms.FormName()
    if request.POST:
        form = forms.FormName(request.POST)

    if form.is_valid():
        print("Form validation is successfully compelted!")
        print("Name: " + form.cleaned_data["name"])
        print("Email: " + form.cleaned_data["email"])
        print("text: " + form.cleaned_data["text"])

    dict_1 = {"form": form}

    return render(request, "fresh_app/form.html", context=dict_1)


@login_required
def user_logout(request):
    logout(request)
    return redirect("user_login")


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


def user_registration(request):
    if request.method == "POST":
        user_form = userForm(request.POST)
        profile_Form = user_Profileform(request.POST)
        if user_form.is_valid() and profile_Form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_Form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()

            return redirect("form_view")

        else:
            print("Your form is not valid!", user_form.errors, profile_Form.errors)

    else:
        user_form = userForm()
        profile_Form = user_Profileform()

    con = {'userform': user_form, 'userforminfo': profile_Form}
    return render(request, "fresh_App/user_info.html", con)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        print(user)

        if user:
            print(user.is_active)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('form_view'))

            else:
                print("ACCOUNT IS NOT ACTIVE")
        else:
            print("Someone tried to logging and Failed !")
            print(f"username: {username} password: {password}")
            return HttpResponse("INVALID CREDENTIALS")

    else:
        return render(request, "fresh_app/user_login.html", {})
