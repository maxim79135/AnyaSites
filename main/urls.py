
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
       path('', views.index, name='home'),
       path('parameter', views.parameter,name='parameter'),
       path('diary', views.diary, name='diary'),
       path('marathon_workout', views.marathon_workout, name='marathon_workout'),
       path('marathon_diary', views.marathon_diary, name='marathon_diary'),
       path('marathon_lection', views.marathon_lection, name='marathon_lection'),
       path('marathon_parameter', views.marathon_parameter, name='marathon_parameter'),
       path('workout', views.workout, name='workout'),
       path('lection', views.lection, name='lection'),
       path('post', views.post, name='post'),
       path('create_diary', views.create_diary, name='create_diary'),
       path('create_parameter', views.create_parameter, name='create_parameter'),
       path('create_workout', views.create_workout, name='create_workout'),
       path('create_lection', views.create_lection, name='create_lection'),
       path('<int:pk>/update_diary', views.update_diary.as_view(), name='update_diary'),
       path('<int:pk>/delete_diary', views.delete_diary.as_view(), name='delete_diary'),
       path('<int:pk>/update_parameter', views.update_parameter.as_view(), name='update_parameter'),
       path('<int:pk>/delete_parameter', views.delete_parameter.as_view(), name='delete_parameter'),
       path('<int:pk>/update_workout', views.update_workout.as_view(), name='update_workout'),
]

