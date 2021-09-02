from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'retranslation'

urlpatterns = [
    path('',views.list_programs, name='list_programs'),
    path('<slug:user>/<slug:programname>',views.program_detail,
         name='program_detail'),
    path('<slug:user>/<slug:programname>/<int:payloadnumber>', views.response_detail,
         name='response_detail'),
    #path('login/', views.user_login, name='login')
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]
