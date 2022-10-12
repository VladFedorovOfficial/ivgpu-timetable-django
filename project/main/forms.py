from dataclasses import fields
from tkinter import Widget
from .models import Timetable
from django.forms import ModelForm, TextInput

class TimetableForm(ModelForm):
    class Meta:
        model = Timetable
        fields = [
            'weekType',
            'weekDay',

            'lessonNameFirst',
            'additInfoFirst',

            'lessonNameSecond',
            'additInfoSecond',

            'lessonNameThird',
            'additInfoThird',

            'lessonNameFourth',
            'additInfoFourth'
        ]