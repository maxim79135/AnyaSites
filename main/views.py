from django.shortcuts import render,redirect
from .models import Diary
from .models import Parameter
from .models import Workout
from .models import Marathon
from .forms import DiaryForm
from .forms import WorkoutForm
from .forms import ParameterForm

from django.views.generic import UpdateView


def index(request):
    return render(request, 'main/index.html')

def parameter(request):
    parameters=Parameter.objects.order_by('-date')
    return render(request, 'main/parameter.html',{'title':'Параметры','parameters':parameters})

def diary(request):
    notes=Diary.objects.order_by('-id')
    return render(request, 'main/diary.html',{'title':'Дневник питания','notes':notes})

def workout(request):
    notes=Workout.objects.order_by('-id')
    return render(request, 'main/workout.html',{'title':'Тренировки','notes':notes})

def marathon(request):
    id = request.GET.get('id')
    if id != None:
        notes=Marathon.objects.order_by('-id').filter(id=id)
        return render(request, 'main/marathon.html',{'title':'Марафон','notes':notes})


def create_diary(request):
    error =''
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary')
        else:
            error ='Заполнено некорректно'

    form=DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_diary.html',context)

class update_diary(UpdateView):
    model = Diary
    template_name = 'main/create_diary.html'

    form_class = DiaryForm

def create_parameter(request):
    error =''
    if request.method == 'POST':
        form = ParameterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/parameter')
        else:
            error ='Заполнено некорректно'

    form=ParameterForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_parameter.html',context)

class update_parameter(UpdateView):
    model = Parameter
    template_name = 'main/create_parameter.html'

    form_class = ParameterForm

def create_workout(request):
    error = ''
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout')
        else:
            error = 'Заполнено некорректно'

    form = WorkoutForm()
    context = {
        'form': form
     }
    return render(request, 'main/create_workout.html', context)

