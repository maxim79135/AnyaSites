
from django.contrib import admin
from .models import Client
from .models import Marathon
from .models import Diary
from .models import Parameter
from .models import Workout


admin.site.register(Client)
admin.site.register(Marathon)
admin.site.register(Diary)
admin.site.register(Parameter)
admin.site.register(Workout)

