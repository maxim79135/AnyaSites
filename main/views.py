from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
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
def marathon(request):
    notes = Marathon.objects.order_by('-date_start')
    workout=Workout.objects.all()
    lection = Workout.objects.all()
    post = Workout.objects.all()
    contract = Contract.objects.all()

    #t = mar.workout_set.count()
    return render(request, 'main/marathon.html',{'title':'Марафон','notes': notes,'workout':workout,'lection':lection,'post':post,'contract':contract})

@login_required
def client(request):
    search_query = request.GET.get('search')
    if search_query:
        notes = User.objects.order_by('last_name').filter(is_superuser=0, last_name=search_query)
    else:
        notes = User.objects.order_by('last_name').filter(is_superuser=0)
    return render(request, 'main/client.html', {'title': 'Клиенты', 'notes': notes})

@login_required
def parameter(request,id):

    search_query=request.GET.get('search')

    user_role = request.user.is_superuser
    #id = int(request.GET.get('id'))
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
        #return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters})
        return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters, 'marathon_id': id})



@login_required
def diary(request,id):
  search_query = request.GET.get('search')
  user_role=request.user.is_superuser
  mar=Marathon.objects.order_by('-id')
  if user_role == 0:
    try:
        #id = int(request.GET.get('id'))
        notes=Diary.objects.order_by('-date').filter(marathon_id=id, user=request.user)
        return render(request, 'main/diary.html',{'title':'Дневник питания','notes':notes,'mar':mar})
    except:
        notes = Diary.objects.order_by('-date')
        return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes,'mar':mar})
  else:
      if search_query:
      #id = int(request.GET.get('id'))
        notes = Diary.objects.order_by('-date').filter(marathon_id=id,user__last_name=search_query)
      else:
        notes = Diary.objects.order_by('-date').filter(marathon_id=id)
      return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes, 'marathon_id':id,'mar':mar})

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
        'form': form,
        'error':error
     }
    return render(request, 'main/create_workout.html', context)


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
def post(request):
    try:
        id = int(request.GET.get('id'))
        posts=Post.objects.order_by('-date').filter(marathon_id=id)
        return render(request, 'main/post.html',{'title':'Посты','posts':posts})
    except:
        posts = Post.objects.order_by('-date')
        return render(request, 'main/post.html', {'title': 'Посты', 'posts': posts})


@login_required
def marathon_workout(request):

        notes = Marathon.objects.order_by('-id')
        return render(request, 'main/marathon_workout.html',{'title': 'Марафон', 'notes': notes})

@login_required
def marathon_parameter(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_parameter.html', {'title': 'Марафон', 'notes': notes})

@login_required
def marathon_post(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_post.html', {'title': 'Марафон', 'notes': notes})


@login_required
def marathon_diary(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_diary.html', {'title': 'Марафон', 'notes': notes})

@login_required
def marathon_lection(request):
    notes = Marathon.objects.order_by('-id')
    return render(request, 'main/marathon_lection.html', {'title': 'Марафон', 'notes': notes})



def upload_pic(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            m = Post.objects.get(pk=id)
            m.model_pic = form.cleaned_data['img']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

@login_required
def create_diary(request, id):

    error =''
    if request.method == 'POST':
        #form = DiaryForm(request.POST)
        id_marathon = request.GET["id"]
        req_data = request.POST.copy()
        req_data['user'] = request.user
        req_data['marathon'] = id_marathon
        # print(req_data)
        form = DiaryForm(req_data)

        if form.is_valid():
            form.save()
            user_role = request.user.is_superuser
            if user_role == 1:
                #return redirect('diary')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                notes = Diary.objects.order_by('-id').filter(user=request.user)
                return render(request, 'main/diary.html', {'title': 'Дневник питания', 'notes': notes})
        else:
            error ='Заполнено некорректно'

    form=DiaryForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create_diary.html',context)

class update_diary(UpdateView):
    model = Diary
    template_name = 'main/create_diary.html'

    form_class = DiaryForm

class delete_diary(DeleteView):
    model = Diary
    success_url = "/marathon_diary"
    template_name = 'main/delete_diary.html'




@login_required
def create_parameter(request):
    error =''
    if request.method == 'POST':
        #form = ParameterForm(request.POST)
        req_data = request.POST.copy()
        req_data['user'] = request.user
        form = ParameterForm(req_data)
        if form.is_valid():
            form.save()
            #return redirect('/parameter')
            parameters = Parameter.objects.order_by('-date').filter(user=request.user)
            return render(request, 'main/parameter.html', {'title': 'Параметры', 'parameters': parameters})
        else:
            error ='Заполнено некорректно'

    form=ParameterForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request, 'main/create_parameter.html',context)


class update_parameter(UpdateView):
    model = Parameter
    template_name = 'main/create_parameter.html'

    form_class = ParameterForm

class delete_parameter(DeleteView):
    model = Parameter
    success_url = "/marathon_parameter"
    template_name = 'main/delete_parameter.html'






@login_required
def create_client(request):
    error = ''
    if request.method == 'POST':
        req_staff = request.POST.copy()
        req_staff['is_staff'] = 1
        form = UserForm(req_staff)
        if form.is_valid():
            form.save()
            return redirect('client')
        else:
            error = 'Заполнено некорректно'

    form = UserForm()
    context = {
        'form': form,
        'error':error
     }
    return render(request, 'main/create_client.html', context)


@login_required
def create_contract(request):
    error = ''
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract')
        else:
            error = 'Заполнено некорректно'

    form = ContractForm()
    context = {
        'form': form,
        'error': error
     }
    return render(request, 'main/create_contract.html', context)



@login_required
def create_marathon(request):
    error = ''
    if request.method == 'POST':
        form = MarathonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marathon')
        else:
            error = 'Заполнено некорректно'

    form = MarathonForm()
    context = {
        'form': form,
        'error':error,
     }
    return render(request, 'main/create_marathon.html', context)


@login_required
def create_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # m = Post.objects.get(pk=id)
            # m.img = form.cleaned_data['img']
            # m.save()
            form.save()
            return redirect('post')
        else:
            error = 'Заполнено некорректно'

    form = PostForm()
    context = {
        'form': form,
        'error': error
     }
    return render(request, 'main/create_post.html', context)


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
        'form': form,
        'error':error
     }
    return render(request, 'main/create_lection.html', context)



class update_lection(UpdateView):
    model = Lection
    template_name = 'main/create_lection.html'

    form_class = LectionForm

class delete_lection(DeleteView):
    model = Lection
    success_url = "/marathon_lection"
    template_name = 'main/delete_lection.html'


class delete_workout(DeleteView):
    model = Workout
    success_url = "/marathon_workout"
    template_name = 'main/delete_workout.html'


class delete_client(DeleteView):
    model = User
    success_url = "/client"
    template_name = 'main/delete_client.html'


class update_post(UpdateView):
    model = Post
    template_name = 'main/create_post.html'

    form_class = PostForm

class delete_post(DeleteView):
    model = Post
    success_url = "/marathon_post"
    template_name = 'main/delete_post.html'

class update_marathon(UpdateView):
    model = Marathon
    template_name = 'main/create_marathon.html'

    form_class = MarathonForm

