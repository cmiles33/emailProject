from django.urls import path
from . import views

app_name = 'retranslation'

urlpatterns = [
    path('',views.list_programs, name='list_programs'),
    path('<slug:user>/<slug:programname>',views.program_detail,
         name='program_detail')
]