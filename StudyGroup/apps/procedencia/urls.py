from django.conf.urls import include, url
from django.contrib import admin
from .views import ListarDepartamentoView

urlpatterns = [
    # Examples:
    # url(r'^$', 'StudyGroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^departamentos/$', ListarDepartamentoView.as_view(), name='Lista_Departamentos'),
]