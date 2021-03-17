
from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='home'),
       path('parameter', views.parameter,name='parameter'),
       path('diary', views.diary, name='diary'),
       path('marathon', views.marathon, name='marathon'),
       path('workout', views.workout, name='workout'),
       path('create_diary', views.create_diary, name='create_diary'),
       path('create_parameter', views.create_parameter, name='create_parameter'),
       path('create_workout', views.create_workout, name='create_workout'),
       path('<int:pk>/update', views.update_diary.as_view(), name='update_diary'),
       path('<int:pk>/update_par', views.update_parameter.as_view(), name='update_parameter')
]