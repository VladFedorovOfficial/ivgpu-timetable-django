from sqlite3 import Time
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Timetable
import datetime
import calendar


weekDays =[
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Суббота',
    'Воскресенье'
]

def get_week_num(day: int, month: int, year: int) -> int:
    calendar_ = calendar.TextCalendar(calendar.MONDAY)
    lines = calendar_.formatmonth(year, month).split('\n')
    days_by_week = [week.lstrip().split() for week in lines[2:]]
    str_day = str(day)
    for index, week in enumerate(days_by_week):
        if str_day in week:
            return index + 1
    
    raise ValueError(f'Нет дня с номером {day} в месяце с номером {month} в {year} году!')


def timetableView(request):
    todayDate = datetime.date.today()

    data = {
        'lessons': Timetable.objects.all(),
        'currentWeekDay': weekDays[todayDate.weekday()],
        'currentWeekTypeInt': get_week_num(todayDate.day, todayDate.month, todayDate.year),
        'testKey': str(todayDate.day) + ' ' + str(todayDate.month) + ' ' + str(todayDate.year),
        'selectedGroup': 'Первая'
    }

    return render(request, 'timetable/timetable-main.html', data)