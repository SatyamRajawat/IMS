from django import forms
from django.db import models
from django.forms import ModelForm
from info.models import *


class deptform(forms.ModelForm):
    id = forms.CharField(max_length=100, label="Dept ID")
    name = forms.CharField(max_length=200, label="Dept Name")
    class Meta:
        model=Dept
        fields='__all__'


class classform(forms.ModelForm):
    id = forms.CharField(max_length=100, label="Class ID")
    class Meta:
        model=Class
        fields='__all__'


class courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class teacherform(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'

class assignform(forms.ModelForm):
    class Meta:
        model=Assign
        fields='__all__'

class timeform(forms.ModelForm):
    class Meta:
        model=AssignTime
        fields='__all__'