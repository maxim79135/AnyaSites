from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import *
from .models import *

from django.views.generic import UpdateView,DeleteView

@login_required
def index(request):
    mar_tit = Marathon.objects.all()
    mar_list = TitleChoiceField()

    context = {
        'mar_tit': mar_tit,
        'mar_list': mar_list,
     }
    return render(request, 'main/index.html',context)

@login_required
def parameter(request):

    search_query=request.GET.get('search')

    user_role = request.user.is_superuser
    id = int(request.GET.get('id'))
    if user_role == 0:
        try:
            parameters=Parameter.objects.order_by('-date').filter(marathon_id=id, user=request.user)
            return render(request, 'main/parameter.html',{'title':'Параметры','parameters':parameters})
        except:
            parameters = Parameter.objects.order_by('-date')
            return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters})
    else:
        if search_query:
            parameters=Parameter.objects.order_by('-date').filter(marathon_id=id,user__last_name=search_query)
        else:
            parameters = Parameter.objects.order_by('-date').filter(marathon_id=id)
        return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters})


@login_required
def post(request):
    posts=Post.objects.order_by('-date')
    return render(request, 'main/post.html',{'title':'Параметры','posts':posts})

@login_required
def diary(request):
  user_role=request.user.is_superuser
  if user_role == 0:
    try:
        id = int(request.GET.get('id'))
        notes=Diary.objects.order_by('-id').filter(marathon_id=id, user=request.user)
        return render(request, 'main/diary.html',{'title':'Дневник питания','notes':notes})
    except:
        notes = Diary.objects.order_by('-id')
        return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes})
  else:
      #id = int(request.GET.get('id'))
      notes = Diary.objects.order_by('-id')#filter(marathon_id=id)
      return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes})

@login_required
def workout(request):
    try:
        id = int(request.GET.get('id'))
        notes=Workout.objects.order_by('-date').filter(marathon_id=id)
        return render(request, 'main/workout.html',{'title':'Тренировки','notes':notes})
    except:
        notes = Workout.objects.order_by('-date')
        return render(request, 'main/workout.html',{'title':'Тренировки','notes':notes})

@login_required
def lection(request):
    try:
        id = int(request.GET.get('id'))
        notes=Lection.objects.order_by('-date').filter(marathon_id=id)
        return render(request, 'main/lection.html',{'title':'Лекции','notes':notes})
    except:
        notes = Lection.objects.order_by('-date')
        return render(request, 'main/lection.html',{'title':'Лекции','notes':notes})

@login_required
def marathon_workout(request):

        notes = Marathon.objects.order_by('-id')
        return render(request, 'main/marathon_workout.html',{'title': 'Марафон', 'notes': notes})

@login_required
def marathon_parameter(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_parameter.html', {'title': 'Марафон', 'notes': notes})

@login_required
def marathon_diary(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_diary.html', {'title': 'Марафон', 'notes': notes})

@login_required
def marathon_lection(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_lection.html', {'title': 'Марафон', 'notes': notes})

@login_required
def create_diary(request):

    error =''
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            user_role = request.user.is_superuser
            if user_role == 1:
                return redirect('diary')
            else:
                notes = Diary.objects.order_by('-id').filter(user=request.user)
                return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes})
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

class delete_diary(DeleteView):
    model = Diary
    success_url = "/"
    template_name = 'main/delete_diary.html'




@login_required
def create_parameter(request):
    error =''
    if request.method == 'POST':
        form = ParameterForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('/parameter')
            parameters = Parameter.objects.order_by('-date').filter(user=request.user)
            return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters})
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

class delete_parameter(DeleteView):
    model = Parameter
    success_url = "/"
    template_name = 'main/delete_parameter.html'




@login_required
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



class update_workout(UpdateView):
    model = Workout
    template_name = 'main/create_workout.html'

    form_class = WorkoutForm

@login_required
def create_lection(request):
    error = ''
    if request.method == 'POST':
        form = LectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lection')
        else:
            error = 'Заполнено некорректно'

    form = LectionForm()
    context = {
        'form': form
     }
    return render(request, 'main/create_lection.html', context)



class update_workout(UpdateView):
    model = Lection
    template_name = 'main/create_lection.html'

    form_class = LectionForm

