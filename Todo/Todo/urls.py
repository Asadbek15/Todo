
from django.contrib import admin
from django.urls import path
from .app1.views  import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', admin.site.urls),
    path('reja/', admin.site.urls),
]
