from .models import Diary
from .models import Parameter
from .models import Workout
from django.forms import ModelForm,TextInput,Textarea,Select,DateInput

class WorkoutForm(ModelForm):
    class Meta:
        model=Workout
        fields=["title","date","description","video","marathon"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "video": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на видео'
            }),
            "marathon": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марафон'
            }),

        }

class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = ["date", "height", "weight", "girth_breast", "girth_waist", "girth_hips","girth_shoulders","girth_arm","girth_leg","marathon","client"]
        widgets = {
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "height": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите рост'
            }),
            "weight": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вес'
            }),
            "girth_breast": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват груди'
            }),
            "girth_waist": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват талии'
            }),
            "girth_hips": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват бёдер'
            }),
            "girth_shoulders": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват плеч'
            }),
            "girth_arm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват руки'
            }),
            "girth_leg": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обхват ноги'
            }),

            "marathon": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марафон'
            }),
            "client": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),

        }

class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields=["title","date","description","comment","marathon","client"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            }),
            "marathon": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марафон'
            }),
            "client": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),



        }


