from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^login/',views.login_page,name='login'),
	url(r'^cadastrar/',views.cad_page, name = 'cadastrar'),
]
