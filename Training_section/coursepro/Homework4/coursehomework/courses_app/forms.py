from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'info']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Input title', 'class': 'form-control',}),
            'info': forms.TextInput(attrs={'placeholder': 'Input title', 'class': 'form-control'}),
        }