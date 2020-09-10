from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='Home'),
    path('chooseSem/', views.chooseSem, name='Choose Semester'),
    path('logout2/', views.logout2, name='logoutpage'),
    path("course/", views.course, name="course"),
    path("final/", views.final, name="Final"),

    path('goToSem5/', views.goToSem5, name='Semester 5'),
    path('goToSem5cs/', views.goToSem5cs, name='Semester 5 - Computer Science'),
    path('goToSem5el/', views.goToSem5el, name='Semester 5 - Electronics'),
    path('goToSem5ct/', views.goToSem5ct, name='Semester 5 - Communication Theory'),
    path('goToSem5sc/', views.goToSem5sc, name='Semester 5 - Mathematics'),
    path('goToSem5hm/', views.goToSem5hm, name='Semester 5 - Humanities'),

    path('goToSem6/', views.goToSem6, name='Semester 6'),
    path('goToSem6cs/', views.goToSem6cs, name='Semester 6 - Computer Science'),
    path('goToSem6el/', views.goToSem6el, name='Semester 6 - Electronics'),
    path('goToSem6ct/', views.goToSem6ct, name='Semester 6 - Communication Theory'),
    path('goToSem6sc/', views.goToSem6sc, name='Semester 6 - Mathematics'),
    path('goToSem6hm/', views.goToSem6hm, name='Semester 6 - Humanities'),

    path('goToSem7/', views.goToSem7, name='Semester 7'),
    path('goToSem7cs/', views.goToSem7cs, name='Semester 7 - Computer Science'),
    path('goToSem7el/', views.goToSem7el, name='Semester 7 - Electronics'),
    path('goToSem7ct/', views.goToSem7ct, name='Semester 7 - Communication Theory'),
    path('goToSem7sc/', views.goToSem7sc, name='Semester 7 - Mathematics'),
    path('goToSem7hm/', views.goToSem7hm, name='Semester 7 - Humanities'),

    path('goToSem8/', views.goToSem8, name='Semester 8'),
    path('goToSem8cs/', views.goToSem8cs, name='Semester 8 - Computer Science'),
    path('goToSem8el/', views.goToSem8el, name='Semester 8 - Electronics'),
    path('goToSem8ct/', views.goToSem8ct, name='Semester 8 - Communication Theory'),
    path('goToSem8sc/', views.goToSem8sc, name='Semester 8 - Mathematics'),
    path('goToSem8hm/', views.goToSem8hm, name='Semester 8 - Humanities'),
]
