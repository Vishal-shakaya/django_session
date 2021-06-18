
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-session/', views.SetSession, name='set_session'),
    path('get-session/', views.GetSession, name='get_session'),
    path('del-session/', views.DeleteSession, name='del_session'),
]
