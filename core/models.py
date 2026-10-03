from django.db import models
from django.utils import timezone


class MainPage(models.Model):
    title = models.CharField(max_length=200, default="Факультет", verbose_name="Заголовок сайту")
    description = models.TextField(verbose_name="Опис факультету")
    main_info = models.TextField(verbose_name="Основна інформація")
    contacts = models.TextField(verbose_name="Контакти")

    class Meta:
        verbose_name = "Головна сторінка"
        verbose_name_plural = "Налаштування головної сторінки"

    def __str__(self):
        return "Контент головної сторінки"


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    head_of_department = models.CharField(max_length=255, verbose_name="Завідувач кафедри")

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    code = models.CharField(max_length=20, verbose_name="Код")
    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=255, verbose_name="Імʼя координатора набору")
    coordinator_contact = models.CharField(max_length=255, verbose_name="Контакт координатора")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs', verbose_name="Випускова кафедра")
    subjects = models.TextField(verbose_name="Список дисциплін", help_text="Вводьте через кому або з нового рядка")

    class Meta:
        verbose_name = "Спецiальнiсть"
        verbose_name_plural = "Спецiальності"

    def __str__(self):
        return f"{self.code} - {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Імʼя")
    position = models.CharField(max_length=255, verbose_name="Посада")
    degree = models.CharField(max_length=255, verbose_name="Науковий ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', verbose_name="Кафедра")

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.name


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255, verbose_name="Університет")
    university_name = models.CharField(max_length=255, verbose_name="Назва університету", null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name="Країна", null=True, blank=True)
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    places = models.CharField(max_length=100, verbose_name="Кількість місць (старе)", null=True, blank=True)
    places_count = models.IntegerField(verbose_name="Кількість місць", null=True, blank=True)
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return f"{self.university}"

    @property
    def is_open(self):
        return self.deadline >= timezone.now().date()