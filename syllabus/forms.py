from django import forms
from .models import *


class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        exclude = ['created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class LearningOutcomeForm(forms.ModelForm):
    class Meta:
        model = LearningOutcome
        fields = ['course_description', 'learning_outcome_course', 'learning_outcome_program']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ThematicPlanForm(forms.ModelForm):
    class Meta:
        model = ThematicPlan
        fields = ['week', 'topic', 'ro', 'qm', 'tasks', 'lit', 'so']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EvaluationSystemForm(forms.ModelForm):
    class Meta:
        model = EvaluationSystem
        fields = ['tm', 'mp', 'mv', 'tb', 'vk']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LiteratureForm(forms.ModelForm):
    class Meta:
        model = Literature
        fields = ['title', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PhilosophyAndPolicyForm(forms.ModelForm):
    class Meta:
        model = PhilosophyAndPolicy
        fields = ['philosophy', 'policy']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
