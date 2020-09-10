from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

grades = (
    ("1", "AA"),
    ("2", "AB"),
    ("3", "BB"),
    ("4", "BC"),
    ("5", "CC"),
    ("6", "CD"),
    ("7", "DD"),
    ("8", "DE"),
    ("9", "F"),
)

interest = (
    ("1", "10"),
    ("2", "9"),
    ("3", "8"),
    ("4", "7"),
    ("5", "6"),
    ("6", "5"),
    ("7", "4"),
    ("8", "3"),
    ("9", "2"),
    ("10", "1"),
    ("11", "0"),
)

class grades(forms.Form):
    grade = forms.ChoiceField(choices = "grades")

    class Meta:
        model = User
        fields = ["grade"]