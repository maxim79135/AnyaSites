
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
       path('', views.index, name='home'),
       path('client', views.client, name='client'),
       path('marathon', views.marathon, name='marathon'),
       path('parameter', views.parameter,name='parameter'),
       path('diary', views.diary, name='diary'),
       path('marathon_workout', views.marathon_workout, name='marathon_workout'),
       path('marathon_diary', views.marathon_diary, name='marathon_diary'),
       path('marathon_lection', views.marathon_lection, name='marathon_lection'),
       path('marathon_parameter', views.marathon_parameter, name='marathon_parameter'),
       path('marathon_post', views.marathon_post, name='marathon_post'),
       path('workout', views.workout, name='workout'),
       path('lection', views.lection, name='lection'),
       path('post', views.post, name='post'),
       path('create_diary', views.create_diary, name='create_diary'),
       path('create_post', views.create_post, name='create_post'),
       path('create_parameter', views.create_parameter, name='create_parameter'),
       path('create_workout', views.create_workout, name='create_workout'),
       path('create_lection', views.create_lection, name='create_lection'),
       path('create_contract', views.create_contract, name='create_contract'),
       path('create_marathon', views.create_marathon, name='create_marathon'),
       path('create_client', views.create_client, name='create_client'),
       path('<int:pk>/update_marathon', views.update_marathon.as_view(), name='update_marathon'),
       path('<int:pk>/update_diary', views.update_diary.as_view(), name='update_diary'),
       path('<int:pk>/delete_diary', views.delete_diary.as_view(), name='delete_diary'),
       path('<int:pk>/update_parameter', views.update_parameter.as_view(), name='update_parameter'),
       path('<int:pk>/delete_parameter', views.delete_parameter.as_view(), name='delete_parameter'),
       path('<int:pk>/update_workout', views.update_workout.as_view(), name='update_workout'),
       path('<int:pk>/delete_workout', views.delete_workout.as_view(), name='delete_workout'),
       path('<int:pk>/update_lection', views.update_lection.as_view(), name='update_lection'),
       path('<int:pk>/delete_lection', views.delete_lection.as_view(), name='delete_lection'),
       path('<int:pk>/update_post', views.update_post.as_view(), name='update_post'),
       path('<int:pk>/delete_post', views.delete_post.as_view(), name='delete_post'),
       path('<int:pk>/delete_client', views.delete_client.as_view(), name='delete_client'),
]


