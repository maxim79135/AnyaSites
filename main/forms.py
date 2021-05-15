from django.forms import ModelForm,TextInput,Textarea,Select,DateInput
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms.fields import ImageField
from django.forms.fields import FileInput

class TitleChoiceField(forms.Form):

        марафон = forms.ModelChoiceField(queryset=Marathon.objects.values_list("title", flat=True).distinct(),empty_label=None)

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

class LectionForm(ModelForm):
    class Meta:
        model=Lection
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

class PostForm(ModelForm,forms.Form):
    class Meta:
            model = Post
            fields = ["title", "date", "description","img", "marathon"]
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

                "img": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ссылку на картинку'
                }),

                "marathon": Select(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите марафон'
                }),


    }

    # img = forms.ImageField()


class MarathonForm(ModelForm):
    class Meta:
        model=Marathon
        fields=["title","season","date_start","date_end"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "season": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сезон'
            }),
            "date_start": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "date_end": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),


        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["last_name","first_name","username","email","password","is_staff"]
        widgets = {
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
             "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),

        }




class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = ["date", "height", "weight", "girth_breast", "girth_waist", "girth_hips","girth_shoulders","girth_arm","girth_leg","marathon","user"]
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
            #"user": Select(attrs={
             #   'class': 'form-control',
              #  'placeholder': 'Введите фамилию'
            #}),

        }

class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields=["title","date","breakfast","lunch","dinner","snack","comment","marathon","user"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "breakfast": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
            "lunch": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
            "dinner": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
            "snack": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            }),
             # "marathon": Select(attrs={
             #     'class': 'form-control',
             #     'placeholder': 'Введите марафон'
             # }),
            #"user": Select(attrs={
             #   'class': 'form-control',
              #  'placeholder': 'Введите фамилию'
            #}),



        }

class ContractForm(ModelForm):
    class Meta:
        model=Contract
        fields=["date","user","marathon"]
        widgets = {
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),

            "user": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите клиента'
            }),
            "marathon": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Введите марафон'
            }),

        }
#
# class ImageUploadForm(forms.Form):
#     image = forms.ImageField()


