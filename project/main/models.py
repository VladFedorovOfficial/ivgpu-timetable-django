from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

class Timetable(models.Model):

    WEEK_NAMES = [
        ('Понедельник', 'Понедельник'), 
        ('Вторник', 'Вторник'), 
        ('Среда', 'Среда'), 
        ('Четверг', 'Четверг'), 
        ('Пятница', 'Пятница'), 
        ('Суббота', 'Суббота'), 
        ('Воскресенье', 'Воскресенье')
    ]

    WEEK_TYPES = [
        ('Первая', 'Первая'),
        ('Вторая', 'Вторая')
    ]

    GROUP_NUMS = [
        ('x', 'Первая'),
        ('xx', 'Вторая')
    ]

    weekType = models.CharField('Тип недели', max_length=20, choices=WEEK_TYPES)
    weekDay = models.CharField('День недели', max_length=20, choices=WEEK_NAMES)
    groupNum = models.CharField('Номер группы', max_length=20, choices=GROUP_NUMS)

    # lessonName = (
    #     models.CharField('8:30-10:00', max_length = 50),
    #     models.CharField('8:30-10:00', max_length = 50),
    #     models.CharField('8:30-10:00', max_length = 50),
    #     models.CharField('8:30-10:00', max_length = 50)
    # )

    # additInfo = (
    #     models.CharField('Дополнительная информация', max_length = 50),
    #     models.CharField('Дополнительная информация', max_length = 50),
    #     models.CharField('Дополнительная информация', max_length = 50),
    #     models.CharField('Дополнительная информация', max_length = 50)
    # )

    lessonNameFirst = models.CharField('08:30-10:00', max_length = 100, blank=True)
    additInfoFirst = models.CharField('Дополнительная информация', max_length = 100, blank=True)

    lessonNameSecond = models.CharField('10:15-11:45', max_length = 100, blank=True)
    additInfoSecond = models.CharField('Дополнительная информация', max_length = 100, blank=True)

    lessonNameThird = models.CharField('12:30-14:00', max_length = 100, blank=True)
    additInfoThird = models.CharField('Дополнительная информация', max_length = 100, blank=True)

    lessonNameFourth = models.CharField('14:10-15:40', max_length = 100, blank=True)
    additInfoFourth = models.CharField('Дополнительная информация', max_length = 100, blank=True)

    def __str__(self):
        return (self.groupNum + ': ' + self.weekType + ' неделя, ' + self.weekDay)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'