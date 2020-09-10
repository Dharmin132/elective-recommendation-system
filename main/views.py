from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import grades
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

# Create your views here.
def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def logout2(response):
    return render(response, 'main/logout2.html', {})

def pagelogout(request):
    logout(request)
    return redirect('logout2')

def chooseSem(response):
    return render(response, 'main/sems.html', {})

#sem 5
def goToSem5(response):
    return render(response, 'main/sem5.html', {})

def goToSem5cs(response):
    return render(response, 'main/sem5cs.html', {})

def goToSem5el(response):
    return render(response, 'main/sem5el.html', {})

def goToSem5ct(response):
    return render(response, 'main/sem5ct.html', {})

def goToSem5sc(response):
    return render(response, 'main/sem5sc.html', {})

def goToSem5hm(response):
    return render(response, 'main/sem5hm.html', {})


#sem 6
def goToSem6(response):
    return render(response, 'main/sem6.html', {})

def goToSem6cs(response):
    return render(response, 'main/sem6cs.html', {})

def goToSem6el(response):
    return render(response, 'main/sem6el.html', {})

def goToSem6ct(response):
    return render(response, 'main/sem6ct.html', {})

def goToSem6sc(response):
    return render(response, 'main/sem6sc.html', {})

def goToSem6hm(response):
    return render(response, 'main/sem6hm.html', {})

#sem 7
def goToSem7(response):
    return render(response, 'main/sem7.html', {})

def goToSem7cs(response):
    return render(response, 'main/sem7cs.html', {})

def goToSem7el(response):
    return render(response, 'main/sem7el.html', {})

def goToSem7ct(response):
    return render(response, 'main/sem7ct.html', {})

def goToSem7sc(response):
    return render(response, 'main/sem7sc.html', {})

def goToSem7hm(response):
    return render(response, 'main/sem7hm.html', {})

#sem 8
def goToSem8(response):
    return render(response, 'main/sem8.html', {})

def goToSem8cs(response):
    return render(response, 'main/sem8cs.html', {})

def goToSem8el(response):
    return render(response, 'main/sem8el.html', {})

def goToSem8ct(response):
    return render(response, 'main/sem8ct.html', {})

def goToSem8sc(response):
    return render(response, 'main/sem8sc.html', {})

def goToSem8hm(response):
    return render(response, 'main/sem8hm.html', {})


#choose
def chooseCS(response):
    return render(response, 'main/choosecs.html', {})

def chooseEL(response):
    return render(response, 'main/chooseel.html', {})

def chooseCT(response):
    return render(response, 'main/choosect.html', {})

def chooseSC(response):
    return render(response, 'main/choosesc.html', {})

def chooseHM(response):
    return render(response, 'main/choosehm.html', {})



def grade(response):
    if response.method == "POST":
        form = grades(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = grading(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = grades()

    return render(response, "main/courses.html", {"form": form})


# def course(response):
#     ls = takenCourses.objects.get()

#     if response.method == "POST":
#         if response.POST.get("save"):
#             for item in ls.item_set.all():
#                 item.save()

#         elif response.POST.get("newItem"):
#             txt = response.POST.get("new")

#             if len(txt) > 2:
#                 ls.item_set.create(text=txt, complete=False)
#             else:
#                 print("invalid")

#     return render(response, "main/courses.html", {"ls":ls})

def course(response):
    return render(response, 'main/courses.html', {})


def final(response):
    return render(response, 'main/final.html', {})
