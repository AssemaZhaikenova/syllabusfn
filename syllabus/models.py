from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Discipline(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name='Код')
    name = models.CharField(max_length=255, verbose_name='Дисциплина')

    def __str__(self):
        return f'{self.code} - {self.name}'

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class EducationLevel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Уровень обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень обучения'
        verbose_name_plural = 'Уровень обучения'


class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name='Язык обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык обучения'
        verbose_name_plural = 'Язык обучения'


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email', unique=True)
    position = models.CharField(max_length=100, verbose_name='Должность', default='Преподаватель')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class LanguageProficiency(models.Model):
    level = models.CharField(max_length=50, verbose_name='Уровень владения языком')

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровень владения языком'


class TeachingFormat(models.Model):
    format_name = models.CharField(max_length=50, verbose_name='Формат обучения')

    def __str__(self):
        return self.format_name

    class Meta:
        verbose_name = 'Формат обучения'
        verbose_name_plural = 'Формат обучения'


class Director(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = models.CharField(max_length=15, verbose_name='Телефонный номер', blank=True, null=True)
    position = models.CharField(max_length=100, verbose_name='Должность', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директоры'


class Approval(models.Model):
    syllabus_item = models.ForeignKey('Syllabus', on_delete=models.CASCADE, related_name='approvals', verbose_name='Силлабус')
    director = models.ForeignKey('Director', on_delete=models.CASCADE, verbose_name='Директор')

    def __str__(self):
        return f'{self.syllabus_item.name} - {self.director.full_name}'

    class Meta:
        verbose_name = 'Согласование'
        verbose_name_plural = 'Согласовывание'


class Syllabus(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, verbose_name='Название силлабуса')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, verbose_name='Дисциплина')
    education_level = models.ForeignKey('EducationLevel', on_delete=models.CASCADE, verbose_name='Уровень обучения')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык обучения')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    ects = models.IntegerField(verbose_name='Кредиты ECTS')
    total_hours = models.IntegerField(verbose_name='Всего часов')
    classroom_hours = models.IntegerField(verbose_name='Аудиторные часы')
    iw_hours = models.IntegerField(verbose_name='Самостоятельная работа (СРОП, СРО)')
    semester = models.IntegerField(verbose_name='Семестр')
    language_proficiency = models.ForeignKey('LanguageProficiency', on_delete=models.CASCADE, verbose_name='Уровень владения языком')
    prerequisites = models.CharField(max_length=255, verbose_name='Пререквизиты')
    educational_program = models.CharField(max_length=255, verbose_name='Образовательная программа')
    teaching_format = models.ForeignKey('TeachingFormat', on_delete=models.CASCADE, verbose_name='Формат обучения')
    time_class = models.CharField(max_length=255, verbose_name='Время и место проведения занятий')
    course_goal = models.TextField(verbose_name='Цель курса', default='Здесь может быть цель курса')
    approvals_syllabus = models.ManyToManyField('Director', through='Approval', blank=True, related_name='syllabus_approvals', verbose_name='Согласование')
    from_asu_repository = models.BooleanField(default=False, verbose_name='На основе ASU репозитории')

    def __str__(self):
        return f'{self.discipline.name} - {self.name}'

    class Meta:
        verbose_name = 'Силлабус'
        verbose_name_plural = 'Силлабус'


class LearningOutcome(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True)
    course_description = models.TextField(verbose_name='Описание курса', null=True)
    learning_outcome_course = models.TextField(verbose_name='Результаты обучения курса (РО курса)', null=True)
    learning_outcome_program = models.TextField(verbose_name='Результаты обучения образоватильной программы (РО ОП)', null=True)

    def __str__(self):
        syllabus_name = self.syllabus.name if self.syllabus else "No Syllabus"
        return f'{syllabus_name} - {self.course_description}'

    class Meta:
        verbose_name = 'Результат обучения'
        verbose_name_plural = 'Результат обучения'


class ThematicPlan(models.Model):
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, verbose_name='Силлабус', null=True)
    week = models.IntegerField(verbose_name='Неделя', null=True)
    topic = models.CharField(max_length=255, verbose_name='Тема / модуль')
    ro = models.CharField(max_length=255, verbose_name='РО курса, РО ОП', null=True)
    qm = models.CharField(max_length=255, verbose_name='Вопросы по теме/ модулю', null=True)
    tasks = models.CharField(max_length=255, verbose_name='Задания', null=True)
    lit = models.CharField(max_length=255, verbose_name='Литература', null=True)
    so = models.CharField(max_length=255, verbose_name='Структура оценок', null=True)

    def __str__(self):
        return f'{self.syllabus.name} - {self.topic}'

    class Meta:
        verbose_name = 'Тематический план'
        verbose_name_plural = 'Тематические планы'


class EvaluationSystem(models.Model):
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, verbose_name='Силлабус', null=True)
    tm = models.CharField(max_length=255, verbose_name='Тема / модуль', null=True)
    mp = models.CharField(max_length=255, verbose_name='Максимальный процент (%)', null=True)
    mv = models.CharField(max_length=255, verbose_name='Максимальный вес (%)', null=True)
    tb = models.CharField(max_length=255, verbose_name='Итого в баллах', null=True)
    vk = models.CharField(max_length=255, verbose_name='Всего за курс', null=True)

    def __str__(self):
        return f'{self.syllabus.name} - {self.tm}'

    class Meta:
        verbose_name = 'Система оценивания курса'
        verbose_name_plural = 'Системы оценивания курса'


class Literature(models.Model):
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, verbose_name='Силлабус')
    title = models.CharField(max_length=255, verbose_name='Обязательная литература', null=True, blank=True)
    author = models.CharField(max_length=255, verbose_name='Интернет ресурсы', null=True, blank=True)

    def __str__(self):
        return f'{self.syllabus.name} - {self.title}'

    class Meta:
        verbose_name = 'Литература'
        verbose_name_plural = 'Список литературы'


class PhilosophyAndPolicy(models.Model):
    syllabus = models.OneToOneField('Syllabus', on_delete=models.CASCADE, verbose_name='Силлабус')
    philosophy = models.TextField(verbose_name='Философия преподавания и обучения')
    policy = models.TextField(verbose_name='Политика курса')

    def __str__(self):
        return f'{self.syllabus.name} - Философия и политика курса'

    class Meta:
        verbose_name = 'Философия и политика курса'
        verbose_name_plural = 'Философия и политика курса'

